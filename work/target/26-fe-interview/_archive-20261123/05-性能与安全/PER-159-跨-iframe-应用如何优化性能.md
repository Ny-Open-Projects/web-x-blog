---
title: [PER-159] 跨 iframe 应用如何优化性能？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-159：跨 iframe 应用如何优化性能？

**答**：
- **消息批处理**：高频消息（滚动同步、鼠标轨迹）用 rAF 每帧合并成一条 postMessage，禁止每个事件发一条——序列化与跨域通信本身有成本。
- **懒挂载**：视口外的 iframe 不加载，用 IntersectionObserver 进入视口前 200px 再注入 src；iframe 创建有 100ms 级开销与独立文档解析成本。
- **加载隔离**：长任务子应用放独立 iframe，利用进程隔离避免它阻塞主应用的 rAF 与 INP；但高频创建场景改用 Worker 或微前端更划算。
- 通信协议收敛到一个 SafeChannel（见 PER-129），统一做节流、重试与销毁，防止多套通信逻辑叠加泄漏。

```javascript
// 跨 iframe 性能：消息批处理 + 懒挂载 + 加载隔离
const ORIGIN = 'https://app.partner.com';
const frame = document.getElementById('partner-frame');

// 1. 高频消息按帧批量：滚动同步、鼠标轨迹合并为一条 postMessage
let queue = [];
function flush() {
  if (!queue.length) return;
  frame.contentWindow.postMessage({ type: 'batch', items: queue }, ORIGIN);
  queue = [];
}
host.addEventListener('mousemove', (e) => {
  queue.push({ x: e.clientX, y: e.clientY });
  requestAnimationFrame(flush); // 每帧最多一条消息
});

// 2. 懒挂载：视口外的 iframe 不加载，接近视口再注入 src
const io = new IntersectionObserver((entries) => {
  entries.forEach((en) => {
    if (!en.isIntersecting) return;
    en.target.src = en.target.dataset.src; // data-src 占位，进入视口才真正发起请求
    io.unobserve(en.target);
  });
}, { rootMargin: '200px' });
document.querySelectorAll('iframe[data-src]').forEach((f) => io.observe(f));

// 3. 加载隔离：重计算子应用放独立 iframe，利用进程隔离保护主应用帧率
// 注意 iframe 创建约 100ms 级开销，高频创建场景改用 Worker 或微前端
```
