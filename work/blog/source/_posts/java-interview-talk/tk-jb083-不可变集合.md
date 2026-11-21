---
title: "[话术JB-083] 集合通用·不可变集合（语法语义）· 7 问"
date: 2026-11-18
categories: [Java面试, Java语言基础]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 集合通用 · 不可变集合（语法语义）—— 7 类问法与标准话术

**Qjava-basics-575（概念考察·P4-P6）**
【面试官】请谈谈你对「集合通用」中「不可变集合」的理解。
【标准回答话术】JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。背后的原理是：不可变集合是防御性编程与安全发布的标准做法。
【评分点】① 准确说出核心机制（不可变集合）；② 能带出原理层而非背结论。 ③ 版本锚点：JDK9+

---

**Qjava-basics-576（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「List.of 返回的集合可以排序。」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。原因是：不可变集合是防御性编程与安全发布的标准做法。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（JDK9+）。

---

**Qjava-basics-577（原理深挖·P5-P7）**
【面试官】「不可变集合」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：不可变集合是防御性编程与安全发布的标准做法。落到结论：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。
【评分点】① 讲出语法语义层面的机制；② 结论与机制对应不脱节。

---

**Qjava-basics-578（工程落地·P7-P9）**
【面试官】在你带过的项目里，「不可变集合」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：跨方法边界返回不可变集合可防调用方误改。事实依据：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。常见误区要规避：List.of 返回的集合可以排序。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-basics-579（版本演进·P8-P10）**
【面试官】关于「不可变集合」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：JDK9+。事实层面：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-basics-580（边界追问·P6-P9）**
【面试官】「不可变集合」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「List.of 返回的集合可以排序。」是常见误区。正确的边界：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。使用要点：跨方法边界返回不可变集合可防调用方误改。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-basics-581（追问链·P5-P8）**
【面试官】追问：如果有人按「List.of 允许 null 元素。」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：JDK9+ 的 List.of/Set.of/Map.of 创建不可变集合：add/remove 抛 UnsupportedOperationException，不允许 null 元素。原理：不可变集合是防御性编程与安全发布的标准做法。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
