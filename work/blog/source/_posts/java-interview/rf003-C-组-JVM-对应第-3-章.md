---
title: "C 组：JVM（对应第 3 章）"
date: 2026-11-18
categories: [Java面试, 快问快答]
tags: [Java面试, 快问快答, 33]
type: 快问快答
disableNunjucks: true
---

## C 组：JVM（对应第 3 章）

21. **对象分配路径？** TLAB → Eden CAS → Survivor 复制 → 年龄 15/动态年龄 → 老年代。
22. **Full GC 触发五条？** 老年代满、元空间满、System.gc、CMS 失败、G1 to-space exhausted。
23. **双亲委派三目的？** 安全（核心类不可替换）、唯一（同类一个加载器）、复用（父加载不重复）。
24. **三色标记漏标两条件？** 黑引用了白 + 灰到白的引用被断；CMS 增量更新，G1 SATB，ZGC 读屏障自愈。
25. **G1 什么时候反而不如 CMS？** 小堆（<6G）：RSet 维护成本占堆 10%+，CMS 卡表更便宜。
26. **ZGC 亚毫秒的秘密？** 着色指针 + 读屏障自愈，让对象复制也并发；JDK21 分代 ZGC 是生产推荐。
27. **OOM 排查三板斧？** jstat 看趋势 → jmap -dump:live → MAT 支配树找 GC Roots 引用链。
28. **JVM 必开三件套？** HeapDumpOnOutOfMemoryError、统一 GC 日志、ExitOnOutOfMemoryError（OOM 快速失败）。
29. **JIT 三板斧？** 分层编译（C1+C2）、方法内联（<35 字节）、逃逸分析（标量替换/锁消除）。
30. **无栈异常怎么排查？** HotSpot 高频异常省略栈帧，加 -XX:-OmitStackTraceInFastThrow。
