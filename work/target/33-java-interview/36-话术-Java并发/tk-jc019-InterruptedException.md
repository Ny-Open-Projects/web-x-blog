---
title: "[话术JC-019] 线程基础·InterruptedException（中断）· 7 问"
date: 2026-11-18
categories: [Java面试, Java并发]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 线程基础 · InterruptedException（中断）—— 7 类问法与标准话术

**Qconcurrency-127（概念考察·P1-P3）**
【面试官】请谈谈你对「线程基础」中「InterruptedException」的理解。
【标准回答话术】捕获 InterruptedException 后必须恢复中断标志或继续向上抛。背后的原理是：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）。
【评分点】① 准确说出核心机制（InterruptedException）；② 能带出原理层而非背结论。 ③ 版本锚点：C1.5 手册

---

**Qconcurrency-128（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「catch 后什么都不做是最安全的」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原因是：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（C1.5 手册）。

---

**Qconcurrency-129（原理深挖·P5-P7）**
【面试官】「InterruptedException」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）。落到结论：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。
【评分点】① 讲出中断层面的机制；② 结论与机制对应不脱节。

---

**Qconcurrency-130（工程落地·P7-P9）**
【面试官】在你带过的项目里，「InterruptedException」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：吞异常必须注释说明理由并恢复标志位。事实依据：捕获 InterruptedException 后必须恢复中断标志或继续向上抛常见误区要规避：catch 后什么都不做是最安全的。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qconcurrency-131（版本演进·P8-P10）**
【面试官】关于「InterruptedException」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：C1.5 手册。事实层面：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qconcurrency-132（边界追问·P6-P9）**
【面试官】「InterruptedException」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「catch 后什么都不做是最安全的」是常见误区。正确的边界：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。使用要点：吞异常必须注释说明理由并恢复标志位。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qconcurrency-133（追问链·P5-P8）**
【面试官】追问：如果有人按「InterruptedException 应转为运行时异常直接打日志了事」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：捕获 InterruptedException 后必须恢复中断标志或继续向上抛。原理：异常被吞掉后中断信号丢失，上层无法再感知停止请求，这是阿里手册明确条款（恢复用 Thread.currentThread().interrupt()）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
