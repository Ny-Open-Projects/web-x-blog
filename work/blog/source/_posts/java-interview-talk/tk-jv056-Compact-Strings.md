---
title: "[话术JV-056] String·Compact Strings（布局）· 7 问"
date: 2026-11-18
categories: [Java面试, JVM]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## String · Compact Strings（布局）—— 7 类问法与标准话术

**Qjvm-386（概念考察·P1-P3）**
【面试官】请谈谈你对「String」中「Compact Strings」的理解。
【标准回答话术】JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。背后的原理是：纯 Latin-1 字符串内存减半，含中文等多字节字符时退回 UTF-16 存储，是 JDK9 升级的隐形收益之一（本项目有实测断言）。
【评分点】① 准确说出核心机制（Compact Strings）；② 能带出原理层而非背结论。 ③ 版本锚点：JEP 254 实测

---

**Qjvm-387（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「JDK9 的 String 变慢了」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。原因是：纯 Latin-1 字符串内存减半，含中文等多字节字符时退回 UTF-16 存储，是 JDK9 升级的隐形收益之一（本项目有实测断言）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JEP 254 实测）。

---

**Qjvm-388（原理深挖·P5-P7）**
【面试官】「Compact Strings」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：纯 Latin-1 字符串内存减半，含中文等多字节字符时退回 UTF-16 存储，是 JDK9 升级的隐形收益之一（本项目有实测断言）。落到结论：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。
【评分点】① 讲出布局层面的机制；② 结论与机制对应不脱节。

---

**Qjvm-389（工程落地·P7-P9）**
【面试官】在你带过的项目里，「Compact Strings」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：估算字符串内存必须分 JDK8/9+。事实依据：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）常见误区要规避：JDK9 的 String 变慢了。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjvm-390（版本演进·P8-P10）**
【面试官】关于「Compact Strings」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JEP 254 实测。事实层面：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjvm-391（边界追问·P6-P9）**
【面试官】「Compact Strings」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「JDK9 的 String 变慢了」是常见误区。正确的边界：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。使用要点：估算字符串内存必须分 JDK8/9+。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjvm-392（追问链·P5-P8）**
【面试官】追问：如果有人按「Compact Strings 对中文也减半」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：JDK9 起 String 内部从 char[] 改为 byte[]（Compact Strings）。原理：纯 Latin-1 字符串内存减半，含中文等多字节字符时退回 UTF-16 存储，是 JDK9 升级的隐形收益之一（本项目有实测断言）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
