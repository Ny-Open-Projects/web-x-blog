---
title: "[话术JB-039] CHM·null拒绝（误用）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## CHM · null拒绝（误用）—— 7 类问法与标准话术

**Qjava-basics-267（概念考察·P6-P8）**
【面试官】请谈谈你对「CHM」中「null拒绝」的理解。
【标准回答话术】ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。背后的原理是：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。
【评分点】① 准确说出核心机制（null拒绝）；② 能带出原理层而非背结论。 ③ 版本锚点：CHM javadoc

---

**Qjava-basics-268（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「CHM 允许一个 null key 与多个 null 值。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。原因是：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（CHM javadoc）。

---

**Qjava-basics-269（原理深挖·P5-P7）**
【面试官】「null拒绝」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。落到结论：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。
【评分点】① 讲出误用层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-270（工程落地·P7-P9）**
【面试官】在你带过的项目里，「null拒绝」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：二义性论证是二面高频考点。事实依据：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。常见误区要规避：CHM 允许一个 null key 与多个 null 值。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-271（结论依据·P8-P10）**
【面试官】关于「null拒绝」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：CHM javadoc。事实与结论：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qjava-basics-272（边界追问·P6-P9）**
【面试官】「null拒绝」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「CHM 允许一个 null key 与多个 null 值。」是常见误区。正确的边界：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。使用要点：二义性论证是二面高频考点。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-273（追问链·P5-P8）**
【面试官】追问：如果有人按「CHM 的 null 处理与 HashMap 完全相同。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：ConcurrentHashMap 的 key 和 value 都不允许 null（put null 会抛 NPE）。原理：并发环境下 get 返回 null 存在"不存在"与"值为 null"的二义性。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
