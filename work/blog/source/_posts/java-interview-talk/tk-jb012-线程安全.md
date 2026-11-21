---
title: "[话术JB-012] StringBuilder·线程安全（语法语义）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## StringBuilder · 线程安全（语法语义）—— 7 类问法与标准话术

**Qjava-basics-78（概念考察·P4-P6）**
【面试官】请谈谈你对「StringBuilder」中「线程安全」的理解。
【标准回答话术】StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。背后的原理是：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。
【评分点】① 准确说出核心机制（线程安全）；② 能带出原理层而非背结论。 ③ 版本锚点：StringBuilder javadoc（非同步）

---

**Qjava-basics-79（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「StringBuilder 是线程安全的。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。原因是：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（StringBuilder javadoc（非同步））。

---

**Qjava-basics-80（原理深挖·P5-P7）**
【面试官】「线程安全」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。落到结论：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。
【评分点】① 讲出语法语义层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-81（工程落地·P7-P9）**
【面试官】在你带过的项目里，「线程安全」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。事实依据：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。常见误区要规避：StringBuilder 是线程安全的。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-82（结论依据·P8-P10）**
【面试官】关于「线程安全」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：StringBuilder javadoc（非同步）。事实与结论：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qjava-basics-83（边界追问·P6-P9）**
【面试官】「线程安全」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「StringBuilder 是线程安全的。」是常见误区。正确的边界：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。使用要点：方法局部变量拼串用 StringBuilder；极少出现需要共享可变拼串的场景。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-84（追问链·P5-P8）**
【面试官】追问：如果有人按「StringBuffer 在 JDK9 后被废弃。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：StringBuilder 非线程安全，StringBuffer 的主要方法加了 synchronized。原理：StringBuffer 牺牲锁开销换取安全，单线程场景 StringBuilder 更快。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
