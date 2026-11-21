---
title: "[话术JC-073] 异步·回调线程（CompletableFuture）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 异步 · 回调线程（CompletableFuture）—— 7 类问法与标准话术

**Qconcurrency-505（概念考察·P1-P3）**
【面试官】请谈谈你对「异步」中「回调线程」的理解。
【标准回答话术】CompletableFuture 未指定线程时回调在完成线程或调用线程执行。背后的原理是：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。
【评分点】① 准确说出核心机制（回调线程）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 文档

---

**Qconcurrency-506（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「thenApply 总是在主线程执行」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原因是：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 文档）。

---

**Qconcurrency-507（原理深挖·P5-P7）**
【面试官】「回调线程」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。落到结论：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。
【评分点】① 讲出CompletableFuture层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-508（工程落地·P7-P9）**
【面试官】在你带过的项目里，「回调线程」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：回调线程归属决定线程上下文是否丢失。事实依据：CompletableFuture 未指定线程时回调在完成线程或调用线程执行常见误区要规避：thenApply 总是在主线程执行。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-509（结论依据·P8-P10）**
【面试官】关于「回调线程」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 文档。事实与结论：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-510（边界追问·P6-P9）**
【面试官】「回调线程」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「thenApply 总是在主线程执行」是常见误区。正确的边界：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。使用要点：回调线程归属决定线程上下文是否丢失。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-511（追问链·P5-P8）**
【面试官】追问：如果有人按「所有回调默认在新线程」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：CompletableFuture 未指定线程时回调在完成线程或调用线程执行。原理：thenApply 不带 Async 由完成线程直接执行，thenApplyAsync(fn) 落到 ForkJoinPool.commonPool，IO 回调务必显式指定自定义线程池。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
