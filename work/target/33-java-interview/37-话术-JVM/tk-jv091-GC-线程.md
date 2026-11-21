---
title: "[话术JV-091] GC·GC 线程（并发）· 7 问"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## GC · GC 线程（并发）—— 7 类问法与标准话术

**Qjvm-631（概念考察·P1-P3）**
【面试官】请谈谈你对「GC」中「GC 线程」的理解。
【标准回答话术】GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。背后的原理是：ParallelGCThreads 是 STW 阶段并行线程数（默认约 CPU 核数），ConcGCThreads 是并发阶段线程数（默认按比例），容器 CPU 限额影响默认值。
【评分点】① 准确说出核心机制（GC 线程）；② 能带出原理层而非背结论。 ③ 版本锚点：HotSpot

---

**Qjvm-632（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「GC 线程越多吞吐越高无上限」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。原因是：ParallelGCThreads 是 STW 阶段并行线程数（默认约 CPU 核数），ConcGCThreads 是并发阶段线程数（默认按比例），容器 CPU 限额影响默认值。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（HotSpot）。

---

**Qjvm-633（原理深挖·P5-P7）**
【面试官】「GC 线程」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：ParallelGCThreads 是 STW 阶段并行线程数（默认约 CPU 核数），ConcGCThreads 是并发阶段线程数（默认按比例），容器 CPU 限额影响默认值。落到结论：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。
【评分点】① 讲出并发层面的机制；② 结论与机制对应不脱节。

---

**Qjvm-634（工程落地·P7-P9）**
【面试官】在你带过的项目里，「GC 线程」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：容器化 JVM 调参注意 CPU 限额影响默认值。事实依据：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制常见误区要规避：GC 线程越多吞吐越高无上限。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjvm-635（结论依据·P8-P10）**
【面试官】关于「GC 线程」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：HotSpot。事实与结论：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qjvm-636（边界追问·P6-P9）**
【面试官】「GC 线程」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「GC 线程越多吞吐越高无上限」是常见误区。正确的边界：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。使用要点：容器化 JVM 调参注意 CPU 限额影响默认值。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjvm-637（追问链·P5-P8）**
【面试官】追问：如果有人按「GC 与业务线程永不并行」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：GC 线程数由 -XX:ConcGCThreads 与 ParallelGCThreads 控制。原理：ParallelGCThreads 是 STW 阶段并行线程数（默认约 CPU 核数），ConcGCThreads 是并发阶段线程数（默认按比例），容器 CPU 限额影响默认值。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
