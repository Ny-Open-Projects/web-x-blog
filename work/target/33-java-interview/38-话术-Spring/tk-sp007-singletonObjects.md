---
title: "[话术SP-007] 循环依赖·singletonObjects（三级缓存）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 循环依赖 · singletonObjects（三级缓存）—— 7 类问法与标准话术

**Qspring-43（概念考察·P1-P3）**
【面试官】请谈谈你对「循环依赖」中「singletonObjects」的理解。
【标准回答话术】三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。背后的原理是：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。
【评分点】① 准确说出核心机制（singletonObjects）；② 能带出原理层而非背结论。 ③ 版本锚点：Spring 源码

---

**Qspring-44（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「三级缓存都是存 Bean 实例的」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原因是：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Spring 源码）。

---

**Qspring-45（原理深挖·P5-P7）**
【面试官】「singletonObjects」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。落到结论：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。
【评分点】① 讲出三级缓存层面的机制；② 结论与机制对应不脱节。

---

**Qspring-46（工程落地·P7-P9）**
【面试官】在你带过的项目里，「singletonObjects」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：背三级缓存必背各级名称与职责。事实依据：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂常见误区要规避：三级缓存都是存 Bean 实例的。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-47（结论依据·P8-P10）**
【面试官】关于「singletonObjects」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：Spring 源码。事实与结论：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-48（边界追问·P6-P9）**
【面试官】「singletonObjects」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「三级缓存都是存 Bean 实例的」是常见误区。正确的边界：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。使用要点：背三级缓存必背各级名称与职责。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-49（追问链·P5-P8）**
【面试官】追问：如果有人按「三级缓存顺序是工厂、早期、成品」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：三级缓存：singletonObjects 一级成品、earlySingletonObjects 二级早期引用、singletonFactories 三级工厂。原理：一级放完整 Bean，二级放提前曝光的引用（拿到后升级放入二级并删三级），三级放能生成早期引用的 ObjectFactory。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
