# -*- coding: utf-8 -*-
"""等待图死锁检测: 谁在等谁, 成环即死锁。

- 预防靠定序, 检测靠观察: 记录 lock->owner 与 thread->waiting 边, 周期扫描找环;
- 找到环后选一个牺牲者, 用 abort 事件劝退它, 打破循环等待;
- 幸存者随后正常拿到锁, 系统继续推进, 这就是数据库死锁选择的思路。
"""
import threading
import time


class NamedLock:
    """带名字的锁包装, 便于把锁放进等待图里说话。"""

    def __init__(self, name):
        self.name = name
        self.lock = threading.Lock()

    def acquire(self, timeout=None):
        return self.lock.acquire(timeout=timeout) if timeout is not None \
            else self.lock.acquire()

    def release(self):
        self.lock.release()


class Detector:
    """登记线程等待关系的注册表 + 周期检测器。"""

    def __init__(self):
        self.mtx = threading.Lock()
        self.owner = {}        # lock 名 -> thread 名
        self.waiting = {}      # thread 名 -> lock 名
        self.abort = {}        # thread 名 -> Event
        self.victim = None

    def register_thread(self, name):
        self.abort[name] = threading.Event()

    def got(self, tname, lname):
        with self.mtx:
            self.owner[lname] = tname
            self.waiting.pop(tname, None)

    def want(self, tname, lname):
        with self.mtx:
            self.waiting[tname] = lname

    def gave_up(self, tname):
        with self.mtx:
            self.waiting.pop(tname, None)

    def find_cycle(self):
        with self.mtx:
            for start in self.waiting:
                seen, cur = [], start
                while cur in self.waiting:
                    if cur in seen:
                        return seen[seen.index(cur):]
                    seen.append(cur)
                    cur = self.owner.get(self.waiting[cur])
            return None

    def scan(self, rounds=40):
        for _ in range(rounds):
            cycle = self.find_cycle()
            if cycle:
                self.victim = max(cycle)          # 选名字最大者为牺牲者
                self.abort[self.victim].set()
                print("检测到死锁环:", " -> ".join(cycle))
                print("选定牺牲者:", self.victim, "劝退它")
                return True
            time.sleep(0.05)
        return False


def worker(reg, name, first, second, done):
    """先拿 first 再试图拿 second, 被 abort 就放手退出。"""
    if not first.acquire(timeout=0.1):
        return
    reg.got(name, first.name)
    time.sleep(0.15)                              # 制造交叉窗口
    abort_evt = reg.abort[name]
    while True:
        reg.want(name, second.name)
        if second.acquire(timeout=0.05):
            reg.got(name, second.name)
            done.append(name + " 完成")
            second.release()
            first.release()
            return
        reg.gave_up(name)
        if abort_evt.is_set():
            print(name, "被选为牺牲者, 释放", first.name, "退出")
            first.release()
            return


def main():
    reg = Detector()
    lock_a, lock_b = NamedLock("A"), NamedLock("B")
    done = []
    reg.register_thread("T1"); reg.register_thread("T2")

    t1 = threading.Thread(target=worker, args=(reg, "T1", lock_a, lock_b, done))
    t2 = threading.Thread(target=worker, args=(reg, "T2", lock_b, lock_a, done))
    t1.start(); t2.start()
    found = reg.scan()
    t1.join(timeout=3); t2.join(timeout=3)
    print("推进结果:", done)
    assert found, "必须检测到一次死锁环"
    assert done, "牺牲者退出后, 幸存者必须能完成"


if __name__ == "__main__":
    main()
