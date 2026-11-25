---
title: [TST-754] 笔试：实现 AI 输出「不确定性」的统计一致性测试器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-754：笔试：实现 AI 输出「不确定性」的统计一致性测试器

**题目**：输入同一 prompt 的多次输出数组 outputs（字符串数组）与最低一致率 minRate（0~1）。计算众数出现频率（最高频输出占比），若 >= minRate 则 consistent=true。返回 { mode, modeRate, consistent }。若 outputs 为空返回 { mode:null, modeRate:0, consistent:false }。

**答**：
- 统计频次找众数，计算占比。
- 空数组兜底。
- 众数并列时取先出现的（用 Map 保持插入顺序）。

```javascript
function consistencyTest(outputs, minRate) {
  if (!outputs.length) return { mode: null, modeRate: 0, consistent: false };
  const freq = new Map();
  for (const o of outputs) freq.set(o, (freq.get(o) || 0) + 1);
  let mode = null, max = 0;
  for (const [k, v] of freq) if (v > max) { max = v; mode = k; }
  const modeRate = +(max / outputs.length).toFixed(3);
  return { mode, modeRate, consistent: modeRate >= minRate };
}
console.log(consistencyTest(['退款', '退款', '退货', '退款'], 0.7));
// {mode:'退款', modeRate:0.75, consistent:true}
```

**评分点**：
- 众数统计正确
- 一致率计算正确
- 空数组兜底
- 并列取先出现者
