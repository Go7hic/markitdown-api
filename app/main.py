# app/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(
    title="MarkItDown API",
    description="API for converting documents to Markdown format",
    version="1.0.0"
)

# origins = [
#     "http://localhost:5173",    # Vite 开发服务器默认端口
#     "http://localhost:4173",    # Vite 预览端口
#     "http://127.0.0.1:5173",
#     "http://127.0.0.1:4173",
# ]

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://markitdown.up.railway.app"],  # Vite 开发服务器的地址
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to MarkItDown API"}