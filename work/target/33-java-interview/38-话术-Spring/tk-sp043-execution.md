---
title: "[话术SP-043] AOP·execution（表达式）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## AOP · execution（表达式）—— 7 类问法与标准话术

**Qspring-295（概念考察·P1-P3）**
【面试官】请谈谈你对「AOP」中「execution」的理解。
【标准回答话术】execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。背后的原理是：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配。
【评分点】① 准确说出核心机制（execution）；② 能带出原理层而非背结论。 ③ 版本锚点：AspectJ 语法

---

**Qspring-296（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「execution 只能匹配 public 方法」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原因是：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（AspectJ 语法）。

---

**Qspring-297（原理深挖·P5-P7）**
【面试官】「execution」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配。落到结论：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。
【评分点】① 讲出表达式层面的机制；② 结论与机制对应不脱节。

---

**Qspring-298（工程落地·P7-P9）**
【面试官】在你带过的项目里，「execution」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。补充要点：写切点前先明确匹配范围。常见误区要规避：execution 只能匹配 public 方法。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-299（结论依据·P8-P10）**
【面试官】关于「execution」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：AspectJ 语法。事实与结论：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-300（边界追问·P6-P9）**
【面试官】「execution」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「execution 只能匹配 public 方法」是常见误区。正确的边界：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。使用要点：写切点前先明确匹配范围。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-301（追问链·P5-P8）**
【面试官】追问：如果有人按「(..) 与 (*) 语义相同」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：execution 表达式：修饰符 返回类型 包.类.方法(参数) throws。原理：execution(* com.a.b.service..*.save*(..)) 匹配 service 包下 save 开头方法，.. 是包通配与参数通配。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
