try:
    from fastapi import FastAPI, APIRouter
    import uvicorn
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI(title='demo')
router = APIRouter(prefix='/v1', tags=['demo'])

@app.get('/')                        # 方式一:装饰器直接注册
def root():
    return {'msg': 'hello fastapi'}

@router.get('/items/{item_id}')      # 方式二:APIRouter,前缀 /v1
def read_item(item_id: int):
    return {'item_id': item_id}

app.include_router(router)           # 汇总 router

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)  # 文档: /docs
