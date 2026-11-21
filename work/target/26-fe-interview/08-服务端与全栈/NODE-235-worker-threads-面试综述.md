---
title: [NODE-235] worker_threads 面试综述？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-235：worker_threads 面试综述？
**答**：
- 综述框架：适用边界（NODE-226）→ 通信与零拷贝（227/229）→ 池化设计（228）→ 生命周期与容错（230）→ I/O 陷阱（231）→ 组合部署（232）。
- 高频追问与答案锚点："worker 之间怎么共享数据"→ SharedArrayBuffer + Atomics；"大 Buffer 传输卡顿"→ transferList 零拷贝；"池多大"→ CPU 核数起步压测扫档。
- 反模式清单：worker 里连 DB（连接爆炸）、小任务进 worker（开销倒挂）、未监听 error（进程崩溃）、启动数据超大盘（主线程序列化卡）。
- 收尾给案例：图片服务上传链路——主线程收流（流式），worker 池做 sharp 压缩（CPU），结果 transferable 回传，DB 写入主线程统一收口。

```javascript
// 综述一页纸
// 1) 边界：CPU 密集 & >10ms & 无共享可变状态 → worker；否则事件循环/微任务切片
// 2) 通信：postMessage(克隆) vs transfer(零拷贝) vs SAB(共享内存)
// 3) 池：piscina / 手写（队列+上限+超时+重建）
// 4) 容错：error → failAll+respawn；僵尸 → terminate；SIGTERM → 优雅 drain
// 5) 部署：cluster/PM2 多进程 × 进程内 worker pool = 双层并发
// 案例链路：req(stream) → cpu-pool(sharp) ←transferable← → res(stream) —— 全程 O(chunk) 内存
```
