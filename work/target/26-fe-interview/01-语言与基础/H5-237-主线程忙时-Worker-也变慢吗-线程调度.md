---
title: [H5-237] 主线程忙时 Worker 也变慢吗：线程调度
date: 2026-11-19
categories: [HTML5]
tags: [前端面试, 面试题, Worker]
type: 面试题
---

## H5-237：主线程忙时 Worker 也变慢吗：线程调度

**答**：
- Worker 是独立线程，主线程卡顿时 Worker 仍能满速计算——这正是它的核心价值
- 但三个环节仍会受主线程影响：消息接收（主线程忙时 onmessage 回调排队）、结果渲染（Worker 算完还是要主线程画）、核心争抢（核数不足时 CPU 线程之间抢时间片）
- 移动端核心数少（4~6 核）且大小核混合，小核上的 Worker 可能比大核慢 2~3 倍——性能预估要按低端机
- 优先级问题：Worker 任务无法被浏览器降级/暂停，长任务会持续占用 CPU；要用「分片 + 中断检查」实现可取消
- 实战结论：Worker 适合「计算重、交互少」的任务；既重计算又需要即时反馈的场景要分片回报进度

```javascript
// Worker 内部实现可取消的长任务（分片 + 检查消息）
let cancelled = false;
self.onmessage = ({ data }) => { if (data === 'CANCEL') cancelled = true; };
function loop() {
  for (let i = 0; i < 1000 && !cancelled; i++) processOne();
  if (!cancelled) setTimeout(loop, 0); // 分片让出线程，可响应取消消息
}
```
