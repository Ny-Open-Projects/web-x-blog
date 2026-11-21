try:
    from fastapi import FastAPI, Depends
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
counter = {'n': 0}

def expensive_check() -> str:
    counter['n'] += 1
    return f'check-{counter["n"]}'

def handler_a(v: str = Depends(expensive_check)):
    return v

def handler_b(v: str = Depends(expensive_check)):   # 与 A 共享缓存
    return v

@app.get('/once')
def once(a=Depends(handler_a), b=Depends(handler_b)):
    return {'a': a, 'b': b}   # expensive_check 同一请求只执行 1 次

@app.get('/fresh')
def fresh(a=Depends(handler_a, use_cache=False),
          b=Depends(handler_b, use_cache=False)):
    return {'a': a, 'b': b}   # 各执行 1 次,结果不同
