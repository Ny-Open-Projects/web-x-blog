import threading
import time


class LeaseManager:
    def __init__(self, ttl: float) -> None:
        self._ttl = ttl
        self._lock = threading.Lock()
        self._leases = {}   # task -> (owner, expire_at)

    def acquire(self, task: str, owner: str) -> bool:
        now = time.monotonic()
        with self._lock:
            cur = self._leases.get(task)
            if cur is not None and cur[1] > now:
                return False            # 仍被有效持有
            self._leases[task] = (owner, now + self._ttl)
            return True

    def renew(self, task: str, owner: str) -> bool:
        now = time.monotonic()
        with self._lock:
            cur = self._leases.get(task)
            if cur is None or cur[0] != owner or cur[1] <= now:
                return False            # 不是你的或已过期, 拒绝续期
            self._leases[task] = (owner, now + self._ttl)
            return True

    def release(self, task: str, owner: str) -> None:
        with self._lock:
            cur = self._leases.get(task)
            if cur and cur[0] == owner:
                del self._leases[task]


def main() -> None:
    mgr = LeaseManager(ttl=0.4)
    timeline = []

    # worker A: 正常续约两轮后假死
    assert mgr.acquire("job", "A")
    timeline.append("A 拿到租约")
    for _ in range(2):
        time.sleep(0.1)
        assert mgr.renew("job", "A")
    timeline.append("A 续约 2 次成功, 随后假死")

    assert not mgr.renew("job", "bogus"), "其他身份不能续 A 的租约"
    assert not mgr.acquire("job", "B"), "租约有效期内 B 不能抢"
    timeline.append("B 尝试接管被拒")

    time.sleep(0.45)                    # A 不再续约, 租约过期
    assert mgr.acquire("job", "B"), "过期后 B 应能接管"
    timeline.append("租约过期, B 合法接管")

    assert mgr.renew("job", "B")
    mgr.release("job", "B")
    assert mgr.acquire("job", "C")
    timeline.append("B 主动释放, C 立即接手")

    for line in timeline:
        print(line)
    print("租约生命周期验证通过")


if __name__ == "__main__":
    main()
