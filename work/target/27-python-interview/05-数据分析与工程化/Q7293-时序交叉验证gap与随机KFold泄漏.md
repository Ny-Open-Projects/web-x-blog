---
title: "[Q7293] 时序交叉验证的 gap：随机 KFold 为什么把未来泄漏进训练集"
date: 2026-11-25
categories: [Python工程化]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7293 · 时序交叉验证的 gap：随机 KFold 为什么把未来泄漏进训练集

难度：P7 ｜ 标签：时序交叉验证、TimeSeriesSplit、gap、数据泄漏、sklearn

基线：库知识库外知识卡，用纯 Python 生成时间索引与切分，模拟随机 KFold 与 TimeSeriesSplit 的泄漏/间隔差异，不依赖 sklearn。

**问**：销量预测模型离线 CV 的 R² 是 0.93，上线后 MAPE 38%，落差大得不像过拟合。排查发现训练用了 `KFold(shuffle=True)`，而且特征里算过"未来 7 天滚动均值"。改成 `TimeSeriesSplit` 后 CV 掉到 0.71，但线上对上了。随机切分到底泄漏了什么？`TimeSeriesSplit` 的 `gap` 该留几期？留了 gap 为什么还会泄漏？

**答**：

- **结论**：随机 KFold 假设样本**独立同分布**，但时序样本不独立：测试集的"未来"会被切进训练集，模型学到的是"用未来解释过去"。更隐蔽的是**特征窗口泄漏**：即使切分按时间，如果特征在 `t` 时刻用了 `t+1...t+7` 的数据（滚动均值、`shift(-1)`、全局标准化），训练仍然偷看未来。`TimeSeriesSplit` 保证"训练集时间 < 测试集时间"，`gap` 在两者之间再挖掉一段，防止**标签窗口/特征窗口跨过边界**（比如标签是未来 7 天销量，训练集最后 7 天的标签其实落进了测试期）。
- **取舍**：① 不做 gap：训练/测试紧邻，边界样本的标签窗口与测试期重叠，CV 偏乐观；② `gap=标签 horizon`（如 7 天）：边界干净，但损失一部分训练样本，且要求数据按自然时间连续；③ `gap` 太大：训练集变短、分布漂移，CV 偏悲观；④ 多序列（多 SKU）场景要**按实体分组 + 按时间切分**，不能只按行随机，否则同一 SKU 的未来仍会泄漏到别的 SKU 的训练折。
- **实战**：① 任何时序任务禁用 `KFold(shuffle=True)`，用 `TimeSeriesSplit(n_splits, gap=horizon)`；② 特征工程先做"可用时点"审计：每个特征标注"最早可用时间"，断言 `feature_time <= label_time`；③ 用 `Pipeline` 把标准化/编码放进折内 `fit`，避免全量 `fit` 的统计量泄漏；④ 线上回测用"滚动原点"（walk-forward）模拟真实训练/预测节奏，而不是一次切分。

下面量化三种切分的泄漏：随机 KFold、无 gap 的 TimeSeriesSplit、带 gap 的 TimeSeriesSplit。

```python
# 时序切分: 随机 KFold 把未来折进训练; gap 挖掉标签窗口跨界的样本
import random


def random_kfold(n, k=4, seed=0):
    idx = list(range(n))
    random.Random(seed).shuffle(idx)
    fold = n // k
    out = []
    for i in range(k):
        test = idx[i * fold:(i + 1) * fold]
        train = idx[:i * fold] + idx[(i + 1) * fold:]
        out.append((train, test))
    return out


def time_split(n, k=4, gap=0):
    fold = n // (k + 1)
    out = []
    for i in range(k):
        test_start = fold * (i + 1)
        test_end = min(test_start + fold, n)
        train_end = max(0, test_start - gap)
        out.append((list(range(train_end)), list(range(test_start, test_end))))
    return out


def future_leaks(splits):
    return sum(1 for train, test in splits if train and max(train) > min(test))


def boundary_gap(splits):
    return min(min(test) - max(train) for train, test in splits if train and test)


n = 40
rk = random_kfold(n)
ts0 = time_split(n, gap=0)
ts7 = time_split(n, gap=7)

print(f"[1] 随机 KFold: {future_leaks(rk)}/{len(rk)} 折的训练集含未来样本")
print(f"[2] TimeSeriesSplit gap=0: 未来泄漏折数={future_leaks(ts0)}, 边界间隔={boundary_gap(ts0)}")
print(f"[3] TimeSeriesSplit gap=7: 未来泄漏折数={future_leaks(ts7)}, 边界间隔={boundary_gap(ts7)}")
assert future_leaks(rk) == 4
assert future_leaks(ts0) == 0 and boundary_gap(ts0) == 1
assert boundary_gap(ts7) == 8
print("    → 实测 随机切分 4/4 折都在偷看未来; gap=7 把边界推到 8 期")

# 标签 horizon=7 时, 无 gap 的训练集最后 7 天标签落进测试期
HORIZON = 7
train, test = ts0[-1]
overlap = [i for i in train if i + HORIZON >= min(test)]
print(f"[4] gap=0 时, 训练集有 {len(overlap)} 个样本的 {HORIZON} 天标签跨进测试期: {overlap}")
assert len(overlap) == HORIZON
print("    → 实测 gap 应 >= 标签 horizon; 否则边界样本的标签仍然泄漏")
```

**追问一**：`gap=7` 是不是就万事大吉？—— 不是。`gap` 只管"训练样本的标签窗口"不跨进测试期；如果特征用了更长的窗口（比如 30 天滚动均值），或者做了**全量标准化**，泄漏仍在。正确做法是给每个特征/标签标注"数据可用时点"，用 `feature_time + horizon <= label_time` 统一审计，而不是只调一个 `gap` 参数。

**追问二**：多 SKU 时序为什么不能简单 `TimeSeriesSplit`？—— 简单的 `TimeSeriesSplit` 按全局行号切，可能同一时间点一部分 SKU 在训练、另一部分在测试，模型学到"同期其他 SKU 的销量"这种跨实体信息；如果线上预测时这些 SKU 的数据不可得，就会高估。应按时间切 + 按实体分组，确保同一实体的同一时间段只出现在一侧。

## 背诵要点

- 时序禁用 `KFold(shuffle=True)`：未来样本进训练集，CV 虚高、上线崩；用 `TimeSeriesSplit`。
- `gap >= 标签 horizon`，否则训练集边界样本的标签窗口跨进测试期；特征窗口/全量标准化是更隐蔽的泄漏。
- 多实体时序：按时间切 + 按实体分组；特征标注"最早可用时点"并断言 `feature_time <= label_time`。

## 复盘追问

- 如果 `gap` 设成 30 天，训练集分布与测试期差异变大，CV 会偏乐观还是偏悲观？为什么？
- 全局标准化为什么在时序 CV 里也是泄漏？把它放进 `Pipeline` 后，统计量是在哪一步算的？
