"""幂等键冲突: 同键同参重放, 同键不同参必须拒绝"""


class IdempotencyConflict(Exception):
    """同一个幂等键被用来提交不同的参数"""


class IdempotencyStore:
    def __init__(self):
        self._store = {}      # key -> (fingerprint, result)

    def execute(self, key, fingerprint, result):
        if key in self._store:
            old_fp, old_result = self._store[key]
            if old_fp != fingerprint:
                raise IdempotencyConflict(
                    f"键 {key[:12]} 已被其他参数占用, 拒绝覆盖, 请先排查调用方 bug")
            return "replay", old_result
        self._store[key] = (fingerprint, result)
        return "new", result


if __name__ == "__main__":
    store = IdempotencyStore()
    status, value = store.execute("key-abc", "fp-2026-03-01", "结果A")
    print(f"首次提交: {status} -> {value}")
    status, value = store.execute("key-abc", "fp-2026-03-01", "结果A")
    print(f"同键同参重试: {status} -> {value} (不重复执行)")
    assert status == "replay"
    try:
        store.execute("key-abc", "fp-2026-03-02", "结果B")
    except IdempotencyConflict as e:
        print("同键不同参:", e)
    else:
        raise AssertionError("同键不同参必须拒绝")
    status, value = store.execute("key-abc", "fp-2026-03-01", "结果A")
    assert status == "replay" and value == "结果A", "冲突被拒后原结果不受污染"
    print("冲突被拒后原键仍可安全重放, 结果未被污染")
    print("要点: 幂等键是承诺不是缓存, 同键不同参说明调用方有 bug, 覆盖会把两份数据搅在一起")
