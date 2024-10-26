from fastapi import APIRouter, HTTPException
from app.spider.org_spider import AustralianCompanySearcher

router = APIRouter()

@router.get("/australian")
async def search_australian_company(query: str):
    try:
        searcher = AustralianCompanySearcher()
        results = searcher.get_australian_companies(query)
        return {"results": results.to_dict(orient='records')}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Australian Company Search Error: {str(e)}")
