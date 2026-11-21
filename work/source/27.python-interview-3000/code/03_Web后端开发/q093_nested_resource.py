try:
    from fastapi import FastAPI, HTTPException
except ImportError:
    print("该题演示需要第三方库 fastapi:pip install fastapi[all],原理见正文")
    raise SystemExit(0)

app = FastAPI()
orders: dict[int, list[dict]] = {1: [{'id': 1, 'item': 'book'}]}

@app.get('/users/{user_id}/orders')          # 嵌套:用户下的订单
def user_orders(user_id: int):
    if user_id not in orders:
        raise HTTPException(404, 'user not found')
    return {'user_id': user_id, 'orders': orders[user_id]}

@app.get('/orders')                           # 平铺 + 查询参数过滤,更灵活
def all_orders(user_id: int | None = None):
    data = orders
    if user_id is not None:
        data = {user_id: orders.get(user_id, [])}
    return [{'user_id': uid, **o} for uid, lst in data.items() for o in lst]
