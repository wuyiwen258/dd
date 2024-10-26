
from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.db.init_db import init_db
from app.api import api_router  # 假设有一个通用的 API 路由模块
from app.api.asic_search_api import router as asic_router
from app.api.australian_search_api import router as australian_router
from app.api.risk_check_api import router as risk_router
from fastapi.middleware.cors import CORSMiddleware



# 配置 CORS 中间件

@asynccontextmanager
async def lifespan(app: FastAPI):
    await init_db(app)
    yield

# 创建 FastAPI 应用
app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tiny-starship-bd07ed.netlify.app"],  # 可以根据实际需求限制允许的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# 包含全局 API 路由
app.include_router(api_router)

# 注册各个模块的 API 路由
app.include_router(asic_router, prefix="/search", tags=["ASIC Search"])
app.include_router(australian_router, prefix="/search", tags=["Australian Search"])
app.include_router(risk_router, prefix="/search", tags=["Risk Check"])

# 根路径
@app.get("/")
def read_root():
    return {"message": "Welcome to the Research Due Diligence System"}
