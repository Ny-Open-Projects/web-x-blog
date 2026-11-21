---
title: "[话术SP-048] 事务·public（失效）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 事务 · public（失效）—— 7 类问法与标准话术

**Qspring-330（概念考察·P1-P3）**
【面试官】请谈谈你对「事务」中「public」的理解。
【标准回答话术】Spring 6.0 之前 @Transactional 只对 public 方法生效。背后的原理是：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效。
【评分点】① 准确说出核心机制（public）；② 能带出原理层而非背结论。 ③ 版本锚点：Spring 6.0 release note

---

**Qspring-331（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「protected 方法事务在所有版本生效」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Spring 6.0 之前 @Transactional 只对 public 方法生效。原因是：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Spring 6.0 release note）。

---

**Qspring-332（原理深挖·P5-P7）**
【面试官】「public」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效。落到结论：Spring 6.0 之前 @Transactional 只对 public 方法生效。
【评分点】① 讲出失效层面的机制；② 结论与机制对应不脱节。

---

**Qspring-333（工程落地·P7-P9）**
【面试官】在你带过的项目里，「public」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：升级 Spring 6 才有非 public 事务支持。事实依据：Spring 6.0 之前 @Transactional 只对 public 方法生效常见误区要规避：protected 方法事务在所有版本生效。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-334（版本演进·P8-P10）**
【面试官】关于「public」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：Spring 6.0 release note。事实层面：Spring 6.0 之前 @Transactional 只对 public 方法生效。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qspring-335（边界追问·P6-P9）**
【面试官】「public」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「protected 方法事务在所有版本生效」是常见误区。正确的边界：Spring 6.0 之前 @Transactional 只对 public 方法生效。使用要点：升级 Spring 6 才有非 public 事务支持。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-336（追问链·P5-P8）**
【面试官】追问：如果有人按「非 public 加注解会启动报错」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Spring 6.0 之前 @Transactional 只对 public 方法生效。原理：事务 AOP 只拦截 public 方法（Spring 6.0 起支持 protected/package-private），非 public 上的注解静默失效。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
