try:
    from fastapi import FastAPI, Query
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

@app.get('/search')
def search(
    keyword: str = Query(..., min_length=1, max_length=50),  # 必填
    page: int = Query(1, ge=1),                              # 可选带约束
    size: int = Query(10, le=100),
    tag: list[str] | None = Query(None),                     # ?tag=a&tag=b
    exact: bool = False,                                     # ?exact=true
):
    return {'keyword': keyword, 'page': page, 'size': size,
            'tags': tag or [], 'exact': exact}
