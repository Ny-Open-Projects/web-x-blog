---
title: "[话术JB-076] 语言杂项·随机数（误用）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 语言杂项 · 随机数（误用）—— 7 类问法与标准话术

**Qjava-basics-526（概念考察·P6-P8）**
【面试官】请谈谈你对「语言杂项」中「随机数」的理解。
【标准回答话术】Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。背后的原理是：ThreadLocalRandom 为每个线程维护独立种子。
【评分点】① 准确说出核心机制（随机数）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 7+（ThreadLocalRandom 推荐）

---

**Qjava-basics-527（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「Random 是线程安全的且并发无性能损失。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。原因是：ThreadLocalRandom 为每个线程维护独立种子。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 7+（ThreadLocalRandom 推荐））。

---

**Qjava-basics-528（原理深挖·P5-P7）**
【面试官】「随机数」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：ThreadLocalRandom 为每个线程维护独立种子。落到结论：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。
【评分点】① 讲出误用层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-529（工程落地·P7-P9）**
【面试官】在你带过的项目里，「随机数」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Random 用相同种子则序列可复现——测试可复现性的技巧。事实依据：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。常见误区要规避：Random 是线程安全的且并发无性能损失。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-530（版本演进·P8-P10）**
【面试官】关于「随机数」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JDK 7+（ThreadLocalRandom 推荐）。事实层面：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-basics-531（边界追问·P6-P9）**
【面试官】「随机数」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「Random 是线程安全的且并发无性能损失。」是常见误区。正确的边界：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。使用要点：Random 用相同种子则序列可复现——测试可复现性的技巧。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-532（追问链·P5-P8）**
【面试官】追问：如果有人按「ThreadLocalRandom 需要手动创建和传递实例。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Random 实例被多线程共享时 CAS 竞争导致性能下降，并发场景用 ThreadLocalRandom.current()。原理：ThreadLocalRandom 为每个线程维护独立种子。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
