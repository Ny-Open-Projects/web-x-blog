---
title: "第 3 章 JVM 与性能调优"
date: 2026-11-18
categories: [Java面试, 速记卡]
tags: [Java面试, 速记卡, 33]
type: 速记卡
disableNunjucks: true
---

## 第 3 章 JVM 与性能调优

1. 五区：程序计数器不 OOM；栈溢出 SOE；元空间 JDK8 在本地内存。
2. 分配路径：TLAB → Eden CAS → Survivor 复制 → 年龄 15/动态年龄 → 老年代。
3. Full GC 触发 5 条：老年代满、元空间满、System.gc、CMS 失败、G1 失败。
4. 双亲委派三目的：安全、唯一、复用；打破场景：SPI/Tomcat/热部署。
5. 三色标记漏标两条件：黑引白 + 灰断白；CMS 增量更新，G1 SATB，ZGC 读屏障自愈。
6. G1：Region 化、停顿预测、Humongous 是大坑、小堆 CMS 反而优；RSet/写屏障有代价。
7. ZGC：着色指针+读屏障；JDK21 分代 ZGC 是生产推荐。
8. 排查三板斧：jstat 看趋势 → jmap dump → MAT 找支配树；Arthas 线上诊断。
9. OOM 三件套必开：HeapDumpOnOutOfMemoryError、GC 日志、ExitOnOutOfMemoryError。
10. JIT 三板斧：分层编译、内联、逃逸分析；新实例要预热。
11. 元空间泄漏五成因：CGLIB/脚本/反射膨胀/加载器不释放/热更新；动态能力要有配额。
12. 容器 JVM：MaxRAMPercentage 50~70、cgroup 感知、区分 JVM OOM 与 OOMKilled、堆外合计 ≤85%。
13. 9 种 OOM 先分流：堆类（有 dump）vs 资源类（看线程数/堆外）——分流错了浪费时间。
