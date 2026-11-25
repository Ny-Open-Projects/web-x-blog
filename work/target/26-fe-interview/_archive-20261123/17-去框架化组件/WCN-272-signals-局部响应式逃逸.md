---
title: [WCN-272] 高频局部更新（拖拽/滑块）的「逃逸通道」（绕过响应式直写 DOM）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-272：高频局部更新（拖拽/滑块）的「逃逸通道」（绕过响应式直写 DOM）？
**答**：
- 60Hz 拖拽：信号更新 + effect 写 DOM 也够快（细粒度），但预算极限场景可直写。
- 模式：直写 DOM + 结束时把终值写回信号（最终一致性）——过程中响应式静默。
- 风险：直写期间其他订阅者看不到值——只用于「纯视觉临时态」。
- 规范：逃逸必须有「归位」（写回信号）代码路径，lint 检测直写无归位。

```javascript
slider.addEventListener('input', (e) => {
  thumb.style.left = e.target.value + 'px';       // 逃逸：直写（60Hz）
});
slider.addEventListener('change', (e) => {
  sliderValue.value = +e.target.value;             // 归位：写回信号
});
r
```
