---
title: "[话术RD-035] Cluster·hash tag（限制）· 7 问"
date: 2026-11-18
categories: [Java面试, Redis]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Cluster · hash tag（限制）—— 7 类问法与标准话术

**Qredis-239（概念考察·P1-P3）**
【面试官】请谈谈你对「Cluster」中「hash tag」的理解。
【标准回答话术】Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。背后的原理是：key 含 {} 内相同串则按串计算槽（user:{1001}:a 与 user:{1001}:b 同槽），跨槽命令报 CROSSSLOT 错误。
【评分点】① 准确说出核心机制（hash tag）；② 能带出原理层而非背结论。 ③ 版本锚点：官方文档

---

**Qredis-240（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「Cluster 完全支持 mget（自动聚合，客户端可聚合但底层仍拆分）」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。原因是：key 含 {} 内相同串则按串计算槽（user:{1001}:a 与 user:{1001}:b 同槽），跨槽命令报 CROSSSLOT 错误。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（官方文档）。

---

**Qredis-241（原理深挖·P5-P7）**
【面试官】「hash tag」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：key 含 {} 内相同串则按串计算槽（user:{1001}:a 与 user:{1001}:b 同槽），跨槽命令报 CROSSSLOT 错误。落到结论：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。
【评分点】① 讲出限制层面的机制；② 结论与机制对应不脱节。

---

**Qredis-242（工程落地·P7-P9）**
【面试官】在你带过的项目里，「hash tag」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。补充要点：业务 key 设计规范。常见误区要规避：Cluster 完全支持 mget（自动聚合，客户端可聚合但底层仍拆分）。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qredis-243（结论依据·P8-P10）**
【面试官】关于「hash tag」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：官方文档。事实与结论：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qredis-244（边界追问·P6-P9）**
【面试官】「hash tag」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「Cluster 完全支持 mget（自动聚合，客户端可聚合但底层仍拆分）」是常见误区。正确的边界：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。使用要点：业务 key 设计规范。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qredis-245（追问链·P5-P8）**
【面试官】追问：如果有人按「hash tag 会影响数据均匀」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Cluster 下 mget/mset/事务/Lua 多 key 必须同 slot，hash tag {} 强制同槽。原理：key 含 {} 内相同串则按串计算槽（user:{1001}:a 与 user:{1001}:b 同槽），跨槽命令报 CROSSSLOT 错误。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
