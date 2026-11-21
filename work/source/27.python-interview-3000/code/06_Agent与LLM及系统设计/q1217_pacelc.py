"""PACELC 演示:同步复制低差异高延迟 vs 异步复制低延迟有旧读 + 会话粘住方案。"""
import time


class ReplicatedStore:
    def __init__(self, mode):
        self.mode = mode                # "sync" or "async"
        self.primary, self.replica = {}, {}
        self.replica_lag = 0.01         # 模拟复制延迟
        self.pending = []

    def write(self, k, v):
        t0 = time.monotonic()
        self.primary[k] = v
        if self.mode == "sync":
            self.replica[k] = v         # 写路径等待副本
        else:
            self.pending.append((k, v))  # 异步:先记账后复制
        return (time.monotonic() - t0, 0.01 if self.mode == "sync" else 0.0)

    def replicate_tick(self):
        while self.pending:
            k, v = self.pending.pop(0)
            self.replica[k] = v

    def read(self, k, from_replica=True):
        src = self.replica if from_replica else self.primary
        return src.get(k)


if __name__ == "__main__":
    sync = ReplicatedStore("sync")
    lat, _ = sync.write("price", 99)
    print(f"sync 写延迟 +{lat:.3f}s(等待副本),副本立即可读:", sync.read("price"))
    assert sync.read("price") == 99, "强一致读必为新值"

    async_s = ReplicatedStore("async")
    lat2, _ = async_s.write("price", 99)
    stale = async_s.read("price")
    print(f"async 写延迟 +{lat2:.3f}s(不等副本),副本读 = {stale}(旧值)")
    assert stale is None, "复制未完成,读到旧值"
    async_s.replicate_tick()
    assert async_s.read("price") == 99
    print("复制完成后收敛;写后读用户应粘住主副本规避旧读")
    # 会话粘住:同一会话读主
    assert async_s.read("price", from_replica=False) == 99
    print("会话粘主策略生效:自己的写自己立即可见")
