---
title: "[话术SP-049] 事务·rollbackFor（回滚）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 事务 · rollbackFor（回滚）—— 7 类问法与标准话术

**Qspring-337（概念考察·P1-P3）**
【面试官】请谈谈你对「事务」中「rollbackFor」的理解。
【标准回答话术】@Transactional 默认只回滚 RuntimeException 与 Error。背后的原理是：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款。
【评分点】① 准确说出核心机制（rollbackFor）；② 能带出原理层而非背结论。 ③ 版本锚点：阿里手册

---

**Qspring-338（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「默认回滚所有异常」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@Transactional 默认只回滚 RuntimeException 与 Error。原因是：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（阿里手册）。

---

**Qspring-339（原理深挖·P5-P7）**
【面试官】「rollbackFor」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款。落到结论：@Transactional 默认只回滚 RuntimeException 与 Error。
【评分点】① 讲出回滚层面的机制；② 结论与机制对应不脱节。

---

**Qspring-340（工程落地·P7-P9）**
【面试官】在你带过的项目里，「rollbackFor」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：事务注解一律显式 rollbackFor。事实依据：@Transactional 默认只回滚 RuntimeException 与 Error常见误区要规避：默认回滚所有异常。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-341（结论依据·P8-P10）**
【面试官】关于「rollbackFor」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：阿里手册。事实与结论：@Transactional 默认只回滚 RuntimeException 与 Error。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-342（边界追问·P6-P9）**
【面试官】「rollbackFor」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「默认回滚所有异常」是常见误区。正确的边界：@Transactional 默认只回滚 RuntimeException 与 Error。使用要点：事务注解一律显式 rollbackFor。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-343（追问链·P5-P8）**
【面试官】追问：如果有人按「默认回滚受检异常」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@Transactional 默认只回滚 RuntimeException 与 Error。原理：受检异常（如 IOException）默认提交，需要 rollbackFor=Exception.class 显式声明，这是手册明确条款。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
