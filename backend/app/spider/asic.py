from DrissionPage import ChromiumPage, ChromiumOptions

class ASICSearcher:
    def __init__(self):
        """
        初始化ASICSearcher类，配置ChromiumPage的选项。
        """
        self.options = ChromiumOptions()
        # 设置远程调试端口，确保与手动启动的Chrome浏览器保持一致
        self.options.debugger_address = '127.0.0.1:9222'  # 这个端口号应该与启动Chrome时一致
        self.options.set_argument('--no-sandbox')
        self.options.headless(True)  # 如果你不需要看到浏览器界面，可以保持headless为True

        try:
            self.page = ChromiumPage(self.options)  # 尝试连接到已启动的浏览器
        except Exception as e:
            print("浏览器连接失败:", e)
            raise

    def search_asic(self, query):
        """
        在ASIC页面搜索指定的公司名称，并返回搜索结果
        :param query: 公司名称或查询关键字
        :return: 返回搜索结果，列表形式
        """
        url = "https://connectonline.asic.gov.au/RegistrySearch/faces/landing/SearchRegisters.jspx"
        self.page.get(url)

        # 等待页面加载
        self.page.wait.load()

        # 查找搜索类型下拉框
        select_element = self.page.ele('#bnConnectionTemplate\\:r1\\:0\\:searchPanelLanding\\:dc1\\:s1\\:searchTypesLovId\\:\\:content')
        select_element.click()
        select_element.select.by_value(1)  # 注意这里可能要确保选项值正确
        input_element = self.page.ele('#bnConnectionTemplate\\:r1\\:0\\:searchPanelLanding\\:dc1\\:s1\\:searchForTextId\\:\\:content')
        input_element.clear()
        input_element.input(query)

        # 点击搜索按钮
        go_ele = self.page.ele('#bnConnectionTemplate\\:r1\\:0\\:searchPanelLanding\\:dc1\\:s1\\:searchButtonId')
        go_ele.click()

        # 等待结果加载
        self.page.wait.load()

        # 获取搜索结果
        table_eles = self.page.eles('@class=af_table_data-row')
        result_data = []
        for row in table_eles.filter.displayed():  # 筛选显示的行
            row_data = []
            span_eles = row.eles('t:span')
            for cell in span_eles:  # 筛选显示的列
                row_data.append(cell.text)
            result_data.append(row_data)

        return result_data

    def close(self):
        """
        关闭浏览器
        """
        self.page.close()

# 使用示例
if __name__ == "__main__":
    searcher = ASICSearcher()

    # 调用封装的函数并传入查询关键字
    query = 'BHP'
    try:
        results = searcher.search_asic(query)

        # 处理结果
        for row in results:
            print(row)
    finally:
        # 完成后关闭浏览器
        searcher.close()
