---
title: [WCN-342] WebGL/Canvas 重元素（图表/3D）封装为 WC 的要点？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-342：WebGL/Canvas 重元素（图表/3D）封装为 WC 的要点？
**答**：
- 尺寸协商：ResizeObserver 驱动 canvas 尺寸 + devicePixelRatio 处理（模糊问题）。
- 生命周期：disconnect 即销毁 GL 上下文/RAF 循环（显存泄漏主因）。
- 渲染调度：脏检查驱动重绘（数据变才渲染），空闲时暂停 RAF。
- 资源释放：dispose 模式（dispose() 显式 API + disconnectedCallback 自动调用）。

```javascript
disconnectedCallback() {
  cancelAnimationFrame(this._raf);
  this._gl?.getExtension('WEBGL_lose_context')?.loseContext();  // 显式释放
}
r
```
