from contextlib import asynccontextmanager
try:
    from fastapi import FastAPI
    import uvicorn
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

pool: dict = {}

@asynccontextmanager
async def lifespan(app: FastAPI):
    pool['redis'] = 'fake-redis-conn'     # startup:初始化连接池/加载配置
    print('app starting, pool ready')
    yield
    pool.clear()                          # shutdown:释放资源
    print('app shutting down, pool closed')

app = FastAPI(lifespan=lifespan)

@app.get('/cache')
def read_cache():
    return {'redis': pool.get('redis')}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
