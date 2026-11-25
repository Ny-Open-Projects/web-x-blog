---
title: [PER-839] 移动端 Web 容器的 JS 异常与性能联动监控：崩溃前的性能信号有哪些
date: 2026-11-21
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-839：移动端 Web 容器的 JS 异常与性能联动监控：崩溃前的性能信号有哪些

**答**：
- 崩溃/白屏很少凭空发生，之前往往有性能信号：内存持续上涨（泄漏）、长任务密集（主线程拥塞）、帧率持续下滑、接口错误率上升——把性能时序与异常关联起来才能定位根因。
- 联动方案：全局异常（JS error/崩溃/白屏检测）发生时，回溯最近 N 秒（如 30s）的性能时序快照（heap、FPS、长任务、路由栈）一起上报，形成"黑匣子"。
- 白屏检测：关键节点存在性检查 + 渲染探针（首屏元素 getBoundingClientRect 可见）超时判定；判定白屏后同样携带黑匣子上报。
- 价值：把"崩溃复现不了"问题变成"有案发现场"——崩溃前 heap 曲线陡涨可指向泄漏，长任务密集指向同步阻塞。

```javascript
const blackBox = {                          // 滚动窗口性能时序（30s 黑匣子）
  buf: [], maxMs: 30000,
  push(sample) {                            // sample: {t, heapMB, fps, longTasks, route}
    this.buf.push(sample);
    while (this.buf.length && sample.t - this.buf[0].t > this.maxMs) this.buf.shift();
  },
  snapshot() { return [...this.buf]; },
};
setInterval(() => blackBox.push(sampleNow()), 1000);            // 每秒采样
addEventListener('error', e => report('js-error', {
  msg: String(e.message), stack: String(e.stack).slice(0, 2000),
  blackbox: blackBox.snapshot(),             // 回溯性能时序
}));
async function whiteScreenCheck() {          // 白屏判定 + 黑匣子
  await sleep(3000);
  const el = document.querySelector('[data-first-screen]');
  const visible = el && el.getBoundingClientRect().width > 0;
  if (!visible) report('white-screen', { blackbox: blackBox.snapshot(), route: location.pathname });
}
```
