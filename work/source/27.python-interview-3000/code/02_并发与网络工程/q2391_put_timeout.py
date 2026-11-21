# -*- coding: utf-8 -*-
"""put 的超时折中: 阻塞、立即失败、限时等待三档实测。

- put() 无限等, 队满时生产者悬停, 上游不可控时是事故源;
- put_nowait() 立即抛 Full, 快速失败但一场抖动就丢数据;
- put(item, timeout=t) 给一个呼吸窗口, 短抖动扛过去, 真拥塞才拒绝。
"""
import queue
import threading
import time

q = queue.Queue(maxsize=2)


def slow_consumer(n, item_s):
    for _ in range(n):
        time.sleep(item_s)
        try:
            q.get_nowait()
        except queue.Empty:
            pass


def attempt_put(item, timeout):
    t0 = time.monotonic()
    try:
        if timeout is None:
            q.put(item)                      # 阻塞版, 本例不会真悬住
        elif timeout == 0:
            q.put_nowait(item)
        else:
            q.put(item, timeout=timeout)     # 限时版
        return "ok", time.monotonic() - t0
    except queue.Full:
        return "Full", time.monotonic() - t0


def main():
    # 先灌满 2 格
    q.put("a"); q.put("b")

    r1 = attempt_put("x", 0)
    print("put_nowait  -> %s, 耗时 %.3fs" % r1)
    r2 = attempt_put("y", 0.15)
    print("put 0.15s   -> %s, 耗时 %.3fs" % r2)
    assert r1[0] == "Full" and r1[1] < 0.05, "立即失败必须马上返回"
    assert r2[0] == "Full" and 0.14 < r2[1] < 0.4, "限时等待应等满窗口再失败"

    # 消费者 0.2s 后取走一件, 限时 put 应在窗口内成功
    threading.Thread(target=slow_consumer, args=(1, 0.2), daemon=True).start()
    r3 = attempt_put("z", 0.5)
    print("消费者 0.2s 后腾位, put 0.5s -> %s, 耗时 %.3fs" % r3)
    assert r3[0] == "ok", "短抖动应被限时等待扛过去"
    print("结论: timeout 版兼顾两头, 是默认推荐档")


if __name__ == "__main__":
    main()
