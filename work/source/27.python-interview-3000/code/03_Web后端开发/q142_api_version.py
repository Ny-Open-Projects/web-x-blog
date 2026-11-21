try:
    from fastapi import FastAPI, APIRouter, Request
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI(title='versioned api')

v1 = APIRouter(prefix='/v1', deprecated=True)   # 标记废弃
v2 = APIRouter(prefix='/v2')

@v1.get('/users/{uid}')
def get_user_v1(uid: int):
    return {'id': uid, 'name': 'alice', 'email': 'a@x.com'}

@v2.get('/users/{uid}')
def get_user_v2(uid: int, request: Request):
    # v2 只加字段不改语义:向后兼容,不破坏 v1 客户端
    return {'id': uid, 'name': 'alice',
            'profile': {'email': 'a@x.com'}}

app.include_router(v1)
app.include_router(v2)
