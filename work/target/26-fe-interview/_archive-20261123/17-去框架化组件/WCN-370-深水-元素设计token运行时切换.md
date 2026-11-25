---
title: [WCN-370] 运行时主题切换（无刷新）的完整链路与边界？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-370：运行时主题切换（无刷新）的完整链路与边界？
**答**：
- 链路：切换动作 → root 类/属性变更 → CSS 变量继承更新 → shadow 内即时生效（零 JS 参与）。
- 即时生效的原理：变量解析在样式计算时——不需要元素重渲染。
- 边界：JS 侧读 token 值的场景（canvas 颜色）需要监听切换事件手动更新。
- 验证：切换瞬间无闪烁（对比截图逐帧审计）。

```javascript
document.documentElement.classList.toggle('dark');
// shadow 内 var(--ds-bg) 即刻生效（样式计算层）
// JS 侧：themeBus.on('change', () => chart.setColor(getToken('--ds-primary')));
r
```
