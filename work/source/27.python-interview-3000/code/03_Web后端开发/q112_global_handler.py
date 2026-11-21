import logging
import uuid
try:
    from fastapi import FastAPI, Request
    from fastapi.responses import JSONResponse
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

logger = logging.getLogger('app')
app = FastAPI()

@app.exception_handler(Exception)
async def unhandled_handler(request: Request, exc: Exception):
    rid = request.headers.get('x-request-id', str(uuid.uuid4())[:8])
    logger.exception('unhandled error rid=%s', rid)      # 完整堆栈进日志
    return JSONResponse(                                  # 对外脱敏
        status_code=500,
        content={'code': 50000, 'message': 'internal server error', 'rid': rid},
    )

@app.get('/boom')
def boom():
    return 1 / 0
