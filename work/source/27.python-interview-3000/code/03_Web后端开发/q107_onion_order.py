try:
    from fastapi import FastAPI, Request
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
trace: list[str] = []

def make_mw(name: str):
    async def mw(request: Request, call_next):
        trace.append(f'{name} in')
        response = await call_next(request)
        trace.append(f'{name} out')
        return response
    return mw

app.middleware('http')(make_mw('A'))   # A 先注册,处于内层
app.middleware('http')(make_mw('B'))   # B 后注册,处于外层

@app.get('/')
def root():
    trace.append('handler')
    return {'ok': True}
# 请求顺序:B in -> A in -> handler -> A out -> B out
