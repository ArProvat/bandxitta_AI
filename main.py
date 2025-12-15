import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.services.Chat.Chat_router import router as chatRouter


app = FastAPI(title="Firecomm AI API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,     
    allow_methods=["*"],
    allow_headers=["*"]
    )


app.include_router(chatRouter ,tags=['Chat'])


@app.get("/",tags = ["health"])
async def root():
    return """
"message": "Welcome to the firecomme AI!",
        "status": "healthy",
        "version": "1.0.0"
"""

@app.get("/health", tags=["Health"])
async def health_check():
    """Health check endpoint for Docker/monitoring"""
    return {
        "status": "healthy",
        "service": "firecomme AI"
    }



if __name__ == "__main__":
    uvicorn.run(
        "main:app", 
        host="0.0.0.0", 
        port=8000, 
        reload=True
    )
