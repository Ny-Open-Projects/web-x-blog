"""Q2597 基于比较交换的分布式互斥:谁能改锁由 CAS 说了算。

分布式锁的本质是一条原子 CAS 语义:加锁 cas(空, 自己),释放
cas(自己, 空);释放带着自己的旧值比对,冒名者对不上旧值必然
失败——过期锁被别人接管后,旧主的迟到释放也伤不到新主。
"""


class Store:
    def __init__(self):
        self.kv = {}

    def cas(self, key, expect, new):
        """模拟原子的 compare-and-swap:当前值等于 expect 才写入。"""
        if self.kv.get(key) == expect:
            self.kv[key] = new
            return True
        return False


def acquire(store, owner, key="lock"):
    return owner + "#1" if store.cas(key, None, owner + "#1") else None


def release(store, owner, key="lock"):
    return store.cas(key, owner + "#1", None)


def main():
    s = Store()
    t1 = acquire(s, "A")
    assert t1 == "A#1" and s.kv["lock"] == "A#1"
    assert acquire(s, "B") is None        # B 抢不到
    assert release(s, "B") is False       # B 冒名释放被 CAS 拒绝
    assert s.kv["lock"] == "A#1", s.kv
    assert release(s, "A") is True
    assert s.kv["lock"] is None
    t2 = acquire(s, "B")
    assert t2 == "B#1" and release(s, "B") is True
    print("A 持锁,B 抢锁与冒名释放均失败")
    print("A 释放后 B 正常获取并释放:", t2)


if __name__ == "__main__":
    main()
