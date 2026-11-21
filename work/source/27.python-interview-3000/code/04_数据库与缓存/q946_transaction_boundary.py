"""Service 层装饰器管理事务: 嵌套调用共享同一事务"""
import functools
import sqlite3

def transactional(func):
    @functools.wraps(func)
    def wrapper(ctx, *a, **kw):
        if ctx.get("in_tx"):                # 传播: 已在事务中直接复用
            return func(ctx, *a, **kw)
        ctx["in_tx"] = True
        try:
            result = func(ctx, *a, **kw)
            ctx["conn"].commit()
            return result
        except Exception:
            ctx["conn"].rollback()
            raise
        finally:
            ctx["in_tx"] = False
    return wrapper

@transactional
def create_order(ctx, sku, qty):
    ctx["conn"].execute("INSERT INTO orders (sku, qty) VALUES (?, ?)", (sku, qty))
    deduct_stock(ctx, sku, qty)             # 同一事务

@transactional
def deduct_stock(ctx, sku, qty):
    n = ctx["conn"].execute(
        "UPDATE stock SET qty = qty - ? WHERE sku = ? AND qty >= ?",
        (qty, sku, qty)).rowcount
    if n == 0:
        raise ValueError("库存不足, 整体回滚")

if __name__ == "__main__":
    conn = sqlite3.connect(":memory:")
    conn.execute("CREATE TABLE orders (sku TEXT, qty INT)")
    conn.execute("CREATE TABLE stock (sku TEXT PRIMARY KEY, qty INT)")
    conn.execute("INSERT INTO stock VALUES ('x', 5)")
    ctx = {"conn": conn, "in_tx": False}

    create_order(ctx, "x", 2)
    print("成功: 订单", conn.execute("SELECT count(*) FROM orders").fetchone()[0],
          "库存", conn.execute("SELECT qty FROM stock").fetchone()[0])
    try:
        create_order(ctx, "x", 99)
    except ValueError as e:
        print("失败:", e)
    print("回滚后订单仍为", conn.execute("SELECT count(*) FROM orders").fetchone()[0])
