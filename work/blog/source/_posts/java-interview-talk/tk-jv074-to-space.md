---
title: "[话术JV-074] GC·to-space（并发失败）· 7 问"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## GC · to-space（并发失败）—— 7 类问法与标准话术

**Qjvm-512（概念考察·P1-P3）**
【面试官】请谈谈你对「GC」中「to-space」的理解。
【标准回答话术】G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。背后的原理是：并发标记期间老年代同时被消耗，晋升失败触发 Full GC，解法：预留空间（-XX:G1ReservePercent 默认 10）、提前并发标记（InitiatingHeapOccupancyPercent）。
【评分点】① 准确说出核心机制（to-space）；② 能带出原理层而非背结论。 ③ 版本锚点：G1 调优

---

**Qjvm-513（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「to-space exhausted 只影响性能无实际危害」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。原因是：并发标记期间老年代同时被消耗，晋升失败触发 Full GC，解法：预留空间（-XX:G1ReservePercent 默认 10）、提前并发标记（InitiatingHeapOccupancyPercent）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（G1 调优）。

---

**Qjvm-514（原理深挖·P5-P7）**
【面试官】「to-space」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：并发标记期间老年代同时被消耗，晋升失败触发 Full GC，解法：预留空间（-XX:G1ReservePercent 默认 10）、提前并发标记（InitiatingHeapOccupancyPercent）。落到结论：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。
【评分点】① 讲出并发失败层面的机制；② 结论与机制对应不脱节。

---

**Qjvm-515（工程落地·P7-P9）**
【面试官】在你带过的项目里，「to-space」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。补充要点：G1 运维告警关键字。常见误区要规避：to-space exhausted 只影响性能无实际危害。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjvm-516（版本演进·P8-P10）**
【面试官】关于「to-space」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：G1 调优。事实层面：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjvm-517（边界追问·P6-P9）**
【面试官】「to-space」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「to-space exhausted 只影响性能无实际危害」是常见误区。正确的边界：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。使用要点：G1 运维告警关键字。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjvm-518（追问链·P5-P8）**
【面试官】追问：如果有人按「G1ReservePercent 默认是 50」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：G1 出现 to-space exhausted 表示晋升时 Survivor/Old Region 不足。原理：并发标记期间老年代同时被消耗，晋升失败触发 Full GC，解法：预留空间（-XX:G1ReservePercent 默认 10）、提前并发标记（InitiatingHeapOccupancyPercent）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
