---
title: "题 3.2.1：说说 Minor GC、Major GC、Full GC 的区别？什么情况触发 Full GC？"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 面试题, 基础题, 33]
type: 面试题
disableNunjucks: true
---

### 题 3.2.1：说说 Minor GC、Major GC、Full GC 的区别？什么情况触发 Full GC？

**【参考回答（可背）】**
- **Minor GC**：Eden 满触发，回收新生代，STW 短（存活对象少，复制算法快）。触发最频繁。
- **Major GC**：术语混乱，通常等价于老年代收集（CMS 的 concurrent collection）。
- **Full GC**：整堆+元空间，STW 最长，是性能事故的头号嫌疑。
触发条件必背 5 条：
1. 老年代空间不足（晋升对象超限）；
2. 元空间不足；
3. System.gc()（建议，可用 -XX:+DisableExplicitGC 禁掉——**堆外内存依赖 System.gc() 的话禁了会 Direct Memory OOM**，正确姿势是 -XX:+ExplicitGCInvokesConcurrent）；
4. CMS 晋升失败（promotion failed）或并发模式失败（concurrent mode failure）→ 退化 Serial Old；
5. G1 的 to-space exhausted / humongous 对象堆积失败退化 Full GC。

**【追问链】**
1. 为什么新生代用复制、老年代用整理？→ 新生代对象朝生夕死、存活率低，复制便宜；老年代存活率高，复制代价大，且需要无碎片支持大对象。
2. 为什么需要两个 Survivor？→ 一个 Survivor 放不下"本次存活 + 上次残留"时会直接晋升，破坏年龄分代设计；两块轮流用保证每次复制都有空区。

**【P10 加分项】**
指出"Full GC 频率"是最该监控的指标，且给出经验阈值：老年代增长速率稳定、Full GC 每天夜深发生一次可以接受；白天突发 Full GC 必查。顺带讲"元空间泄漏"：动态生成类（CGLIB 代理、Groovy 脚本、反射频繁生成）撑爆元空间——连接了第 4 章的 Spring 场景。

---
