---
title: "[话术JB-100] String·UTF16与码点（语法语义）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## String · UTF16与码点（语法语义）—— 7 类问法与标准话术

**Qjava-basics-694（概念考察·P4-P6）**
【面试官】请谈谈你对「String」中「UTF16与码点」的理解。
【标准回答话术】Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。背后的原理是：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。
【评分点】① 准确说出核心机制（UTF16与码点）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 9+（Compact Strings）

---

**Qjava-basics-695（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「length() 对任何字符串都等于"可见字符数"。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。原因是：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 9+（Compact Strings））。

---

**Qjava-basics-696（原理深挖·P5-P7）**
【面试官】「UTF16与码点」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。落到结论：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。
【评分点】① 讲出语法语义层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-697（工程落地·P7-P9）**
【面试官】在你带过的项目里，「UTF16与码点」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：涉及 emoji 的截断必须按码点边界，否则产生非法字符。事实依据：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。常见误区要规避：length() 对任何字符串都等于"可见字符数"。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-698（版本演进·P8-P10）**
【面试官】关于「UTF16与码点」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JDK 9+（Compact Strings）。事实层面：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-basics-699（边界追问·P6-P9）**
【面试官】「UTF16与码点」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「length() 对任何字符串都等于"可见字符数"。」是常见误区。正确的边界：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。使用要点：涉及 emoji 的截断必须按码点边界，否则产生非法字符。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-700（追问链·P5-P8）**
【面试官】追问：如果有人按「emoji 的 length() 是 1。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Java 用 UTF-16 编码字符串：BMP 内字符 1 个 char，增补字符（如 emoji）占 2 个 char（代理对）。原理：length()/charAt 以代码单元为单位；码点操作用 codePointAt/codePointCount。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
