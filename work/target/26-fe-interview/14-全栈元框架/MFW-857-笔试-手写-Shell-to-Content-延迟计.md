---
title: [MFW-857] 笔试：手写 Shell-to-Content 延迟计算器与分档
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-857：笔试：手写 Shell-to-Content 延迟计算器与分档

**答**：
- 结论：STC = 关键内容时间 − 壳时间；按阈值分档 good/needs-improvement/poor，用于告警与优化方向判断。
- 关键：缺少任一 mark 返回 null（而非 NaN）；分档阈值要贴近业务体验。
- 追问钩子：STC 和 INP 有什么区别？——STC 衡量内容到达延迟，INP 衡量交互响应，二者互补。

```javascript
function calcSTC(marks) {
  const map = Object.fromEntries(marks.map(m => [m.name, m.t]));
  if (map.shell == null || map['hero-content'] == null) return null;
  const stc = map['hero-content'] - map.shell;
  const grade = stc < 200 ? 'good' : stc < 800 ? 'needs-improvement' : 'poor';
  return { stc, grade };
}

// 自测
console.log(calcSTC([{ name: 'shell', t: 120 }, { name: 'hero-content', t: 900 }]));
// { stc: 780, grade: 'needs-improvement' }
console.log(calcSTC([{ name: 'shell', t: 120 }]));    // null（缺 mark）
console.log(calcSTC([{ name: 'shell', t: 100 }, { name: 'hero-content', t: 200 }]).grade);
// good
```

**评分点**：
- 正确计算 内容时间 − 壳时间；缺 mark 返回 null 而非 NaN
- 分档阈值合理（good / needs-improvement / poor）
- 能结合 STC 与 LCP 差异给出优化方向（数据层 vs 渲染层）
- 边界：负值（内容早于壳标记）与异常数据处理
