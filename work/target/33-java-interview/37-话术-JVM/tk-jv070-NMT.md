---
title: "[话术JV-070] 排查·NMT（NMT）· 7 问"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 排查 · NMT（NMT）—— 7 类问法与标准话术

**Qjvm-484（概念考察·P1-P3）**
【面试官】请谈谈你对「排查」中「NMT」的理解。
【标准回答话术】NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。背后的原理是：分类包括 Java Heap、Class、Thread、Code、GC、Internal、Other，把"消失的内存"按项对号，开销约 5%（detail 模式更高）。
【评分点】① 准确说出核心机制（NMT）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 文档

---

**Qjvm-485（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「NMT 默认开启」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。原因是：分类包括 Java Heap、Class、Thread、Code、GC、Internal、Other，把"消失的内存"按项对号，开销约 5%（detail 模式更高）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 文档）。

---

**Qjvm-486（原理深挖·P5-P7）**
【面试官】「NMT」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：分类包括 Java Heap、Class、Thread、Code、GC、Internal、Other，把"消失的内存"按项对号，开销约 5%（detail 模式更高）。落到结论：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。
【评分点】① 讲出NMT层面的机制；② 结论与机制对应不脱节。

---

**Qjvm-487（工程落地·P7-P9）**
【面试官】在你带过的项目里，「NMT」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。补充要点：堆外内存问题第一步。常见误区要规避：NMT 默认开启。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjvm-488（结论依据·P8-P10）**
【面试官】关于「NMT」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 文档。事实与结论：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qjvm-489（边界追问·P6-P9）**
【面试官】「NMT」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「NMT 默认开启」是常见误区。正确的边界：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。使用要点：堆外内存问题第一步。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjvm-490（追问链·P5-P8）**
【面试官】追问：如果有人按「NMT 能精确到对象级别」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：NMT 开启后 jcmd VM.native_memory summary 分项展示内存去向。原理：分类包括 Java Heap、Class、Thread、Code、GC、Internal、Other，把"消失的内存"按项对号，开销约 5%（detail 模式更高）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
