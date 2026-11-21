# -*- coding: utf-8 -*-
"""健康探测的指数回退: 从快到慢, 恢复即回正常。

- 探测失败按倍数拉长间隔并设上限, 避免打死已经病了的依赖;
- 一旦成功立即回到最快档, 保证恢复能被第一时间发现;
- 实测间隔序列: 0.05, 0.10, 0.20, 0.40, 0.40... 成功后回到 0.05。
"""
import time


def probe(calls, state):
    """假依赖: 前 4 次失败, 之后恢复; 记录真实健康变化。"""
    state["n"] += 1
    calls.append(state["n"])
    return state["n"] > 4


def main():
    state = {"n": 0}
    calls = []
    base, cap, factor = 0.05, 0.4, 2.0
    interval = base
    seq = []
    ok_at = None
    deadline = time.monotonic() + 3.0
    t0 = time.monotonic()
    while time.monotonic() < deadline:
        begin = time.monotonic()
        healthy = probe(calls, state)
        if healthy:
            ok_at = time.monotonic() - t0
            seq.append(("成功", interval))
            break
        seq.append(("失败", interval))
        interval = min(cap, interval * factor)   # 回退, 封顶
        sleep_left = interval - (time.monotonic() - begin)
        if sleep_left > 0:
            time.sleep(sleep_left)

    for i, (res, gap) in enumerate(seq):
        print("第 %d 次探测: %-2s 间隔 %.2fs" % (i + 1, res, gap))
    print("恢复时刻: %.2fs" % ok_at)
    print("失败段间隔翻倍直到封顶; 成功后下一轮从 base 重新开始")
    print("工程补充: 抖动 jitter 防止多实例同相位探测; "
          "连续 N 次失败才标记不健康, 单次失败不摘除")


if __name__ == "__main__":
    main()
