try:
    from fastapi import FastAPI, Request
    from fastapi.responses import JSONResponse
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class BizError(Exception):
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

@app.exception_handler(BizError)
async def biz_error_handler(request: Request, exc: BizError):
    return JSONResponse(
        status_code=400,
        content={'code': exc.code, 'message': exc.message,
                 'path': request.url.path},
    )

@app.get('/items/{item_id}')
def get_item(item_id: int):
    if item_id > 100:
        raise BizError(40001, 'item not found')
    return {'id': item_id}
