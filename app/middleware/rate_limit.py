# app/middleware/rate_limit.py
from fastapi import Request, HTTPException
from typing import Dict, Tuple
import time

class RateLimitMiddleware:
    def __init__(self, requests_per_minute: int = 10):
        self.requests_per_minute = requests_per_minute
        self.requests: Dict[str, list] = {}

    async def __call__(self, request: Request, call_next):
        # 获取客户端 IP
        client_ip = request.client.host
        current_time = time.time()

        # 清理过期的请求记录
        if client_ip in self.requests:
            self.requests[client_ip] = [
                req_time for req_time in self.requests[client_ip]
                if current_time - req_time < 60
            ]

        # 检查请求频率
        if client_ip in self.requests and len(self.requests[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please try again later."
            )

        # 记录新请求
        if client_ip not in self.requests:
            self.requests[client_ip] = []
        self.requests[client_ip].append(current_time)

        response = await call_next(request)
        return response