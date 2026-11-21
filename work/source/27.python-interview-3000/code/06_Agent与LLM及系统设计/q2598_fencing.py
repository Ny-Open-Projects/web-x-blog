"""Q2598 CAS 互斥的容错:持有者崩溃后 TTL 到期可接管,fencing 挡旧主。

锁值带过期时刻,持有者崩溃不释放也能被接管;接管时 fencing 号
单调递增,资源侧守卫只认不小于签发时的最大 fencing 号,旧主
拿着过期号迟到写入会被当场拒绝。
"""


class LockStore:
    def __init__(self):
        self.holder = None
        self.expires = 0.0
        self.fencing = 0

    def cas_acquire(self, owner, now, ttl):
        if self.holder is not None and now < self.expires:
            return None
        self.fencing += 1
        self.holder = owner
        self.expires = now + ttl
        return self.fencing

    def cas_release(self, owner, now):
        if self.holder == owner and now < self.expires:
            self.holder = None
            return True
        return False


def guarded_write(current_fencing, fencing, log):
    if fencing >= current_fencing:
        log.append("write-ok:" + str(fencing))
        return True
    log.append("write-rejected-stale:" + str(fencing))
    return False


def main():
    s = LockStore()
    f1 = s.cas_acquire("A", now=0.0, ttl=5.0)
    assert f1 == 1
    assert s.cas_acquire("B", now=3.0, ttl=5.0) is None   # 未过期拿不到
    assert s.cas_release("B", now=3.0) is False           # 非持有人不能释放
    assert s.cas_release("A", now=3.0) is True
    f2 = s.cas_acquire("A", now=4.0, ttl=5.0)             # A 拿到锁后崩溃
    assert f2 == 2
    log = []
    guarded_write(f2, f2, log)                            # A 用 fencing=2 写
    f3 = s.cas_acquire("B", now=10.0, ttl=5.0)            # TTL 已过,B 接管
    assert f3 == 3
    guarded_write(f3, f2, log)                            # 旧主迟到写被拒
    guarded_write(f3, f3, log)
    assert log == ["write-ok:2", "write-rejected-stale:2", "write-ok:3"], log
    print("接管后 fencing 单调递增:", f2, "->", f3)
    print("资源侧守卫:", log[1], "← 崩溃旧主的迟到写被挡")


if __name__ == "__main__":
    main()
