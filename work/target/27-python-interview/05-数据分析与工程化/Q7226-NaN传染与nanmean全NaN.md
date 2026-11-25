---
title: "[Q7226] 一个 NaN 让整列均值变 NaN：nanmean 也不是万能"
date: 2026-11-24
categories: [Python数据分析工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7226 · 一个 NaN 让整列均值变 NaN：nanmean 也不是万能

难度：P6 ｜ 标签：NumPy、NaN 传播、nanmean、统计口径

基线：Python 3.12；NumPy 2.x `mean`/`nanmean`/`nansum` 的警告语义；标准库 `math` + `warnings` 复现。

**问**：`np.mean([1.0, 2.0, np.nan])` 返回 nan，换 `np.nanmean` 得到 1.5。可某天整列都是 NaN，`np.nanmean` 返回 nan 并打了 `RuntimeWarning: Mean of empty slice`，而告警被 `-W ignore` 吞了，报表直接出现空值。NaN 到底该怎么处理？

**答**：
- **结论**：NumPy 的归约默认**传播 NaN**（`mean`/`sum`/`std` 都是），因为 NaN 表示"未知"，未知参与运算结果仍是未知；`nanmean`/`nansum` 跳过 NaN，但**全 NaN 时有效元素个数为 0**：`nanmean` 返回 nan 并触发 `RuntimeWarning: Mean of empty slice`，`nansum` 返回 `0.0`（更危险）。pandas 的 `mean()` 默认 `skipna=True`，全 NaN 返回 nan 且不报警。
- **取舍**：跳过 NaN 让局部缺失不影响整体，但**分母变小**（1.5 是 2 个样本的均值，不是 3 个），在"缺失本身有信息"的场景（未评分用户、未激活设备）会高估。`nansum` 返回 0 会把"无数据"伪装成"零"。缺失率超阈值时应该**拒绝出数**而不是静默跳过。
- **实战**：① 先算 `missing_rate`，超阈值直接 raise 或打标；② `warnings.catch_warnings` + `simplefilter("error")` 把警告升级为异常；③ 需要明确分母时写 `nansum(x) / count_valid(x)` 并处理 0 分母；④ pandas 聚合用 `min_count=1`，让全 NaN 组返回 NaN 而不是 0。

```python
"""mean 传播 NaN、nanmean 跳过、nansum 返回 0 的三种坑。"""
import math
import warnings

NAN = float("nan")


def mean(xs: list[float]) -> float:
    """等价 np.mean：NaN 传染。"""
    return math.fsum(xs) / len(xs)


def nansum(xs: list[float]) -> float:
    return math.fsum(v for v in xs if not math.isnan(v))


def nanmean(xs: list[float]) -> float:
    """等价 np.nanmean：全 NaN 时警告 + 返回 nan。"""
    valid = [v for v in xs if not math.isnan(v)]
    if not valid:
        warnings.warn("Mean of empty slice", RuntimeWarning, stacklevel=2)
        return NAN
    return math.fsum(valid) / len(valid)


def guarded_mean(xs: list[float], max_missing: float = 0.3) -> float:
    """带缺失率闸门的均值：超阈值拒绝出数。"""
    missing = sum(1 for v in xs if math.isnan(v)) / len(xs)
    if missing > max_missing:
        raise ValueError(f"缺失率 {missing:.0%} 超过阈值 {max_missing:.0%}，拒绝出数")
    return nanmean(xs)


if __name__ == "__main__":
    data = [1.0, 2.0, NAN]
    print("mean    :", mean(data))
    print("nanmean :", nanmean(data), "-> 分母是 2 不是 3")
    print("nansum  :", nansum(data), "| 全 NaN 时:", nansum([NAN, NAN]), "-> 伪装成 0")

    with warnings.catch_warnings():
        warnings.simplefilter("error")                 # 警告升级为异常
        try:
            nanmean([NAN, NAN])
        except RuntimeWarning as e:
            print("全 NaN 升级为异常:", e)

    # 缺失率闸门
    print("2/3 有效:", guarded_mean([1.0, 2.0, NAN], max_missing=0.5))
    try:
        guarded_mean([NAN, NAN, NAN])
    except ValueError as e:
        print("闸门:", e)

    # 显式分母：和自己算的对得上
    valid = [v for v in data if not math.isnan(v)]
    print("显式分子/分母:", nansum(data), "/", len(valid), "=", nansum(data) / len(valid))

    print("结论：跳过 NaN 会改分母；全 NaN 要显式拦截，别让 0 或 nan 流到报表")
```

**追问一**：为什么 `np.nansum([nan, nan])` 返回 0.0 比返回 nan 更危险？
→ 解析：0 是合法值，下游求均值、求和、同比时无法区分"和为 0"与"全缺失"，会算出 0 均值、0 增长，且不触发任何告警。统计口径上"无数据"必须显式传播为缺失，让报表显示"暂无数据"。

**追问二**：pandas 的 `mean(skipna=False)` 和 numpy 的 `nanmean` 有什么区别？
→ 解析：`skipna=False` 遇到 NaN 直接返回 nan（与 `np.mean` 一致），`skipna=True`（默认）跳过；`nanmean` 是"永远跳过"，没有开关。要精确控制就用 pandas 的 `skipna`，或在 numpy 侧自己算分子分母。
