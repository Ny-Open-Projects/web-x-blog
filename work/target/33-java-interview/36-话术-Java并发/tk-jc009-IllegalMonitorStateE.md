---
title: "[话术JC-009] wait/notify·IllegalMonitorStateException（协作机制）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## wait/notify · IllegalMonitorStateException（协作机制）—— 7 类问法与标准话术

**Qconcurrency-57（概念考察·P4-P6）**
【面试官】请谈谈你对「wait/notify」中「IllegalMonitorStateException」的理解。
【标准回答话术】wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。背后的原理是：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。
【评分点】① 准确说出核心机制（IllegalMonitorStateException）；② 能带出原理层而非背结论。 ③ 版本锚点：JLS 17.2

---

**Qconcurrency-58（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「任何线程都可以对任意对象调用 wait」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原因是：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JLS 17.2）。

---

**Qconcurrency-59（原理深挖·P5-P7）**
【面试官】「IllegalMonitorStateException」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。落到结论：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。
【评分点】① 讲出协作机制层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-60（工程落地·P7-P9）**
【面试官】在你带过的项目里，「IllegalMonitorStateException」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：永远在 synchronized(obj) 内配对使用 wait 与 notify。事实依据：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException常见误区要规避：任何线程都可以对任意对象调用 wait。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-61（版本演进·P8-P10）**
【面试官】关于「IllegalMonitorStateException」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JLS 17.2。事实层面：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qconcurrency-62（边界追问·P6-P9）**
【面试官】「IllegalMonitorStateException」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「任何线程都可以对任意对象调用 wait」是常见误区。正确的边界：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。使用要点：永远在 synchronized(obj) 内配对使用 wait 与 notify。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-63（追问链·P5-P8）**
【面试官】追问：如果有人按「在 synchronized 块外调用 wait 只是无效不报错」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：wait 与 notify 必须在持有对象 monitor 时调用否则抛 IllegalMonitorStateException。原理：wait 的语义是释放锁并挂起，不持锁调用则语义不成立，JVM 直接抛异常。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
