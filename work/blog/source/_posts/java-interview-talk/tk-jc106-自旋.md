---
title: "[话术JC-106] 原子类·自旋（getAndIncrement）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 原子类 · 自旋（getAndIncrement）—— 7 类问法与标准话术

**Qconcurrency-736（概念考察·P1-P3）**
【面试官】请谈谈你对「原子类」中「自旋」的理解。
【标准回答话术】AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。背后的原理是：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察。
【评分点】① 准确说出核心机制（自旋）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 源码

---

**Qconcurrency-737（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「getAndIncrement 失败会阻塞等待」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原因是：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 源码）。

---

**Qconcurrency-738（原理深挖·P5-P7）**
【面试官】「自旋」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察。落到结论：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。
【评分点】① 讲出getAndIncrement层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-739（工程落地·P7-P9）**
【面试官】在你带过的项目里，「自旋」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：理解无锁与阻塞的本质区别。事实依据：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）常见误区要规避：getAndIncrement 失败会阻塞等待。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-740（结论依据·P8-P10）**
【面试官】关于「自旋」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 源码。事实与结论：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-741（边界追问·P6-P9）**
【面试官】「自旋」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「getAndIncrement 失败会阻塞等待」是常见误区。正确的边界：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。使用要点：理解无锁与阻塞的本质区别。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-742（追问链·P5-P8）**
【面试官】追问：如果有人按「它内部用了 synchronized」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：AtomicLong.getAndIncrement 失败后自旋重试（do-while CAS）。原理：高竞争下大量自旋浪费 CPU，这是 LongAdder 分段设计的动机，自旋次数可用性能工具观察。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
