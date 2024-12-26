# app/main.py
from app.middleware.rate_limit import RateLimitMiddleware
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes import router as api_router

app = FastAPI(
    title="MarkItDown API",
    description="API for converting documents to Markdown format",
    version="1.0.0"
)

# 添加速率限制中间件
# app.add_middleware(
#     RateLimitMiddleware,
#     requests_per_minute=10
# )

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "https://markitdown.up.railway.app", "https://www.markitdown.tools", "https://markitdown.tools"],  # Vite 开发服务器的地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include API routes
app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "Welcome to MarkItDown API"}