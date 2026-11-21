---
title: "[话术JC-008] synchronized·Class 对象（锁机制）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## synchronized · Class 对象（锁机制）—— 7 类问法与标准话术

**Qconcurrency-50（概念考察·P4-P6）**
【面试官】请谈谈你对「synchronized」中「Class 对象」的理解。
【标准回答话术】static synchronized 方法锁的是 Class 对象与实例锁互不冲突。背后的原理是：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行。
【评分点】① 准确说出核心机制（Class 对象）；② 能带出原理层而非背结论。 ③ 版本锚点：JLS 8.4.3.6

---

**Qconcurrency-51（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「static synchronized 与实例方法锁同一把锁」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原因是：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JLS 8.4.3.6）。

---

**Qconcurrency-52（原理深挖·P5-P7）**
【面试官】「Class 对象」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行。落到结论：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。
【评分点】① 讲出锁机制层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-53（工程落地·P7-P9）**
【面试官】在你带过的项目里，「Class 对象」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：保护静态状态用 Class 锁或专用锁对象。事实依据：static synchronized 方法锁的是 Class 对象与实例锁互不冲突常见误区要规避：static synchronized 与实例方法锁同一把锁。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-54（版本演进·P8-P10）**
【面试官】关于「Class 对象」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JLS 8.4.3.6。事实层面：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qconcurrency-55（边界追问·P6-P9）**
【面试官】「Class 对象」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「static synchronized 与实例方法锁同一把锁」是常见误区。正确的边界：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。使用要点：保护静态状态用 Class 锁或专用锁对象。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-56（追问链·P5-P8）**
【面试官】追问：如果有人按「Class 锁可以保护实例字段」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：static synchronized 方法锁的是 Class 对象与实例锁互不冲突。原理：类的所有实例共享同一把 Class 锁，静态与实例同步方法可并发执行。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
