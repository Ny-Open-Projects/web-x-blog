# -*- coding: utf-8 -*-
"""有界阻塞栈的关闭与排空语义: close 后 push 拒绝, pop 排完存量返回 None。

- close() 置位后要 notify_all, 把还挂在空栈上的 pop 全部唤醒;
- pop 的谓词是 "空且未关闭才等", 空且已关闭直接返回 None, 这是优雅下线的核心;
- push 一律拒绝, 语义是 "关门, 不是清仓": 存量仍然可取。
"""
import threading
import time


class ClosableStack:
    def __init__(self, cap):
        self._cap = cap
        self._items = []
        self._closed = False
        self._cond = threading.Condition()

    def push(self, x, timeout=3.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while True:
                if self._closed:
                    raise RuntimeError("栈已关闭, 不再接受写入")
                if len(self._items) < self._cap:
                    self._items.append(x)
                    self._cond.notify_all()
                    return
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("push 超时: 栈一直满")
                self._cond.wait(remain)

    def pop(self, timeout=3.0):
        with self._cond:
            deadline = time.monotonic() + timeout
            while True:
                if self._items:
                    v = self._items.pop()
                    self._cond.notify_all()
                    return v
                if self._closed:
                    return None             # 关门且清空: 优雅退出信号
                remain = deadline - time.monotonic()
                if remain <= 0:
                    raise TimeoutError("pop 超时: 栈一直空")
                self._cond.wait(remain)

    def close(self):
        with self._cond:
            self._closed = True
            self._cond.notify_all()          # 唤醒所有等待中的 pop


def main():
    st = ClosableStack(2)
    got = []
    got_lock = threading.Lock()
    stop = threading.Event()

    def consumer():
        while not stop.is_set():
            v = st.pop(timeout=3.0)
            if v is None:
                break                        # 收到关门信号
            with got_lock:
                got.append(v)

    def producer():
        for i in range(1, 6):
            st.push(i, timeout=3.0)
        time.sleep(0.1)                      # 确保消费者已经饥饿等待过
        st.close()

    cs = [threading.Thread(target=consumer) for _ in range(2)]
    p = threading.Thread(target=producer)
    for t in cs:
        t.start()
    p.start()
    p.join()
    for t in cs:
        t.join(timeout=2.0)
        assert not t.is_alive(), "消费者应随关门信号退出, 不能永久卡死"

    try:
        st.push(99)
        raise AssertionError("close 后 push 应当被拒绝")
    except RuntimeError as e:
        print("close 后 push 被拒绝:", e)

    assert sorted(got) == [1, 2, 3, 4, 5], "存量 5 个元素必须全部可排空"
    assert st.pop(timeout=0.5) is None, "关门且空栈的 pop 返回 None"
    print("排空结果:", sorted(got))
    print("结论: close 是关门不清仓, pop 靠 '空且已关' 谓词优雅退出")


if __name__ == "__main__":
    main()
