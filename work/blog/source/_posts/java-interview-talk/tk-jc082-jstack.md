---
title: "[话术JC-082] 死锁·jstack（排查）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 死锁 · jstack（排查）—— 7 类问法与标准话术

**Qconcurrency-568（概念考察·P6-P8）**
【面试官】请谈谈你对「死锁」中「jstack」的理解。
【标准回答话术】jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。背后的原理是：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测。
【评分点】① 准确说出核心机制（jstack）；② 能带出原理层而非背结论。 ③ 版本锚点：工具文档

---

**Qconcurrency-569（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「死锁需要人工分析才能发现」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原因是：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（工具文档）。

---

**Qconcurrency-570（原理深挖·P5-P7）**
【面试官】「jstack」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测。落到结论：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。
【评分点】① 讲出排查层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-571（工程落地·P7-P9）**
【面试官】在你带过的项目里，「jstack」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：生产 dump 排查第一入口。事实依据：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁常见误区要规避：死锁需要人工分析才能发现。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-572（结论依据·P8-P10）**
【面试官】关于「jstack」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：工具文档。事实与结论：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qconcurrency-573（边界追问·P6-P9）**
【面试官】「jstack」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「死锁需要人工分析才能发现」是常见误区。正确的边界：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。使用要点：生产 dump 排查第一入口。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-574（追问链·P5-P8）**
【面试官】追问：如果有人按「jstack 无法检测 ReentrantLock 死锁」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：jstack 输出末尾直接报告 Java-level deadlock 及涉及的锁。原理：JVM 自动检测 monitor 与 JUC 锁的死锁，Arthas thread -b 一条命令定位死锁源头，ThreadMXBean.findDeadlockedThreads 可编程检测。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
