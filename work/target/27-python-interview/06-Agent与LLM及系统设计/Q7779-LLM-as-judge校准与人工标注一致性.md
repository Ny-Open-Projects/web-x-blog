---
title: "[Q7779] judge 打 95 分业务却在跌：LLM-as-judge 的校准与人工标注一致性"
date: 2026-11-24
categories: [PythonAgent与LLM]
tags: [Python面试, 面试题, 27]
type: 面试题
---

### Q7779 · judge 打 95 分业务却在跌：LLM-as-judge 的校准与人工标注一致性

难度：P7 ｜ 标签：LLM-as-judge、kappa、校准、长度偏置、评测指标

基线：Python 3.12；实现 Cohen's kappa 一致性度量，演示 judge 的长度偏置（粗一致率 80% 但 kappa 仅 0.60）与校准修复，全标准库实跑。

**问**：自建 judge 给模型输出打分，评测分数 95 分一路创新高，线上用户投诉却在涨——judge 和真实质量脱节了。judge 上线前要做什么校准？"粗一致率"为什么不可信？长度偏置、格式偏置这些系统性偏差怎么发现和修？kappa 为什么比一致率更诚实？

**答**：
- **结论**：judge 本质是一个模型在评另一个模型，它自带系统性偏差，上线前必须与人工标注对齐：构造校准集（200~500 样本，按类别分层采样），人工标注与 judge 双盲打分，算两个指标——**粗一致率**（agree rate）和 **Cohen's kappa**。粗一致率危险在**基线膨胀**：数据类别不平衡时（80% 是 good），一个"全部判 good"的垃圾 judge 也有 80% 一致率——本卡演示：长度偏置 judge（>400 字一律判 good）粗一致率 80%，看似能用；kappa 扣除随机一致的期望后只有 0.60——它的一致性远低于表面。kappa 的意义：**把"碰巧一致"从分数里剔掉**，衡量的是超出概率的一致性，kappa < 0.6 的 judge 不配上岗。偏差的发现：按样本属性（长度、格式、语言）分组算一致率，**组间差异 >10 个百分点就是系统性偏置**——本卡"长且差的样本"全部被 judge 判 good，长度偏置实锤。修复：偏置源进 judge 提示（"长度与质量无关"）+ 校准集补长差样本 + 分位数归一（按长度分组归一分数）。
- **取舍**：① judge 的定位：它是**回归监控的仪表**（大量样本、低成本、可重复），不是终审——抽查人工复核永远保留一条独立通道，两者差异率本身是 judge 的健康指标；② 校准集的时效：产品形态变了（输出变长、新增语言）校准集要重标，老校准集上的高分是新偏差的遮羞布；③ 多 judge 投票 vs 单 judge 精调：预算够时 2~3 个异构 judge 投票（Q7777 的归并逻辑）比单 judge 提示调优更稳——judge 的偏差也是模型偏差，异构是对冲；④ 分数 vs 排序：judge 打的绝对分数不可跨版本比较（换 judge 模型分数漂移，Q7599 类问题），**用同 judge 的相对排序**（新版本 vs 老版本 A/B 对评）才是跨版本可迁移的信号。
- **实战**：① judge 上线 checklist：kappa ≥ 0.6、分组一致率差 < 10pp、校准集留档、复核通道开启——四条缺一不放量；② 评测分数与业务指标的**联动监控**：评测分新高 + 业务投诉上升的组合告警（本卡事故的自动化版），两者背离即人工介入（Q7533 离线在线一致性的持续版）；③ 校准集按类别分层采样（good/bad、长/短、各语言均衡）——不平衡的校准集算出的 kappa 也骗人；④ judge 的 prompt 版本管理（Q7507）：judge 提示变更视同模型变更，要重新校准再上线。

```python
"""Q7779 LLM-as-judge 校准: judge 与人工标注的一致性(kappa), 长度偏置的校准修复。"""


def cohens_kappa(a: list[str], b: list[str]) -> float:
    """Cohen's kappa: 扣除随机一致后的一致性度量."""
    labels = sorted(set(a) | set(b))
    n = len(a)
    po = sum(x == y for x, y in zip(a, b)) / n
    pa = {l: a.count(l) / n for l in labels}
    pb = {l: b.count(l) / n for l in labels}
    pe = sum(pa[l] * pb[l] for l in labels)
    return (po - pe) / (1 - pe) if pe < 1 else 0.0


# 20 个样本: 人工标注 与 两版 judge
# judge_v1 有长度偏置: 长答案一律判 good(不看内容)
HUMAN = ["good", "bad", "good", "bad", "good", "bad", "good", "bad",
         "good", "bad", "good", "bad", "good", "bad", "good", "bad",
         "good", "bad", "good", "bad"]
LENGTHS = [120, 800, 90, 150, 600, 110, 95, 480,
           130, 720, 85, 140, 550, 100, 125, 690,
           115, 90, 800, 135]


def judge_v1(lengths: list[int]) -> list[str]:
    """带长度偏置: 超过 400 字一律 good."""
    return ["good" if l > 400 else ("good" if i % 2 == 0 else "bad")
            for i, l in enumerate(lengths)]


def judge_v2(lengths: list[int]) -> list[str]:
    """校准后: 长度不再直接决定结论(回归人工分布)."""
    return [("good" if i % 2 == 0 else "bad") for i, _ in enumerate(lengths)]


if __name__ == "__main__":
    v1 = judge_v1(LENGTHS)
    v2 = judge_v2(LENGTHS)
    agree1 = sum(x == y for x, y in zip(HUMAN, v1)) / len(HUMAN)
    agree2 = sum(x == y for x, y in zip(HUMAN, v2)) / len(HUMAN)
    k1 = cohens_kappa(HUMAN, v1)
    k2 = cohens_kappa(HUMAN, v2)
    long_bad = sum(1 for h, l in zip(HUMAN, LENGTHS) if h == "bad" and l > 400)
    print(f"长且差的样本: {long_bad} 个 -> judge_v1 全判 good (长度偏置)")
    print(f"v1: 粗一致率 {agree1:.0%}, kappa={k1:.2f}")
    print(f"v2: 粗一致率 {agree2:.0%}, kappa={k2:.2f}")
    ok = k2 > k1 and long_bad > 0
    print(f"校验: kappa 量化偏置并验证校准收益 -> {'通过' if ok else '异常'}")
    print("结论：judge 上线前必须和人工标注算 kappa, 粗一致率会掩盖类别偏置;")
    print("      长度/格式偏置是 LLM judge 两大顽疾, 校准集要按类别分层采样")
```

**追问一**：为什么评测分数与业务指标会背离？发现背离后怎么归因？

→ 解析：背离的根源是**评测集与线上分布的错位**：评测集是历史 badcase + 人工构造样本（分布静态、难度分布偏中间），线上流量是动态分布（新场景、新用户话术、边缘 case）——judge 在评测集上的高分只证明"评测集覆盖的区域内质量好"。归因四步：① **分布比对**：线上流量的聚类（话题、长度、语言、复杂度）与评测集分布逐桶对比，找出"线上有、评测集没有"的桶——背离通常精准落在这个桶里；② **judge 抽检**：从背离桶抽线上样本让 judge 打分、人工标注对照——judge 在新分布上的 kappa 可能骤降（偏置在新属性上发作，比如新出的超长输出触发长度偏置）；③ **生成侧核查**：judge 没问题的话查生成侧（新版本模型在老评测集上过拟合、线上用的提示与评测用的不一致，Q7509 类配置漂移）；④ **指标口径**：业务投诉率的分母变化（用户量暴增、入口变更）有时伪装成质量下降。预防机制：评测集的**滚动更新管线**——线上抽样新场景定期人工标注进评测集（Q2988 评测集版本化），让"分布错位"的窗口期从季度缩到周。评测与业务的关系是"仪表盘与路况"：仪表盘必须持续对表，否则越精确的仪表盘越自信地指着错的方向。

**追问二**：Cohen's kappa 有什么局限？多类别/多 judge 场景该用什么度量？

→ 解析：kappa 的三个局限：① **类别不平衡敏感**：极端不平衡下 kappa 的期望基线本身不稳，会出现"一致率很高但 kappa 为负"的反直觉（一致都落在多数类上）；② **边际分布依赖**：两个标注者的类别使用频率差异会压低 kappa——judge 整体更严（bad 判得多）时 kappa 低，但这可能是合理的严格而非不一致；③ **序数信息丢失**：good/mid/bad 是有序等级，kappa 把"good vs bad 的分歧"和"good vs mid 的分歧"等价看待——前者是事故后者是噪音。进阶度量按场景选：多标注者一致性用 **Fleiss' kappa** 或 **Krippendorff's alpha**（支持缺失值与任意尺度）；序数等级用**加权 kappa**（分歧距离加权）或直接报**分组一致率矩阵**（confusion matrix 看分歧落在哪一对类别上，比单一标量有信息量得多）；连续分数（1-10 打分）用 **Pearson/Spearman 相关** + 分位数偏差图。工程建议：主指标选一个（Krippendorff's alpha 通用性最好），辅以 confusion matrix 做归因——单一标量永远会掩盖 judge 的病灶位置，矩阵才是诊断工具。
