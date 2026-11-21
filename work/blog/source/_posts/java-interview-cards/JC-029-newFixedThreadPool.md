---
title: "[JC-029] 线程池·newFixedThreadPool（误用）"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 背诵卡, 33]
type: 背诵卡
disableNunjucks: true
---

## 线程池 · newFixedThreadPool（误用）

- **事实**：Executors.newFixedThreadPool 使用无界 LinkedBlockingQueue 可能堆积任务导致 OOM
- **原理**：队列容量是 Integer.MAX_VALUE，下游变慢时任务无限堆积，阿里手册明确禁止使用 Executors 创建线程池
- **常见误区**：
  1. newFixedThreadPool 会自动拒绝多余任务（错）
  2. 队列满了会扩容线程（错）
  3. OOM 风险只在任务执行慢时不存在（错）
- **工程用法**：生产用 new ThreadPoolExecutor 加有界队列
- **版本锚点**：阿里手册
