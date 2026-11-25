---
title: [PER-980] 渲染管线的"Skip Content"优化：defer 阶段能跳过什么
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-980：渲染管线的"Skip Content"优化：defer 阶段能跳过什么

**答**：
- 浏览器对不可见区域跳过：视口外子树（content-visibility）、display:none 子树不参与 Style/Layout、独立滚动容器可部分跳过。
- 对 SPA 的含义：切换路由时旧页面卸载要彻底（unmount），否则残留的 display:none 子树仍占内存与后续失效成本。
- 深水：visibility 与 display 的差别——visibility:hidden 仍占布局参与部分计算，大块隐藏内容用 display:none 或移除 DOM。
- 检查：内存面板对比路由切换后的 detached 节点数与 retained size。

```javascript
// 路由切换残留检测
function auditHiddenTrees(root = document.body) {
  const report = [];
  for (const el of root.querySelectorAll('*')) {
    if (getComputedStyle(el).display === 'none' && el.querySelectorAll('*').length > 200)
      report.push({ sel: el.className, nodes: el.querySelectorAll('*').length,
        advice: '大块隐藏内容建议 unmount 或懒挂载' });
  }
  return report;
}
// display:none 子树虽不参与布局，但事件/内存/样式失效仍在
```
