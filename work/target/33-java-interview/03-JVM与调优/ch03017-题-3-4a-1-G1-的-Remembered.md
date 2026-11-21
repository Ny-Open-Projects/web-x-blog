---
title: "题 3.4a.1：G1 的 Remembered Set 与写屏障的成本，为什么说\"没有免费的并发\"？"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 面试题, 33]
type: 面试题
disableNunjucks: true
---

### 题 3.4a.1：G1 的 Remembered Set 与写屏障的成本，为什么说"没有免费的并发"？

**【面试官意图】** 区分"背 G1 特性"与"理解 G1 代价"——P8 以上必考。
**【参考回答（可背）】** 问题背景：Region 化之后跨 Region 引用（老年代 Region 引用新生代，或任意方向）必须被记录，否则回收单个 Region 会漏活对象。机制：每个 Region 一张 RSet，通过**写屏障**维护——应用每次引用赋值都会触发 post-write barrier，找到目标 Region 的 card 标记。代价：① 写屏障是每次引用赋值都执行的指令，分配密集型应用吞吐损失 5%~10%；② RSet 内存可能占堆 10%~20%（引用密集场景）；③ 维护 RSet 的 Refinement 线程吃 CPU。**所以 G1 在小堆、分配密集、CPU 紧张时不占优**——"并发/增量回收的每一点停顿优化，都是用吞吐和内存换的"。
**【追问链】** ① 什么场景 RSet 特别大？（大量老年代对象互相引用且稀疏分布在多 Region）② 怎么缓解？（G1HeapRegionSize 调大减少跨 Region 数、或换 ZGC 用着色指针免 RSet）。
**【P10 加分项】** 哲学升华："三色标记解决'漏标'靠屏障，ZGC 解决 RSet 靠着色指针，分代 ZGC 换来吞吐——每一代 GC 的进步都是'把某个成本换到更便宜的地方'，调优者的工作就是找到你们业务的便宜成本项。"
