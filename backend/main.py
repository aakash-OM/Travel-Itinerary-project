from fastapi import FastAPI, Depends
from api.endpoints import router as api_router
from utils.config import settings
from utils.logger import logger
import uvicorn

app = FastAPI(
    title="Travel Genius API",
    description="AI-powered travel planning platform",
    version="1.0.0"
)

# Include API routes
app.include_router(api_router, prefix="/api/v1")

@app.on_event("startup")
async def startup_event():
    logger.info("Starting Travel Genius API server")
    # Initialize database connections, etc.

@app.on_event("shutdown")
async def shutdown_event():
    logger.info("Shutting down Travel Genius API server")
    # Clean up resources

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug_mode,
        workers=4
    )