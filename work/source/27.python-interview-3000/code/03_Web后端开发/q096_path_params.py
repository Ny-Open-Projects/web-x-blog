from enum import Enum
try:
    from fastapi import FastAPI, Path
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()

class Category(str, Enum):
    book = 'book'
    food = 'food'

@app.get('/items/latest')            # 固定路径必须声明在动态路径之前
def latest():
    return {'id': 0, 'name': 'latest'}

@app.get('/items/{item_id}')
def read_item(item_id: int = Path(..., ge=1, description='商品 ID 大于 0')):
    return {'item_id': item_id}

@app.get('/categories/{category}')
def read_category(category: Category):
    return {'category': category.value}
