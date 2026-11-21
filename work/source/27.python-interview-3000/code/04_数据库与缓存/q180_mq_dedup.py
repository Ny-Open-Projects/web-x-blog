"""消费端幂等: Redis SETNX 去重 + 失败释放重投"""
import itertools


class FakeRedis:
    def __init__(self):
        self._set: set = set()

    def setnx(self, key: str) -> bool:
        if key in self._set:
            return False
        self._set.add(key)          # 真实命令: SET key 1 NX EX 86400
        return True

    def delete(self, key: str) -> None:
        self._set.discard(key)


class Consumer:
    def __init__(self):
        self.redis = FakeRedis()
        self.processed: list = []
        self._ids = itertools.count()

    def consume(self, message: dict) -> None:
        msg_id = message["id"]
        key = f"dedup:{msg_id}"
        if not self.redis.setnx(key):
            print(f"消息 {msg_id} 重复, 直接 ACK 跳过")
            return
        try:
            self.processed.append(message)
            print(f"消息 {msg_id} 业务处理完成")
        except Exception:
            self.redis.delete(key)   # 失败释放标记, 让 MQ 重投
            raise


if __name__ == "__main__":
    c = Consumer()
    c.consume({"id": "m1", "payload": "order-42"})
    c.consume({"id": "m1", "payload": "order-42"})   # 重复投递
    c.consume({"id": "m2", "payload": "order-43"})
    print("实际处理:", [m["id"] for m in c.processed])
