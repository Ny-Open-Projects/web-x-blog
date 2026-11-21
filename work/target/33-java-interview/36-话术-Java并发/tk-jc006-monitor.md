---
title: "[话术JC-006] synchronized·monitor（锁机制）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## synchronized · monitor（锁机制）—— 7 类问法与标准话术

**Qconcurrency-36（概念考察·P4-P6）**
【面试官】请谈谈你对「synchronized」中「monitor」的理解。
【标准回答话术】synchronized 基于对象头的 monitor 机制实现互斥与可见性。背后的原理是：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。
【评分点】① 准确说出核心机制（monitor）；② 能带出原理层而非背结论。 ③ 版本锚点：JLS 17.x

---

**Qconcurrency-37（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「synchronized 只保证互斥不保证可见性」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原因是：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JLS 17.x）。

---

**Qconcurrency-38（原理深挖·P5-P7）**
【面试官】「monitor」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。落到结论：synchronized 基于对象头的 monitor 机制实现互斥与可见性。
【评分点】① 讲出锁机制层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-39（工程落地·P7-P9）**
【面试官】在你带过的项目里，「monitor」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：互斥与可见性需求同时存在时首选 synchronized。事实依据：synchronized 基于对象头的 monitor 机制实现互斥与可见性常见误区要规避：synchronized 只保证互斥不保证可见性。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-40（版本演进·P8-P10）**
【面试官】关于「monitor」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JLS 17.x。事实层面：synchronized 基于对象头的 monitor 机制实现互斥与可见性。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qconcurrency-41（边界追问·P6-P9）**
【面试官】「monitor」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「synchronized 只保证互斥不保证可见性」是常见误区。正确的边界：synchronized 基于对象头的 monitor 机制实现互斥与可见性。使用要点：互斥与可见性需求同时存在时首选 synchronized。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-42（追问链·P5-P8）**
【面试官】追问：如果有人按「synchronized 是 JVM 层完全独立于对象头的机制」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：synchronized 基于对象头的 monitor 机制实现互斥与可见性。原理：字节码层面是 monitorenter 与 monitorexit 指令，进入时 invalidate 缓存、退出时 flush 写，语义与 volatile 写读对应。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
