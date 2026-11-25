---
title: [MP-257] 小程序 Worker 数据管道怎么实现（大 JSON 解析）？
date: 2026-11-19
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-257：Worker 数据管道？
**答**：
- 架构：主线程 wx.createWorker('workers/parse.js') → postMessage(rawData) → worker 内解析/计算 → postMessage(result) → 主线程 setData。
- 场景：大 JSON 解析（10MB+ 接口响应）、报表计算、加密解密——避免逻辑层主线程阻塞导致交互卡死。
- 工程封装：WorkerPool（复用 worker，最多 5 个）、任务队列 + 超时取消、序列化成本评估（传字符串比对象小）。
- 限制：worker 与主线程通信是拷贝（非共享内存）——超大对象传输本身有成本，权衡「解析阻塞」vs「传输开销」。
- 监控：worker 任务耗时上报，超阈值回退主线程分片处理。
