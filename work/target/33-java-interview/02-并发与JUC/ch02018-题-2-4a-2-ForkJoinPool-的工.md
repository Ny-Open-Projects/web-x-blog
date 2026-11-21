---
title: "题 2.4a.2：ForkJoinPool 的工作窃取是什么？commonPool 有哪些坑？"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 2.4a.2：ForkJoinPool 的工作窃取是什么？commonPool 有哪些坑？

**【参考回答（可背）】** ForkJoinPool：每个 worker 有自己的双端队列，自己从头部取任务，空闲 worker 从其他队列**尾部窃取**——减少竞争、提高缓存命中。commonPool 是 JVM 全局共享池（parallelStream、CompletableFuture 默认都在里面），大小=CPU 核-1。三大坑：① **全局共享**：一个阻塞任务拖垮所有并行流（所以 CF 生产必须自定义线程池）；② 阻塞任务让窃取失效（worker 被钉住）；③ ManagedBlocker 可告知阻塞让池补偿扩容，但很少人正确使用。
**【追问链】** ① parallelStream 的线程是哪来的？（commonPool，且并行流+外部阻塞=灾难组合）② 怎么给并行流指定池？（把流操作提交到自定义 FJP 中执行——技巧但更推荐直接不用 parallelStream 改显式线程池）。
**【P10 加分项】** "commonPool 的正确用法是'纯 CPU 计算的分治'；一旦任务里有 IO，它就是全局故障域。我们规定 parallelStream 只用于纯内存转换计算，IO 聚合一律 CompletableFuture+专用池。"
