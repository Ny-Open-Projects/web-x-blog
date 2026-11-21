import time
from collections import defaultdict, deque
try:
    from fastapi import FastAPI, Request, Response
    from fastapi.responses import JSONResponse
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
WINDOW = 10       # 秒
LIMIT = 5         # 每窗口最多 5 次
hits: dict[str, deque] = defaultdict(deque)

@app.middleware('http')
async def rate_limit(request: Request, call_next):
    # 生产: 真实 IP 从 X-Forwarded-For 解析且只信任可信代理
    ip = request.client.host if request.client else 'unknown'
    now = time.monotonic()
    q = hits[ip]
    while q and q[0] <= now - WINDOW:
        q.popleft()
    if len(q) >= LIMIT:
        return JSONResponse(status_code=429,
                            content={'detail': 'too many requests'})
    q.append(now)
    return await call_next(request)

@app.get('/ping')
def ping():
    return {'msg': 'pong'}
