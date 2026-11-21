"""CSP 头构造与 nonce 注入(纯标准库,fastapi 可用时挂中间件)。"""
import secrets

try:
    from fastapi import FastAPI, Request
    HAS_FASTAPI = True
except ImportError:
    HAS_FASTAPI = False
    print("[降级] 未安装 fastapi,以下演示头构造逻辑")


def csp_header(nonce):
    return "; ".join([
        "default-src 'self'",
        f"script-src 'self' 'nonce-{nonce}' 'strict-dynamic'",
        "style-src 'self'",
        "img-src 'self' data:",
        "object-src 'none'",
        "base-uri 'self'",
        "frame-ancestors 'none'",
    ])


if HAS_FASTAPI:
    app = FastAPI()

    @app.middleware("http")
    async def csp_middleware(request: Request, call_next):
        response = await call_next(request)
        response.headers["Content-Security-Policy"] = csp_header(secrets.token_urlsafe(16))
        return response
    print("[fastapi] 已注册 CSP 中间件示例")

nonce = secrets.token_urlsafe(16)
header = csp_header(nonce)
print(header)
assert f"nonce-{nonce}" in header and "'unsafe-inline'" not in header
print("页面脚本写法:", f'<script nonce="{nonce}">')
