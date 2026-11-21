# -*- coding: utf-8 -*-
"""优先级反转概念演示: 低持锁、高等待、中间者插队。

- 高优先级任务要拿低优先级持有的锁时, 不持锁的中优先级任务照常运行;
- 高优先级实际被"低锁 + 中间算力"双重拖延, 这就是优先级反转;
- CPython 没有用户态优先级 API, 这里用时间线展示反转窗口的形状。
"""
import threading
import time

lock = threading.Lock()
timeline = []


def note(tag):
    timeline.append((tag, round(time.monotonic() - T0, 3)))


def low():
    note("low 拿锁")
    with lock:
        note("low 进入临界区 干 0.5s")
        end = time.monotonic() + 0.5
        while time.monotonic() < end:
            pass                       # 低优先级长临界区
    note("low 放锁")


def mid():
    end = time.monotonic() + 0.3
    n = 0
    while time.monotonic() < end:      # 中优先级不需要锁, 却一直有算力
        n += 1
    note("mid 完成无锁工作")


def high():
    note("high 请求锁")
    got = lock.acquire(timeout=2.0)
    if got:
        note("high 终于拿到锁")
        lock.release()


def main():
    global T0
    tl = threading.Thread(target=low, name="low")
    tl.start()
    time.sleep(0.05)
    tm = threading.Thread(target=mid, name="mid")
    tm.start()
    time.sleep(0.01)
    th = threading.Thread(target=high, name="high")
    th.start()
    tl.join()
    tm.join()
    th.join()
    for tag, ts in timeline:
        print("%6.3f  %s" % (ts, tag))
    req = [t for tag, t in timeline if "请求锁" in tag][0]
    got = [t for tag, t in timeline if "终于拿到" in tag][0]
    mid_done = [t for tag, t in timeline if tag.startswith("mid 完成")][0]
    print("反转证据: high 等 %.3fs 才拿到锁, 期间 mid 已于 %.3f 完成全部工作" %
          (got - req, mid_done))
    print("高优先级被'低持锁 + 中间算力'双重拖延, 这就是反转窗口")


if __name__ == "__main__":
    T0 = time.monotonic()
    main()
