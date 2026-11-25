---
title: [OPS-293] 笔试题——实现 SRM 偏斜检测器（分流比例失配告警）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## OPS-293：手写 SRM 检测器

**需求与边界**：
- 需求：观测灰度组与对照组样本计数，检验比例是否符合预期分配——卡方拟合优度检验（单侧）+ 逐维度切片检测（按端/地域切，定位偏差来源）。
- 边界：① 卡方统计量 χ² = Σ(O-E)²/E，自由度 k-1；② 小样本下限（每桶 <100 不检验，标注 insufficient）；③ 切片定位：全局正常但某切片异常 = 细分分流 bug。

**答**：
```javascript
function chiSquareSF(counts, expected) {               // counts: [实际], expected: [比例]
  const total = counts.reduce((s, c) => s + c, 0);
  if (counts.some(c => c < 100)) return { insufficient: true };   // 小样本不检验
  const chi = counts.reduce((s, c, i) => {
    const e = total * expected[i];
    return s + (c - e) ** 2 / e;
  }, 0);
  const df = counts.length - 1;
  const p = chiSquarePValue(chi, df);                  // 上尾概率
  return { chi, df, p, skewed: p < 0.001 };            // 极显著才告警（控制误报）
}
function srmMonitor(observed, expected, dims) {
  const global = chiSquareSF(observed, expected);
  const slices = Object.entries(dims).map(([name, byDim]) => ({
    dim: name,
    ...Object.fromEntries(Object.entries(byDim).map(([k, cnt]) =>
      [k, chiSquareSF(cnt, expected)])),               // 逐切片检验
  }));
  const badSlice = slices.flatMap(s => Object.entries(s).slice(1))
    .find(([, v]) => v.skewed);
  return { global, slices, localize: badSlice ? badSlice[0] : null };   // 偏差来源定位
}
```

**评分点**:
- 卡方拟合优度正确（O-E)²/E 累加 + 上尾 p 值。
- 极显著阈值（p<0.001）控制误报。
- 逐切片检验定位偏差来源（全局正常切片异常 = 细分 bug）。
- 小样本 insufficient 保护。
