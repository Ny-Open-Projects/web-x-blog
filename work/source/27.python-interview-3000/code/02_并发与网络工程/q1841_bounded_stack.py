# -*- coding: utf-8 -*-
"""条件变量实现有界阻塞栈: 满/空两向等待。

- 一个 Condition 承担 not_full 与 not_empty 两种谓词, notify_all 后由等待方自查;
- push 在栈满时等待, pop 在栈空时等待, 都带超时避免永久卡死;
- 统计等待次数, 证明背压真实发生过。
"""
import threading
import time


class BoundedStack:
    def __init__(self, cap):
        assert cap > 0
        self._cap = cap
        self._items = []
        self._cond = threading.Condition()
        self.stats = {"push_wait": 0, "pop_wait": 0}

    def push(self, x, timeout=3.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while len(self._items) >= self._cap:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("push 超时: 栈一直满")
                self.stats["push_wait"] += 1
                self._cond.wait(remain)
            self._items.append(x)
            self._cond.notify_all()

    def pop(self, timeout=3.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while not self._items:
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("pop 超时: 栈一直空")
                self.stats["pop_wait"] += 1
                self._cond.wait(remain)
            v = self._items.pop()
            self._cond.notify_all()
            return v

    def __len__(self):
        with self._cond:
            return len(self._items)


def main():
    st = BoundedStack(2)
    got = []
    got_lock = threading.Lock()

    def consumer(n):
        for _ in range(n):
            v = st.pop(timeout=3.0)
            with got_lock:
                got.append(v)

    def producer():
        for i in (3, 4):
            st.push(i, timeout=3.0)       # 栈已满, push 必然等待
            time.sleep(0.05)              # 慢慢放, 制造空栈等待

    st.push(1)
    st.push(2)                            # 预先填满, 制造确定性满栈
    p = threading.Thread(target=producer)
    p.start()
    time.sleep(0.1)                       # 确保 push 已经卡在满栈等待上
    cs = [threading.Thread(target=consumer, args=(2,)) for _ in range(2)]
    for t in cs:
        t.start()
    p.join()
    for t in cs:
        t.join()

    print("消费到的元素:", sorted(got))
    print("等待统计:", st.stats)
    assert sorted(got) == [1, 2, 3, 4], "四个元素都应被消费"
    assert st.stats["push_wait"] >= 1, "预填满栈, 第三个 push 必须等待"
    assert st.stats["pop_wait"] >= 1, "消费者追平后应在空栈上等待"
    print("结论: 单 Condition + 谓词循环, 就能实现满/空双向等待的有界栈")


if __name__ == "__main__":
    main()
