---
title: "[话术JC-017] 线程基础·BLOCKED（线程状态）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 线程基础 · BLOCKED（线程状态）—— 7 类问法与标准话术

**Qconcurrency-113（概念考察·P1-P3）**
【面试官】请谈谈你对「线程基础」中「BLOCKED」的理解。
【标准回答话术】Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。背后的原理是：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。
【评分点】① 准确说出核心机制（BLOCKED）；② 能带出原理层而非背结论。 ③ 版本锚点：Thread.State

---

**Qconcurrency-114（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「RUNNABLE 的线程一定在 CPU 上执行」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原因是：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Thread.State）。

---

**Qconcurrency-115（原理深挖·P5-P7）**
【面试官】「BLOCKED」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。落到结论：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。
【评分点】① 讲出线程状态层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-116（工程落地·P7-P9）**
【面试官】在你带过的项目里，「BLOCKED」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：dump 分析时区分 BLOCKED 与 WAITING 定位问题。事实依据：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同常见误区要规避：RUNNABLE 的线程一定在 CPU 上执行。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-117（结论依据·P8-P10）**
【面试官】关于「BLOCKED」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：Thread.State。事实与结论：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-118（边界追问·P6-P9）**
【面试官】「BLOCKED」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「RUNNABLE 的线程一定在 CPU 上执行」是常见误区。正确的边界：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。使用要点：dump 分析时区分 BLOCKED 与 WAITING 定位问题。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-119（追问链·P5-P8）**
【面试官】追问：如果有人按「BLOCKED 包括等 Condition」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Java 线程有 6 种状态 BLOCKED 与 WAITING 语义不同。原理：BLOCKED 是等 monitor 锁，WAITING 是等 notify、join 或 LockSupport.park，TIMED_WAITING 是限时版。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
