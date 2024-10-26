from fastapi import APIRouter, HTTPException
from app.spider.asic import ASICSearcher

router = APIRouter()

@router.get("/asic")
async def search_asic(query: str):
    try:
        searcher = ASICSearcher()
        results = searcher.search_asic(query)
        searcher.close()
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"ASIC Search Error: {str(e)}")
