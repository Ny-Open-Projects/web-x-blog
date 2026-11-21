---
title: "[话术JC-031] 线程池·AbortPolicy（拒绝策略）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 线程池 · AbortPolicy（拒绝策略）—— 7 类问法与标准话术

**Qconcurrency-211（概念考察·P1-P3）**
【面试官】请谈谈你对「线程池」中「AbortPolicy」的理解。
【标准回答话术】ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。背后的原理是：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理。
【评分点】① 准确说出核心机制（AbortPolicy）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 源码

---

**Qconcurrency-212（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「默认策略是静默丢弃」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原因是：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 源码）。

---

**Qconcurrency-213（原理深挖·P5-P7）**
【面试官】「AbortPolicy」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理。落到结论：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。
【评分点】① 讲出拒绝策略层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-214（工程落地·P7-P9）**
【面试官】在你带过的项目里，「AbortPolicy」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：重要任务用 CallerRuns 降速反压。事实依据：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException常见误区要规避：默认策略是静默丢弃。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-215（结论依据·P8-P10）**
【面试官】关于「AbortPolicy」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 源码。事实与结论：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-216（边界追问·P6-P9）**
【面试官】「AbortPolicy」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「默认策略是静默丢弃」是常见误区。正确的边界：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。使用要点：重要任务用 CallerRuns 降速反压。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-217（追问链·P5-P8）**
【面试官】追问：如果有人按「默认策略是调用者执行」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：ThreadPoolExecutor 默认拒绝策略是 AbortPolicy 即抛 RejectedExecutionException。原理：四种策略：Abort 抛异常、CallerRuns 由提交线程执行、Discard 静默丢弃、DiscardOldest 丢队首再提交，默认抛异常逼迫调用方处理。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
