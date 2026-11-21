---
title: "[话术SP-068] Boot·校验（web）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Boot · 校验（web）—— 7 类问法与标准话术

**Qspring-470（概念考察·P1-P3）**
【面试官】请谈谈你对「Boot」中「校验」的理解。
【标准回答话术】@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。背后的原理是：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理。
【评分点】① 准确说出核心机制（校验）；② 能带出原理层而非背结论。 ③ 版本锚点：JSR-380

---

**Qspring-471（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「@Valid 支持@Validated 的分组」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原因是：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JSR-380）。

---

**Qspring-472（原理深挖·P5-P7）**
【面试官】「校验」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理。落到结论：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。
【评分点】① 讲出web层面的机制；② 结论与机制对应不脱节。

---

**Qspring-473（工程落地·P7-P9）**
【面试官】在你带过的项目里，「校验」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：DTO 校验注解+全局异常三件套。事实依据：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）常见误区要规避：@Valid 支持@Validated 的分组。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-474（版本演进·P8-P10）**
【面试官】关于「校验」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JSR-380。事实层面：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qspring-475（边界追问·P6-P9）**
【面试官】「校验」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「@Valid 支持@Validated 的分组」是常见误区。正确的边界：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。使用要点：DTO 校验注解+全局异常三件套。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-476（追问链·P5-P8）**
【面试官】追问：如果有人按「校验在参数绑定前执行」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@Validated/@Valid 触发 JSR-303 校验（Hibernate Validator 实现）。原理：@Valid 支持嵌套级联校验，@Validated 支持分组与类上标注触发方法级校验，校验失败抛 MethodArgumentNotValidException 进全局异常处理。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
