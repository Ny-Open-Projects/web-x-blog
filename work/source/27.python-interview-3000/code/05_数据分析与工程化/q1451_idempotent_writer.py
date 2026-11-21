"""幂等写入器:按业务键 upsert,重放同一批次结果不变"""


class AppendSink:
    """反例:只追加的写入器,重放会产生重复数据"""

    def __init__(self):
        self.rows = []

    def write(self, batch):
        self.rows.extend(batch)


class UpsertSink:
    """正确做法:以业务键为准的 upsert,天然幂等"""

    def __init__(self):
        self.rows = {}

    def write(self, batch):
        for row in batch:
            key = row["order_id"]
            old = self.rows.get(key)
            # 业务规则:同键取更新时间更大的那条
            if old is None or row["updated_at"] > old["updated_at"]:
                self.rows[key] = row

    def snapshot(self):
        return {k: (v["amount"], v["updated_at"]) for k, v in sorted(self.rows.items())}


BATCH = [
    {"order_id": "o1", "amount": 100, "updated_at": "2025-06-01T10:00:00"},
    {"order_id": "o2", "amount": 200, "updated_at": "2025-06-01T10:05:00"},
]
UPDATE = [{"order_id": "o1", "amount": 150, "updated_at": "2025-06-01T11:00:00"}]


def state_hash(snap):
    import hashlib
    return hashlib.md5(repr(snap).encode()).hexdigest()


if __name__ == "__main__":
    sink = UpsertSink()
    h1 = state_hash(sink.snapshot())
    sink.write(BATCH)
    sink.write(UPDATE)
    good_once = state_hash(sink.snapshot())
    sink.write(BATCH)   # 故意重放旧批次
    good_twice = state_hash(sink.snapshot())
    print("upsert: 首次写入哈希 =", good_once, " 重放后哈希 =", good_twice,
          " 幂等:", good_once == good_twice)

    bad = AppendSink()
    bad.write(BATCH)
    bad.write(UPDATE)
    bad.write(BATCH)    # 重放导致重复行
    print("append: 行数 =", len(bad.rows), "-> 重放产生重复,这就是要避免的写法")
