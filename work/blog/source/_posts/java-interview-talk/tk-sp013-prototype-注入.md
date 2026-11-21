---
title: "[话术SP-013] IoC·prototype 注入（误用）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## IoC · prototype 注入（误用）—— 7 类问法与标准话术

**Qspring-85（概念考察·P6-P8）**
【面试官】请谈谈你对「IoC」中「prototype 注入」的理解。
【标准回答话术】singleton 中注入 prototype Bean 只注入一次失去多例语义。背后的原理是：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取。
【评分点】① 准确说出核心机制（prototype 注入）；② 能带出原理层而非背结论。 ③ 版本锚点：经典陷阱

---

**Qspring-86（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「Spring 会自动按需创建新 prototype」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：singleton 中注入 prototype Bean 只注入一次失去多例语义。原因是：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（经典陷阱）。

---

**Qspring-87（原理深挖·P5-P7）**
【面试官】「prototype 注入」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取。落到结论：singleton 中注入 prototype Bean 只注入一次失去多例语义。
【评分点】① 讲出误用层面的机制；② 结论与机制对应不脱节。

---

**Qspring-88（工程落地·P7-P9）**
【面试官】在你带过的项目里，「prototype 注入」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：每次需要新实例用 ObjectProvider.getBean。事实依据：singleton 中注入 prototype Bean 只注入一次失去多例语义常见误区要规避：Spring 会自动按需创建新 prototype。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-89（结论依据·P8-P10）**
【面试官】关于「prototype 注入」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：经典陷阱。事实与结论：singleton 中注入 prototype Bean 只注入一次失去多例语义。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-90（边界追问·P6-P9）**
【面试官】「prototype 注入」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「Spring 会自动按需创建新 prototype」是常见误区。正确的边界：singleton 中注入 prototype Bean 只注入一次失去多例语义。使用要点：每次需要新实例用 ObjectProvider.getBean。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-91（追问链·P5-P8）**
【面试官】追问：如果有人按「注入后每次调用返回新实例」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：singleton 中注入 prototype Bean 只注入一次失去多例语义。原理：注入发生在 singleton 初始化时只执行一次，之后每次请求 singleton 用的都是同一份 prototype 实例，需 ObjectProvider 延迟获取。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
