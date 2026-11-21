"""纯逻辑模拟 N+1 与两种批量加载的查询次数对比"""


class FakeDB:
    def __init__(self):
        self.users = {1: "alice", 2: "bob", 3: "carol"}
        self.orders = [{"id": i, "user_id": i % 3 + 1} for i in range(1, 31)]
        self.queries = 0

    def get_orders(self) -> list:
        self.queries += 1
        return self.orders

    def get_user(self, uid: int):
        self.queries += 1
        return self.users.get(uid)

    def get_users(self, uids: list) -> dict:
        self.queries += 1
        return {u: self.users[u] for u in set(uids)}


def lazy_load(db: FakeDB) -> list:
    """典型 N+1: 访问每条订单的 user 都触发一次查询"""
    return [(o["id"], db.get_user(o["user_id"])) for o in db.get_orders()]


def selectin_load(db: FakeDB) -> list:
    """先取订单, 收集 user_id 后一次 IN 查询, 再内存组装"""
    orders = db.get_orders()
    users = db.get_users([o["user_id"] for o in orders])
    return [(o["id"], users[o["user_id"]]) for o in orders]


if __name__ == "__main__":
    for fn in (lazy_load, selectin_load):
        db = FakeDB()
        fn(db)
        print(f"{fn.__name__}: SQL 次数 = {db.queries}")
    # SQLAlchemy 中对应: selectinload(Order.user) 或 joinedload(Order.user)
