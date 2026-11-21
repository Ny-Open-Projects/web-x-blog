---
title: "[话术RD-076] 运维·OOM（故障）· 7 问"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 运维 · OOM（故障）—— 7 类问法与标准话术

**Qredis-526（概念考察·P1-P3）**
【面试官】请谈谈你对「运维」中「OOM」的理解。
【标准回答话术】Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。背后的原理是：先看淘汰策略是否误配 noeviction，再查大 key/碎片/持久化缓冲，扩容（加内存/分片）与治理并行。
【评分点】① 准确说出核心机制（OOM）；② 能带出原理层而非背结论。 ③ 版本锚点：实战共识

---

**Qredis-527（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「报错说明 Redis 坏了」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。原因是：先看淘汰策略是否误配 noeviction，再查大 key/碎片/持久化缓冲，扩容（加内存/分片）与治理并行。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（实战共识）。

---

**Qredis-528（原理深挖·P5-P7）**
【面试官】「OOM」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：先看淘汰策略是否误配 noeviction，再查大 key/碎片/持久化缓冲，扩容（加内存/分片）与治理并行。落到结论：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。
【评分点】① 讲出故障层面的机制；② 结论与机制对应不脱节。

---

**Qredis-529（工程落地·P7-P9）**
【面试官】在你带过的项目里，「OOM」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。补充要点：线上故障应急。常见误区要规避：报错说明 Redis 坏了。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qredis-530（结论依据·P8-P10）**
【面试官】关于「OOM」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：实战共识。事实与结论：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qredis-531（边界追问·P6-P9）**
【面试官】「OOM」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「报错说明 Redis 坏了」是常见误区。正确的边界：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。使用要点：线上故障应急。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qredis-532（追问链·P5-P8）**
【面试官】追问：如果有人按「删数据是唯一解」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Redis 写入报 OOM command not allowed：内存到 maxmemory 且策略是 noeviction。原理：先看淘汰策略是否误配 noeviction，再查大 key/碎片/持久化缓冲，扩容（加内存/分片）与治理并行。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
