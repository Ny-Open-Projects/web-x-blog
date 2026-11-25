---
title: [VIZ-324] 手写图表 A/B 实验：可视化方案对比（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-324：手写图表 A/B 实验：可视化方案对比（笔试）

**答**：
- 题目：两种可视化方案（柱状 vs 表格）效果对比——A/B 分流（ALG-533 复用）+ 交互行为指标（理解时长/准确率测试）。
- 思路：分流按用户哈希；指标：任务完成率（从图中读数答题）、耗时、交互深度；统计显著性（HW-820 复用）。
- 评分点：分流实现；指标设计（可读性量化）；显著性判定。

```javascript
class VizExperiment {
  constructor(key) { this.key = key; }
  assign(userId) {                                          // 分桶
    return hashStr(userId + this.key) % 100 < 50 ? 'bar' : 'table';
  }
  async run(users) {
    const groups = { bar: [], table: [] };
    for (const u of users) {
      const variant = this.assign(u.id);
      const quiz = await renderComprehensionQuiz(u.id, variant);   // 读图测试
      groups[variant].push({ correct: quiz.correct, seconds: quiz.seconds });
    }
    const acc = v => v.filter(x => x.correct).length / v.length;  // 准确率
    const sig = significance(groups.bar.length, sum(groups.bar, 'correct'),
      groups.table.length, sum(groups.table, 'correct'));   // 复用 HW-820 z 检验
    return { accuracy: { bar: acc(groups.bar), table: acc(groups.table) },
      significant: sig.significant, advice: sig.significant
        ? '采用准确率更高方案' : '无显著差异，按偏好选择' };
  }
}
```

## 补充：评分点与变体

**评分点**：

- 分桶用 hash(userId 加实验 key) 对 100 取模，同一用户稳定命中且两组比例可核对（给分）；用 Math.random 直接分导致刷新跳组（扣分）。
- 指标同时给出准确率（读图答题正确率）与耗时两个维度，并区分主指标与护栏指标（给分）；只算点击率、不体现可读性（扣分）。
- 显著性复用 z 检验或卡方，并说明样本量与 p 值口径（给分）；只看均值差就下结论、不给置信区间（扣分）。
- 输出 advice 区分显著采用与无显著按偏好，并说明实验期不中途偷看（给分）；显著即上线、样本量不足也强行判定（扣分）。

**变体与延伸**：

1. 两种方案用户量天然 10 比 90 怎么分 → 用分层分流保证每层内比例一致，或直接改 50 比 50 并延长实验期。
2. 怎么排除图好看但读不准的情况 → 加一道读数答题正确率作为硬指标，正确率低于基线即判方案失败，不看主观偏好。
3. 实验期间前端发版了，数据还能合并吗 → 必须按版本维度切分样本，跨版本数据不可直接合并，否则结论被实现差异污染。
