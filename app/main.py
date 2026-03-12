from fastapi import FastAPI
from app.api.endpoints import router

app = FastAPI()
app.include_router(router, prefix="/api/v1", tags=["CEP"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="[IP_ADDRESS]", port=8000)