---
title: "C 卷 JVM"
date: 2026-11-18
categories: [Java面试, 笔试]
tags: [Java面试, 笔试题, 33]
type: 笔试题
disableNunjucks: true
---

## C 卷 JVM

**C-1（选择）** 哪个区域**不会**抛 OOM？
A. 堆　B. 元空间　C. 程序计数器　D. 直接内存
**答案：C**（唯一不 OOM 的区域）。

**C-2（选择）** 三色标记中"对象消失"必须同时满足？
A. 黑引用白 + 灰到白引用断开　B. 黑引用白 + 黑到黑断开　C. 灰引用白 + 白孤立　D. 只要黑引用白
**答案：A。** CMS 用增量更新（记录黑新增引用），G1 用 SATB（记录被断的灰引用），ZGC 读屏障自愈。

**C-3（选择）** `GC(12) Pause Young (Normal) (G1 Evacuation Pause) 2048M->456M(4096M) 12.3ms` 中 "GC(12)" 表示？
A. 第 12 次 Full GC　B. GC 编号（统一日志序号）　C. 12MB 回收　D. 12 个 Region
**答案：B（实测）**。JDK9+ 统一日志的序号特征——说得出这个细节 = 真用过 JDK9+。

**C-4（选择）** MaxTenuringThreshold 默认值？
A. 6　B. 8　C. 15　D. 21
**答案：C（PrintFlagsFinal 实测 =15）**。

**C-5（简答）** 类卸载的三个条件？
**答案**：所有实例回收、加载器回收、Class 对象无引用——Bootstrap 加载的类永不卸载。

**C-6（简答）** 为什么 G1 在小堆上反而可能不如 CMS？
**答案**：RSet 维护占堆 10%~20% + 写屏障吞吐代价；小堆收益小于成本。选型：小堆 CMS 或 Serial，6G+ 才考虑 G1。

**C-7（简答）** `-XX:+UseBiasedLocking` 在 JDK 21 上会怎样？
**答案（实测）**：`Unrecognized VM option`——偏向锁 15 禁用+废弃、18 标志废弃、21 **代码彻底移除**。讲锁升级主动报这条时间线是加分项。

**C-8（分析）** 循环内 `new byte[64]` 三千万次，`-Xmx64m` 下 GC 日志为 0，为什么？
**答案（本机实证）**：JIT 逃逸分析+标量替换——未逃逸分配全部消除。把数组写入静态字段（逃逸）后 GC 立即出现。配套教学点：GC 测试必须让对象逃逸。

---
