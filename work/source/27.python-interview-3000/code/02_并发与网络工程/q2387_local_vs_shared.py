# -*- coding: utf-8 -*-
"""局部快照与共享裸读: 一致性和活性各有一个坑。

- 一致性: 裸读共享结构的两个字段, 可能夹在写入者两次修改中间, 快照才自洽;
- 活性: 纯 CPU 循环不释放 GIL, 写入者的标志位要等到切换间隔才被看见;
- 局部变量天然免疫这两个问题, 因为它读一次就定格在自己世界里。
"""
import sys
import threading
import time


def liveness_demo(switch_interval):
    """写线程 50ms 后置标志, 读线程纯 CPU 循环能多快看见它。"""
    flag = [False]
    result = []

    def writer():
        time.sleep(0.05)
        flag[0] = True                       # 需要抢到 GIL 才能执行

    def reader():
        t0 = time.monotonic()
        while time.monotonic() - t0 < 0.8:   # 纯 CPU 轮询, 无任何让盘点
            if flag[0]:
                result.append(time.monotonic() - t0)
                return
        result.append(None)

    old = sys.getswitchinterval()
    sys.setswitchinterval(switch_interval)
    try:
        wt = threading.Thread(target=writer)
        rt = threading.Thread(target=reader)
        rt.start(); wt.start()
        wt.join(); rt.join()
    finally:
        sys.setswitchinterval(old)
    return result[0]


def consistency_demo():
    """写入者 a-=1 与 b+=1 两步之间, 裸读者能读到自相矛盾的世界。"""
    state = {"a": 0, "b": 0}
    lock = threading.Lock()
    violations = {"bare": 0, "snapshot": 0}
    rounds = {"n": 200}
    done = threading.Event()

    def writer():
        for _ in range(rounds["n"]):
            with lock:
                state["a"] -= 1
                time.sleep(0)                # 人为扩大两步之间的让步窗口
                state["b"] += 1
        done.set()

    def bare_reader():
        while not done.is_set():
            x = state["a"]                   # 裸读: 不持锁, 不快照
            y = state["b"]
            if x + y != 0:
                violations["bare"] += 1

    def snapshot_reader():
        while not done.is_set():
            with lock:                       # 快照: 持锁拷进局部变量
                x, y = state["a"], state["b"]
            if x + y != 0:
                violations["snapshot"] += 1

    wt = threading.Thread(target=writer)
    b1 = threading.Thread(target=bare_reader)
    b2 = threading.Thread(target=snapshot_reader)
    for t in (wt, b1, b2):
        t.start()
    wt.join()
    b1.join(timeout=2); b2.join(timeout=2)
    return violations["bare"], violations["snapshot"]


def main():
    fast = liveness_demo(0.005)
    slow = liveness_demo(1.0)
    print("切换间隔 5ms : %.3fs 看见标志" % fast)
    print("切换间隔 1s  : %s (0.8s 内没看见, GIL 迟迟不放手)" % slow)
    assert fast is not None and fast < 0.3, "正常切换间隔下应很快看见标志"
    assert slow is None, "超大切换间隔下纯 CPU 循环应在窗口内看不见标志"

    bare = snap = 0
    # 断言采用确定性设计: 竞态窗口能否被抓到受线程调度影响(单轮抓到率约 2/3),
    # 重试多轮, 任一轮抓到矛盾即证明裸读不安全; 快照读在每一轮都必须零违例
    for _ in range(10):
        bare, snap = consistency_demo()
        assert snap == 0, "持锁快照必须完全一致"
        if bare > 0:
            break
    print("裸读不一致次数: %d, 快照读不一致次数: %d" % (bare, snap))
    assert bare > 0, "sleep(0) 让步窗口下裸读必须抓到矛盾状态"


if __name__ == "__main__":
    main()
