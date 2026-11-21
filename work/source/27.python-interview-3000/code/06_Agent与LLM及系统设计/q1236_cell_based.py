"""单元化:按用户 id 分片路由到单元,单元内闭环,跨单元数据只读同步。"""
import hashlib


class Cell:
    def __init__(self, name, user_shards):
        self.name, self.shards = name, set(user_shards)
        self.data, self.replica_from = {}, None      # 本单元写 + 异单元只读副本

    def write(self, user_id, kv):
        assert user_id % 100 in self.shards, f"{user_id} 不属于 {self.name}"
        self.data[user_id] = kv

    def read(self, user_id, cells):
        if user_id in self.data:
            return self.data[user_id]
        # 跨单元数据:只读副本(同步延迟由异步复制模拟)
        for c in cells:
            if c is not self and user_id in c.data:
                return c.data[user_id]
        return None


class Router:
    def __init__(self, cells, shard_of_user=lambda uid: uid % 100):
        self.cells, self.shard_fn = cells, shard_of_user

    def route(self, user_id):
        shard = self.shard_fn(user_id)
        for c in self.cells:
            if shard in c.shards:
                return c
        raise RuntimeError("路由表缺分片")

    def handle(self, user_id, op, kv=None):
        cell = self.route(user_id)
        if op == "write":
            cell.write(user_id, kv)
            return f"{cell.name} 写入"
        return f"{cell.name} 读取 {cell.read(user_id, self.cells)}"


if __name__ == "__main__":
    cells = [Cell("cell-hz", set(range(0, 50))), Cell("cell-sh", set(range(50, 100)))]
    router = Router(cells)
    print(router.handle(1001, "write", {"vip": True}))     # 1001%100=1 -> cell-hz
    print(router.handle(2050, "write", {"vip": False}))    # -> cell-sh
    assert router.route(1001).name == "cell-hz"
    assert router.route(2050).name == "cell-sh"

    # 单元故障:路由摘除 cell-sh,该单元用户不可写但 hz 用户无感
    cells_alive = [cells[0]]
    router2 = Router(cells_alive)
    print(router2.handle(1002, "write", {"vip": True}))
    try:
        router2.route(2077)
    except RuntimeError as e:
        print("故障单元用户路由失败(快速失败):", e)
    assert router2.route(1002).name == "cell-hz"
    print("爆炸半径=单元:hz 单元完全不受 sh 故障影响")
