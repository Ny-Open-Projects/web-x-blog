---
title: [AGT-688] 手写 judgeCalibrate：与金标一致率、逐级混淆矩阵、偏差报告、重校准建议？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-688：手写 judgeCalibrate：与金标一致率、逐级混淆矩阵、偏差报告、重校准建议

**需求与边界**：
- 实现 judgeCalibrate(judgeScores, golden)。
- 边界要求：① 金标五档（0~4），输出混淆矩阵与一致率；② 逐档偏差（judge 系统性偏严/偏松各档量化）；③ 相邻档混淆容忍、跨两档以上算大错单独统计；④ 一致率 <80% 输出重校准建议（附典型错例）。

**答**：
```javascript
function judgeCalibrate(judgeScores, golden) {
  const K = 5;
  const conf = Array.from({ length: K }, () => Array(K).fill(0));
  judgeScores.forEach((s, i) => conf[golden[i]][s]++);  // 金标行×judge列
  const total = judgeScores.length;
  const agree = conf.reduce((a, row, g) =>
    a + row.reduce((b, v, j) => b + (j === g ? v : 0), 0), 0);
  const bias = conf.map((row, g) => {              // 逐档系统偏差
    const judged = weightedMean(row);
    return { gold: g, judged, drift: judged - g }; // 正=偏松
  });
  const big = judgeScores.filter((s, i) =>
    Math.abs(s - golden[i]) >= 2).length;          // 跨两档大错
  return { conf, agreeRate: agree / total, bias,
    bigErrRate: big / total,
    recalibrate: agree / total < 0.8
      ? { suggest: 'revise-rubric', samples: worstCases(conf, judgeScores, golden) }
      : null };
}
```

**评分点**:
- 混淆矩阵与一致率正确；逐档 drift 正负语义清晰（正=偏松）。
- 跨档大错独立统计（比一致率更刺眼的健康指标）。
- 低于阈值给重校准建议并附典型错例（可行动）。

