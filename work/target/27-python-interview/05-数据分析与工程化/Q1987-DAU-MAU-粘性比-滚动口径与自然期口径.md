---
title: [Q1987] DAU/MAU 粘性比:滚动口径与自然期口径
date: 2026-11-17
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q1987 · DAU/MAU 粘性比:滚动口径与自然期口径

> 难度:★★☆ | 标签:活跃指标, 指标口径

**问**:DAU/MAU 这个粘性比怎么算才算对?为什么它经常"莫名其妙"跌一半?

**答**:粘性比等于 DAU 除以 MAU,衡量"月活里有多少天天来"。工程上最容易错的是 MAU 口径:自然月 MAU 每月一号跳变,滚动 30 天 MAU 逐日重算才平滑,两个口径在同一天能差出不少,报表必须写明用的哪个,实测用 5 天窗口演示了滚动口径的逐日计算。粘性比经常莫名下跌,最常见原因是拉新做大分母:实测随新用户涌入,粘性比从 0.8 掉到 0.44,产品并没有变糟。所以粘性比看趋势和结构性变化,不看绝对值;跨产品比较要同品类同口径,电商和社交没有可比性。行业经验区间只做参考,自家基线自己建。

```python
# file: code/05_数据分析与工程化/q1987_stickiness.py
"""DAU/MAU 粘性比:滚动窗口口径与自然期口径的差异"""

ACTIVE = {
    1: {"u1", "u2", "u3", "u4"},
    2: {"u1", "u2", "u5"},
    3: {"u1", "u3", "u6", "u7", "u8"},
    4: {"u1", "u2", "u3"},
    5: {"u1", "u4", "u9"},
    6: {"u1", "u10", "u11", "u12"},
    7: {"u1", "u2", "u3", "u13"},
}
WINDOW = 5  # 演示用 5 天窗口,生产 MAU 用滚动 30 天


def rolling_mau(active, day, window):
    s = set()
    for d in range(day - window + 1, day + 1):
        s |= active.get(d, set())
    return s


if __name__ == "__main__":
    for day in sorted(ACTIVE):
        dau = len(ACTIVE[day])
        mau = rolling_mau(ACTIVE, day, WINDOW)
        print(f"第{day}天 DAU={dau:>2}  滚动{WINDOW}日 MAU={len(mau):>2}  粘性比 {dau / len(mau):.2f}")
    last = max(ACTIVE)
    all_users = set().union(*ACTIVE.values())
    print(f"自然期口径:整期去重 {len(all_users)} 人,末日粘性比 {len(ACTIVE[last]) / len(all_users):.2f}")
    print("要点:MAU 要逐日滚动重算而不是自然月一次;粘性比看趋势不看绝对值,跌一半常见于拉新带来的分母膨胀")
```

**追问**:
- 追问 1:wDAU/MAU 是什么?—— 周活跃比月活,衡量周节奏用户的占比,与日粘性比搭配看活跃频次的分层。
- 追问 2:滚动 MAU 算起来贵怎么办?—— 用 BitMap 或 HLL 存每日活跃集,滚动并集在位图上做,成本与窗口天数线性。
