---
title: "[话术SP-076] MyBatis·@MapperScan（集成）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## MyBatis · @MapperScan（集成）—— 7 类问法与标准话术

**Qspring-526（概念考察·P1-P3）**
【面试官】请谈谈你对「MyBatis」中「@MapperScan」的理解。
【标准回答话术】@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。背后的原理是：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。
【评分点】① 准确说出核心机制（@MapperScan）；② 能带出原理层而非背结论。 ③ 版本锚点：MyBatis-Spring

---

**Qspring-527（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「Mapper 接口由 JDK 反射直接调用」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原因是：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（MyBatis-Spring）。

---

**Qspring-528（原理深挖·P5-P7）**
【面试官】「@MapperScan」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。落到结论：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。
【评分点】① 讲出集成层面的机制；② 结论与机制对应不脱节。

---

**Qspring-529（工程落地·P7-P9）**
【面试官】在你带过的项目里，「@MapperScan」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。补充要点：框架集成扩展点实战案例。常见误区要规避：Mapper 接口由 JDK 反射直接调用。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-530（结论依据·P8-P10）**
【面试官】关于「@MapperScan」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：MyBatis-Spring。事实与结论：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-531（边界追问·P6-P9）**
【面试官】「@MapperScan」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「Mapper 接口由 JDK 反射直接调用」是常见误区。正确的边界：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。使用要点：框架集成扩展点实战案例。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-532（追问链·P5-P8）**
【面试官】追问：如果有人按「@MapperScan 是 BeanPostProcessor 实现」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@MapperScan 通过 MapperScannerRegistrar 动态注册每个 Mapper 的 MapperFactoryBean。原理：每个接口变成 FactoryBean 产出的代理对象（MapperProxy），这就是"接口没有实现类却能注入"的原理。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
