---
title: [TST-672] 笔试：实现 AI 测试助手价值评分卡
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-672：笔试：实现 AI 测试助手价值评分卡

**题目**：实现 scorecard(m,weights)。m 含 {savedMin,bugsFound,falsePositives,reviewMin,mutationScore}。四维归一到 0~100 后加权求总分，返回最弱维度与是否合格（>=60）。

**答**：
- 四个维度：效率（节省时长）、效果（新增缺陷）、成本（误报处理 + 评审）、质量（变异存活率）。
- 各维度归一到 0~100 后加权，输出总分与短板维度。
- 净收益为负时直接判不合格。

```javascript
function scorecard(m, weights = { eff: 0.3, found: 0.3, cost: 0.2, qual: 0.2 }) {
  const norm = x => Math.max(0, Math.min(100, Math.round(x)));
  const s = {
    eff: norm(m.savedMin / 2),
    found: norm(m.bugsFound * 20),
    cost: norm(100 - m.falsePositives * 3 - m.reviewMin / 2),
    qual: norm(m.mutationScore * 100),
  };
  const total = +Object.entries(weights)
    .reduce((t, [k, w]) => t + s[k] * w, 0).toFixed(1);
  const weakest = Object.entries(s).sort((a, b) => a[1] - b[1])[0][0];
  return { s, total, weakest, qualified: total >= 60 };
}
```

**评分点**：
- 四维归一化与钳制正确
- 加权总分计算
- 短板维度识别
- 合格线判定
