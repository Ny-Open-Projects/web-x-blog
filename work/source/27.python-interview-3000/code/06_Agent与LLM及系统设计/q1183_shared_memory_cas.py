"""共享状态仓库:乐观并发 CAS + 冲突重试 + 分片锁。"""
import threading, time


class ShardedStore:
    def __init__(self, shards=4):
        self.shards = [({}, threading.Lock()) for _ in range(shards)]

    def _shard(self, key):
        return self.shards[hash(key) % len(self.shards)]

    def read(self, key):
        d, lk = self._shard(key)
        with lk:
            return d.get(key)

    def cas(self, key, value, expect_version):
        d, lk = self._shard(key)
        with lk:
            cur = d.get(key, {"value": None, "version": 0})
            if cur["version"] != expect_version:
                return False, cur["version"]
            d[key] = {"value": value, "version": expect_version + 1}
            return True, expect_version + 1


def worker(store, key, n_writes, success_counter):
    for _ in range(n_writes):
        for attempt in range(50):                  # 重试上限
            cur = store.read(key)
            v = (cur["value"] or 0) if cur else 0
            ok, _ = store.cas(key, v + 1, cur["version"] if cur else 0)
            if ok:
                success_counter[0] += 1
                break
            time.sleep(0.001 * (attempt + 1))      # 退避
        else:
            raise RuntimeError("重试耗尽")


if __name__ == "__main__":
    store = ShardedStore()
    key = "shared_counter"
    success = [0]
    threads = [threading.Thread(target=worker, args=(store, key, 50, success)) for _ in range(4)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    final = store.read(key)
    print(f"4 线程各写 50 次,成功 CAS {success[0]} 次,最终值 {final['value']}")
    assert success[0] == 200 and final["value"] == 200, "任何丢失更新都会导致计数偏小"
    print("无丢失更新:乐观并发 + 冲突退避重试收敛")
