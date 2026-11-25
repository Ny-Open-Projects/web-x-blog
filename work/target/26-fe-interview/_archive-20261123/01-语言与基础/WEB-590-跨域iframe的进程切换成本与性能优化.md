---
title: [WEB-590] 跨域 iframe 的进程切换成本与性能优化
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 浏览器架构]
type: 面试题
---

## WEB-590：跨域 iframe 的进程切换成本与性能优化

**答**：
- 每个跨站 iframe 是独立进程：创建成本含进程 fork、V8 实例初始化、首帧渲染；页面带多个第三方 iframe（广告/社交组件）时进程数与内存显著上涨
- 通信成本：主文档 ↔ iframe 一切交互（postMessage、resize 上报）跨进程，高频同步调用（如拖拽实时同步）会卡
- 懒加载是第一杠杆：`loading="lazy"` + 交互触发加载（点击后挂 iframe），把第三方进程创建推迟到真正需要时
- 规格协商：预留 iframe 尺寸（width/height/aspect-ratio）避免进程起来后再 layout 抖动；`credentialless` iframe 减少凭据加载开销
- 通信架构优化：合并消息（节流 postMessage）、用 MessageChannel 建点对点通道避免经 window 层级转发、大批量数据用 transferable（postMessage 第二参数）零拷贝

```javascript
// 高频同步优化: 节流 + transferable
let pending = null;
function syncDrag(x, y) {
  pending = { x, y };
  if (pending.__t) return;
  pending.__t = setTimeout(() => {
    const buf = new Float32Array([pending.x, pending.y]);
    iframe.contentWindow.postMessage(buf, '*', [buf.buffer]); // transferable
    pending.__t = null;
  }, 32); // ~2帧节流
}
```
