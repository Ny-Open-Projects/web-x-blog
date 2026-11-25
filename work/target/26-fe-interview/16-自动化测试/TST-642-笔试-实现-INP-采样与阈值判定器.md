---
title: [TST-642] 笔试：实现 INP 采样与阈值判定器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-642：笔试：实现 INP 采样与阈值判定器

**题目**：实现 judgeINP(samples,{threshold,minSamples})。samples=[{duration,target}]。计算 P75（排序后按 ceil(n*0.75)-1 取），样本不足返回 insufficient，否则按阈值判定 pass/fail，并返回最差交互 target。

**答**：
- 用数组收集交互延迟，P75 用排序后插值位置计算。
- 判定要带样本量检查：样本太少不给结论。
- 输出最差交互的 target 名称便于定位。

```javascript
function judgeINP(samples, { threshold = 200, minSamples = 10 } = {}) {
  if (!samples.length) return { verdict: 'no-data' };
  const s = [...samples].sort((a, b) => a.duration - b.duration);
  const p75 = s[Math.min(s.length - 1, Math.ceil(s.length * 0.75) - 1)].duration;
  const worst = s[s.length - 1];
  return {
    samples: s.length,
    p75,
    verdict: s.length < minSamples ? 'insufficient'
      : p75 <= threshold ? 'pass' : 'fail',
    worstTarget: worst.target,
  };
}
console.log(judgeINP([{ duration: 100, target: 'btn' },
  { duration: 300, target: 'input' }]));
```

**评分点**：
- P75 分位数计算正确
- 样本量不足的保护逻辑
- 最差元素定位信息
- 边界（空数组/单样本）处理
