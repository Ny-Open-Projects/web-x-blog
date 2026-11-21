---
title: "[话术MQ-099] 语义·组合方案（矩阵）· 7 问"
date: 2026-11-18
categories: [Java面试, 消息队列]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 语义 · 组合方案（矩阵）—— 7 类问法与标准话术

**Qmq-687（概念考察·P1-P3）**
【面试官】请谈谈你对「可靠」中「publisher confirm」的理解。
【标准回答话术】RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。背后的原理是：confirm 异步回调确认到达 broker，配合本地消息表/事务消息实现不丢投递，消费端 manual ack。
【评分点】① 准确说出核心机制（publisher confirm）；② 能带出原理层而非背结论。 ③ 版本锚点：官方文档

---

**Qmq-688（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「confirm 默认开启」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。原因是：confirm 异步回调确认到达 broker，配合本地消息表/事务消息实现不丢投递，消费端 manual ack。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（官方文档）。

---

**Qmq-689（原理深挖·P5-P7）**
【面试官】「publisher confirm」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：confirm 异步回调确认到达 broker，配合本地消息表/事务消息实现不丢投递，消费端 manual ack。落到结论：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。
【评分点】① 讲出confirm层面的机制；② 结论与机制对应不脱节。

---

**Qmq-690（工程落地·P7-P9）**
【面试官】在你带过的项目里，「publisher confirm」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。补充要点：投递可靠性配置。常见误区要规避：confirm 默认开启。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qmq-691（结论依据·P8-P10）**
【面试官】关于「publisher confirm」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：官方文档。事实与结论：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qmq-692（边界追问·P6-P9）**
【面试官】「publisher confirm」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「confirm 默认开启」是常见误区。正确的边界：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。使用要点：投递可靠性配置。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qmq-693（追问链·P5-P8）**
【面试官】追问：如果有人按「持久化消息 confirm 就不丢（confirm 只到内存/日志）」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：RabbitMQ 可靠投递：publisher confirm（broker 确认）+mandatory（路由失败退回）+持久化。原理：confirm 异步回调确认到达 broker，配合本地消息表/事务消息实现不丢投递，消费端 manual ack。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
