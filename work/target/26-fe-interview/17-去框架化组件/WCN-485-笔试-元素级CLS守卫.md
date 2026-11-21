---
title: [WCN-485] 笔试：实现元素的 CLS 守卫（懒加载占位高度估算）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-485：笔试：实现元素的 CLS 守卫（懒加载占位高度估算）。
**题目**：`guardLayout(el, estHeight)`：懒加载前设置占位高度（min-height），加载完成移除并测量实际高度；偏差 > 20% 告警（估算不准）。

```javascript
function guardLayout(el, estHeight) {
  el.style.minHeight = estHeight + 'px';
  return () => {   // 加载完成后调用
    el.style.minHeight = '';
    const real = el.getBoundingClientRect().height;
    const dev = Math.abs(real - estHeight) / Math.max(1, estHeight);
    if (dev > 0.2 && el.isConnected)
      report({ type: 'cls-est-drift', est: estHeight, real: Math.round(real), dev: +dev.toFixed(2) });
  };
}

```

**评分点**：
- 占位防 CLS（min-height 预留）。
- 偏差度量（估算 vs 实际）。
- 告警阈值与采样（估算质量监控）。
- 卸载安全（断开后不再测量）。
