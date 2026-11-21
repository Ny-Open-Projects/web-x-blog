---
title: "[话术JB-109] 异常·异常分类速查（语法语义）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 异常 · 异常分类速查（语法语义）—— 7 类问法与标准话术

**Qjava-basics-757（概念考察·P4-P6）**
【面试官】请谈谈你对「异常」中「异常分类速查」的理解。
【标准回答话术】高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。背后的原理是：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。
【评分点】① 准确说出核心机制（异常分类速查）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK 文档

---

**Qjava-basics-758（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「浮点数除以零会抛 ArithmeticException。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。原因是：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK 文档）。

---

**Qjava-basics-759（原理深挖·P5-P7）**
【面试官】「异常分类速查」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。落到结论：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。
【评分点】① 讲出语法语义层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-760（工程落地·P7-P9）**
【面试官】在你带过的项目里，「异常分类速查」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：NumberFormat 的 message 通常包含导致失败的字符串——排查入口。事实依据：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。常见误区要规避：浮点数除以零会抛 ArithmeticException。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-761（结论依据·P8-P10）**
【面试官】关于「异常分类速查」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：JDK 文档。事实与结论：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qjava-basics-762（边界追问·P6-P9）**
【面试官】「异常分类速查」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「浮点数除以零会抛 ArithmeticException。」是常见误区。正确的边界：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。使用要点：NumberFormat 的 message 通常包含导致失败的字符串——排查入口。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-763（追问链·P5-P8）**
【面试官】追问：如果有人按「NumberFormatException 属于 Checked 异常。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：高频运行时异常速查：NPE（null 解引用）、ArrayIndexOutOfBounds（越界）、ClassCast（强转）、NumberFormat（字符串转数字失败）、ArithmeticException（整数除零）、IllegalState（状态不符）、IllegalArgument（参数不符）。原理：整数除零抛异常而浮点除零得 Infinity/NaN——IEEE754 规范行为。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
