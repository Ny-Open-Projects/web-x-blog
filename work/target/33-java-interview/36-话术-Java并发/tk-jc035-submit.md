---
title: "[话术JC-035] 线程池·submit（误用）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 线程池 · submit（误用）—— 7 类问法与标准话术

**Qconcurrency-239（概念考察·P6-P8）**
【面试官】请谈谈你对「线程池」中「submit」的理解。
【标准回答话术】submit 提交的任务抛出的异常被 Future 吞掉不打印。背后的原理是：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默。
【评分点】① 准确说出核心机制（submit）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 源码实测

---

**Qconcurrency-240（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「submit 与 execute 异常行为一致」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：submit 提交的任务抛出的异常被 Future 吞掉不打印。原因是：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 源码实测）。

---

**Qconcurrency-241（原理深挖·P5-P7）**
【面试官】「submit」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默。落到结论：submit 提交的任务抛出的异常被 Future 吞掉不打印。
【评分点】① 讲出误用层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-242（工程落地·P7-P9）**
【面试官】在你带过的项目里，「submit」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：有 get 才用 submit，否则 execute 加 UEH 打日志。事实依据：submit 提交的任务抛出的异常被 Future 吞掉不打印常见误区要规避：submit 与 execute 异常行为一致。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-243（结论依据·P8-P10）**
【面试官】关于「submit」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 源码实测。事实与结论：submit 提交的任务抛出的异常被 Future 吞掉不打印。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-244（边界追问·P6-P9）**
【面试官】「submit」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「submit 与 execute 异常行为一致」是常见误区。正确的边界：submit 提交的任务抛出的异常被 Future 吞掉不打印。使用要点：有 get 才用 submit，否则 execute 加 UEH 打日志。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-245（追问链·P5-P8）**
【面试官】追问：如果有人按「submit 会自动打印堆栈」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：submit 提交的任务抛出的异常被 Future 吞掉不打印。原理：execute 直接走线程的 uncaughtExceptionHandler，submit 把异常包进 Future 只有 get 时才拿到，漏 get 则异常静默。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
