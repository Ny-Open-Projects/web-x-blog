---
title: "[话术SP-035] 配置类·lite mode（proxyBeanMethods）· 7 问"
date: 2026-11-18
categories: [Java面试, Spring]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 配置类 · lite mode（proxyBeanMethods）—— 7 类问法与标准话术

**Qspring-239（概念考察·P1-P3）**
【面试官】请谈谈你对「配置类」中「lite mode」的理解。
【标准回答话术】@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。背后的原理是：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）。
【评分点】① 准确说出核心机制（lite mode）；② 能带出原理层而非背结论。 ③ 版本锚点：Boot 文档

---

**Qspring-240（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「lite 模式下 @Bean 互调仍返回单例」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原因是：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Boot 文档）。

---

**Qspring-241（原理深挖·P5-P7）**
【面试官】「lite mode」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）。落到结论：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。
【评分点】① 讲出proxyBeanMethods层面的机制；② 结论与机制对应不脱节。

---

**Qspring-242（工程落地·P7-P9）**
【面试官】在你带过的项目里，「lite mode」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。补充要点：性能敏感的启动优化点。常见误区要规避：lite 模式下 @Bean 互调仍返回单例。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qspring-243（结论依据·P8-P10）**
【面试官】关于「lite mode」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：Boot 文档。事实与结论：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qspring-244（边界追问·P6-P9）**
【面试官】「lite mode」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「lite 模式下 @Bean 互调仍返回单例」是常见误区。正确的边界：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。使用要点：性能敏感的启动优化点。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qspring-245（追问链·P5-P8）**
【面试官】追问：如果有人按「proxyBeanMethods 默认是 false」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：@Configuration(proxyBeanMethods=false) 为 lite 模式 @Bean 方法互调不再走代理。原理：full 模式 CGLIB 拦截 @Bean 调用保证容器内单例，lite 模式直接执行方法体每次 new，启动更快内存更小（Boot 内部大量 lite）。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
