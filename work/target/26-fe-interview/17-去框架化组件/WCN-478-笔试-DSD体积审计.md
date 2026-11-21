---
title: [WCN-478] 笔试：实现 DSD 输出的体积审计（模板占比）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-478：笔试：实现 DSD 输出的体积审计（模板占比）。
**题目**：输入整页 HTML：统计 DSD 模板字节数占总量比；> 40% 告警并列出占比最高的元素 tag（优化目标）。

```javascript
function dsdBudget(html, { threshold = 0.4 } = {}) {
  const total = html.length;
  const by = new Map();
  for (const m of html.matchAll(/<([\w-]+)[^>]*>\s*<template shadowrootmode="open">([\s\S]*?)<\/template>/g)) {
    by.set(m[1], (by.get(m[1]) || 0) + m[2].length);
  }
  const tmplBytes = [...by.values()].reduce((a, b) => a + b, 0);
  const ratio = tmplBytes / total;
  const top = [...by].sort((a, b) => b[1] - a[1]).slice(0, 3)
    .map(([tag, n]) => `${tag}(${(n / total * 100).toFixed(0)}%)`);
  return { ratio: +ratio.toFixed(2), over: ratio > threshold, top };
}

```

**评分点**：
- 正则提取 template 块字节数。
- 按 tag 分组占比排序。
- 阈值告警（40%）。
- 优化建议（critical 内联 + 水合 adopt）。
