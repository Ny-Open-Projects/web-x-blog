"""分级降级与滞回: 防抖的恢复节奏。

降级不是开关, 是阶梯: L0 正常 -> L1 关推荐 -> L2 关搜索 -> L3 只读兜底。
三条防抖规则:
- 升级要连续恶化: 错误率连续超阈值才升级, 且级别越高需要的证据越多
  (2/4/6 连恶化), 越深越谨慎;
- 改善中的采样不累计恶化: 错误率在下降说明正在自愈, 别趁机升级;
- 恢复要比升级难: 连续 5 个周期健康才降一级, 防止在阈值附近来回抖动。
"""
from collections import deque


class DegradationManager:
    LEVELS = ["L0 全功能", "L1 关推荐", "L2 关搜索", "L3 只读兜底"]
    BAD_RATE = 0.5          # 滑动窗口错误率 >= 50% 才算恶化
    BAD_STREAK = 2          # L0->L1 需要连续 2 个恶化周期
    GOOD_RATE = 0.1         # 错误率 < 10% 才算健康
    GOOD_STREAK = 5         # 连续 5 个健康周期 -> 降一级(恢复更难)

    def __init__(self):
        self.level = 0
        self.window = deque(maxlen=10)
        self.prev_err = None
        self.bad = 0
        self.good = 0
        self.transitions = []

    def record(self, ok):
        self.window.append(ok)
        return self._evaluate()

    def _needed_bad(self):
        # 级别越高, 升级要的证据越多: 2 / 4 / 6 连恶化
        return self.BAD_STREAK * (self.level + 1)

    def _evaluate(self):
        if not self.window:
            return self.level
        err = 1.0 - 1.0 * self.window.count(True) / len(self.window)
        improving = self.prev_err is not None and err < self.prev_err
        self.prev_err = err
        if err >= self.BAD_RATE and not improving:
            self.bad += 1
            self.good = 0
            if self.bad >= self._needed_bad() and self.level < 3:
                self.level += 1
                self.bad = 0
                self.transitions.append(("upgrade", self.level))
        elif improving:
            self.bad = 0                 # 正在自愈, 别趁机升级
        elif err < self.GOOD_RATE:
            self.good += 1
            if self.good >= self.GOOD_STREAK and self.level > 0:
                self.level -= 1
                self.good = 0
                self.transitions.append(("downgrade", self.level))
        # 中间地带(10% <= err < 50% 且无趋势): 保持现状, 这就是滞回
        return self.level


def feed(mgr, samples):
    level = mgr.level
    for ok in samples:
        level = mgr.record(ok)
    return level


def main():
    mgr = DegradationManager()
    lvl = feed(mgr, [True] * 10)
    print("阶段 1: 全健康 ->", mgr.LEVELS[lvl])
    assert mgr.level == 0

    lvl = feed(mgr, [False] * 10)
    print("阶段 2: 持续恶化 ->", mgr.LEVELS[lvl], "| 轨迹:", mgr.transitions)
    assert mgr.level == 2, "恶化证据 2/4 连应升到 L2"

    lvl = feed(mgr, [True] * 10)
    print("阶段 3: 立刻全好 ->", mgr.LEVELS[lvl], "(错误率一路在降, 不升级也不降级)")
    assert mgr.level == 2, "恢复证据不足且趋势向好时, 级别应保持"

    lvl = feed(mgr, [True] * 10)
    print("阶段 4: 持续健康 ->", mgr.LEVELS[lvl], "| 轨迹:", mgr.transitions)
    assert mgr.level == 0, "健康周期够多后应逐级恢复到 L0"
    assert mgr.transitions[-2] == ("downgrade", 1) and mgr.transitions[-1] == ("downgrade", 0), \
        "恢复必须逐级降, 不允许跳级"

    print("结论: 升级要证据且越深越难, 恢复要耐心——滞回是防抖的全部秘密")


if __name__ == "__main__":
    main()
