"""两个独立 Engine 的数据源注册中心 + 按域路由"""

try:
    from sqlalchemy import create_engine, text
except ImportError:
    print("该题演示需要第三方库 sqlalchemy:pip install sqlalchemy>=2.0,原理见正文")
    raise SystemExit(0)

class DataSources:
    def __init__(self):
        self._engines = {}

    def register(self, name, url, **pool_opts):
        self._engines[name] = create_engine(url, **pool_opts)

    def engine(self, name):
        if name not in self._engines:
            raise KeyError(f"数据源 {name} 未注册")
        return self._engines[name]

if __name__ == "__main__":
    ds = DataSources()
    ds.register("orders", "sqlite:///q922_orders.db")
    ds.register("users", "sqlite:///q922_users.db")

    with ds.engine("users").begin() as c:
        c.execute(text("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)"))
        c.execute(text("INSERT OR IGNORE INTO users (name) VALUES ('alice')"))
    with ds.engine("orders").begin() as c:
        c.execute(text("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INT)"))
        c.execute(text("INSERT INTO orders (user_id) VALUES (1)"))

    uid = ds.engine("users").connect().execute(
        text("SELECT id FROM users WHERE name='alice'")).scalar()
    n = ds.engine("orders").connect().execute(
        text("SELECT count(*) FROM orders WHERE user_id=:u"), {"u": uid}).scalar()
    print(f"用户 {uid} 的订单数: {n}  <- 跨库由应用层协调, 非同一事务")
