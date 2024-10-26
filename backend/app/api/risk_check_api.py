from fastapi import APIRouter, HTTPException
from app.spider.google import RiskChecker

router = APIRouter()

# 配置 API Key 和搜索引擎 ID，用于 Google 风险检查
api_key = "your_api_key_here"
search_engine_id = "your_search_engine_id_here"
risk_checker = RiskChecker(api_key, search_engine_id)

@router.get("/check-risk")
async def check_company_risk(company_name: str):
    try:
        results = risk_checker.check_company_risks(company_name)
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Company Risk Check Error: {str(e)}")
