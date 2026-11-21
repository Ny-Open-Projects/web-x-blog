---
title: "[话术JB-005] String·CompactStrings（版本）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## String · CompactStrings（版本）—— 7 类问法与标准话术

**Qjava-basics-29（概念考察·P8-P10）**
【面试官】请谈谈你对「String」中「CompactStrings」的理解。
【标准回答话术】JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。背后的原理是：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。
【评分点】① 准确说出核心机制（CompactStrings）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK9+

---

**Qjava-basics-30（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「JDK9 后 String 内部仍是 char 数组。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。原因是：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK9+）。

---

**Qjava-basics-31（原理深挖·P5-P7）**
【面试官】「CompactStrings」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。落到结论：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
【评分点】① 讲出版本层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-32（工程落地·P7-P9）**
【面试官】在你带过的项目里，「CompactStrings」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。事实依据：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。常见误区要规避：JDK9 后 String 内部仍是 char 数组。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-33（版本演进·P8-P10）**
【面试官】关于「CompactStrings」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JDK9+。事实层面：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-basics-34（边界追问·P6-P9）**
【面试官】「CompactStrings」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「JDK9 后 String 内部仍是 char 数组。」是常见误区。正确的边界：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。使用要点：纯 ASCII 内容大量存储时升级 JDK9+ 有可观内存收益。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-35（追问链·P5-P8）**
【面试官】追问：如果有人按「Compact Strings 改变了 String 不可变的语义。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：JDK9 引入 Compact Strings：String 底层从 char[] 改为 byte[] 加 coder 编码标记。原理：纯拉丁字符存储只需 1 字节每字符，内存占用约省一半。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
