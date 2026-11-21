---
title: "[话术JC-087] 协作·park（LockSupport）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 协作 · park（LockSupport）—— 7 类问法与标准话术

**Qconcurrency-603（概念考察·P1-P3）**
【面试官】请谈谈你对「协作」中「park」的理解。
【标准回答话术】LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。背后的原理是：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。
【评分点】① 准确说出核心机制（park）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 源码

---

**Qconcurrency-604（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「unpark 必须在 park 之后调用才有效」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原因是：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 源码）。

---

**Qconcurrency-605（原理深挖·P5-P7）**
【面试官】「park」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。落到结论：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。
【评分点】① 讲出LockSupport层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-606（工程落地·P7-P9）**
【面试官】在你带过的项目里，「park」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。补充要点：自定义同步器时使用。常见误区要规避：unpark 必须在 park 之后调用才有效。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-607（结论依据·P8-P10）**
【面试官】关于「park」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 源码。事实与结论：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-608（边界追问·P6-P9）**
【面试官】「park」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「unpark 必须在 park 之后调用才有效」是常见误区。正确的边界：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。使用要点：自定义同步器时使用。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-609（追问链·P5-P8）**
【面试官】追问：如果有人按「park 会抛 InterruptedException」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：LockSupport.park 与 unpark 是 JUC 阻塞的底层原语。原理：unpark 可先于 park 调用（许可制，最多持有 1 个许可），不抛 InterruptedException 但响应中断返回，AQS 队列挂起全靠它。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
