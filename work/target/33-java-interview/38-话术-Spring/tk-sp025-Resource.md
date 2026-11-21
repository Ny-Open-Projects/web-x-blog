---
title: "[话术SP-025] IoC·@Resource（注入）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## IoC · @Resource（注入）—— 7 类问法与标准话术

**Qspring-169（概念考察·P1-P3）**
【面试官】请谈谈你对「IoC」中「@Resource」的理解。
【标准回答话术】@Resource 是 JSR-250 标准默认按名称注入。背后的原理是：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同。
【评分点】① 准确说出核心机制（@Resource）；② 能带出原理层而非背结论。 ③ 版本锚点：JSR-250

---

**Qspring-170（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「@Resource 默认按类型注入」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@Resource 是 JSR-250 标准默认按名称注入。原因是：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JSR-250）。

---

**Qspring-171（原理深挖·P5-P7）**
【面试官】「@Resource」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同。落到结论：@Resource 是 JSR-250 标准默认按名称注入。
【评分点】① 讲出注入层面的机制；② 结论与机制对应不脱节。

---

**Qspring-172（工程落地·P7-P9）**
【面试官】在你带过的项目里，「@Resource」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation。事实依据：@Resource 是 JSR-250 标准默认按名称注入常见误区要规避：@Resource 默认按类型注入。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-173（版本演进·P8-P10）**
【面试官】关于「@Resource」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JSR-250。事实层面：@Resource 是 JSR-250 标准默认按名称注入。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qspring-174（边界追问·P6-P9）**
【面试官】「@Resource」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「@Resource 默认按类型注入」是常见误区。正确的边界：@Resource 是 JSR-250 标准默认按名称注入。使用要点：JDK17+ 移除 javax.annotation 后 Boot 3 需显式依赖 jakarta.annotation。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-175（追问链·P5-P8）**
【面试官】追问：如果有人按「@Resource 是 Spring 的注解」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@Resource 是 JSR-250 标准默认按名称注入。原理：先按名字找找不到再按类型，由 CommonAnnotationBeanPostProcessor 处理，与 @Autowired（Spring 自家 byType）语义不同。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
