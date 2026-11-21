---
title: "[话术JC-046] 原子类·LongAdder（性能）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 原子类 · LongAdder（性能）—— 7 类问法与标准话术

**Qconcurrency-316（概念考察·P6-P8）**
【面试官】请谈谈你对「原子类」中「LongAdder」的理解。
【标准回答话术】高竞争计数用 LongAdder 而非 AtomicLong。背后的原理是：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。
【评分点】① 准确说出核心机制（LongAdder）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 文档

---

**Qconcurrency-317（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「LongAdder 在任何场景都快于 AtomicLong」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：高竞争计数用 LongAdder 而非 AtomicLong。原因是：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 文档）。

---

**Qconcurrency-318（原理深挖·P5-P7）**
【面试官】「LongAdder」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。落到结论：高竞争计数用 LongAdder 而非 AtomicLong。
【评分点】① 讲出性能层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-319（工程落地·P7-P9）**
【面试官】在你带过的项目里，「LongAdder」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：纯计数（QPS 统计）用 LongAdder。事实依据：高竞争计数用 LongAdder 而非 AtomicLong常见误区要规避：LongAdder 在任何场景都快于 AtomicLong。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-320（结论依据·P8-P10）**
【面试官】关于「LongAdder」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 文档。事实与结论：高竞争计数用 LongAdder 而非 AtomicLong。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-321（边界追问·P6-P9）**
【面试官】「LongAdder」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「LongAdder 在任何场景都快于 AtomicLong」是常见误区。正确的边界：高竞争计数用 LongAdder 而非 AtomicLong。使用要点：纯计数（QPS 统计）用 LongAdder。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-322（追问链·P5-P8）**
【面试官】追问：如果有人按「LongAdder 的 sum 是精确强一致快照」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：高竞争计数用 LongAdder 而非 AtomicLong。原理：AtomicLong 所有线程 CAS 同一个值自旋严重，LongAdder 分散到 Cell 数组各自累加，sum 时汇总，竞争下吞吐可高一个数量级。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
