---
title: "[话术SP-063] 异步·失效（@Async）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 异步 · 失效（@Async）—— 7 类问法与标准话术

**Qspring-435（概念考察·P1-P3）**
【面试官】请谈谈你对「异步」中「失效」的理解。
【标准回答话术】@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。背后的原理是：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里。
【评分点】① 准确说出核心机制（失效）；② 能带出原理层而非背结论。 ③ 版本锚点：实战共识

---

**Qspring-436（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「@Async 默认启用无需 @EnableAsync」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原因是：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（实战共识）。

---

**Qspring-437（原理深挖·P5-P7）**
【面试官】「失效」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里。落到结论：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。
【评分点】① 讲出@Async层面的机制；② 结论与机制对应不脱节。

---

**Qspring-438（工程落地·P7-P9）**
【面试官】在你带过的项目里，「失效」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。补充要点：异步任务失效排查三板斧。常见误区要规避：@Async 默认启用无需 @EnableAsync。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-439（结论依据·P8-P10）**
【面试官】关于「失效」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：实战共识。事实与结论：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-440（边界追问·P6-P9）**
【面试官】「失效」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「@Async 默认启用无需 @EnableAsync」是常见误区。正确的边界：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。使用要点：异步任务失效排查三板斧。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-441（追问链·P5-P8）**
【面试官】追问：如果有人按「自调用异步生效」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@Async 失效场景：同类自调用、未加 @EnableAsync、方法非 public。原理：与事务失效同源（代理绕过），@Async 异常对 void 方法进入 AsyncUncaughtExceptionHandler，返回 Future 则留在 Future 里。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
