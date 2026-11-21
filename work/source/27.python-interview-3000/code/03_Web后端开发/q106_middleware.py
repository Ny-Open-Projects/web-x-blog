import time
import uuid
try:
    from fastapi import FastAPI, Request
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.middleware('http')
async def add_request_id(request: Request, call_next):
    rid = request.headers.get('x-request-id', str(uuid.uuid4())[:8])
    start = time.perf_counter()
    response = await call_next(request)          # 交给内层处理
    cost = round((time.perf_counter() - start) * 1000, 2)
    response.headers['x-request-id'] = rid
    response.headers['x-cost-ms'] = str(cost)
    return response

@app.middleware('http')
async def log_requests(request: Request, call_next):
    print(f'-> {request.method} {request.url.path}')
    response = await call_next(request)
    print(f'<- {request.url.path} done')
    return response

@app.get('/')
def root():
    return {'msg': 'hello'}
