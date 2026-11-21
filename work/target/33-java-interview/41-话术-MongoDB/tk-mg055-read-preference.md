---
title: "[话术MG-055] 副本集·read preference（读偏好）· 7 问"
date: 2026-11-18
categories: [Java面试, MongoDB]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## 副本集 · read preference（读偏好）—— 7 类问法与标准话术

**Qmongodb-379（概念考察·P1-P3）**
【面试官】请谈谈你对「副本集」中「read preference」的理解。
【标准回答话术】读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。背后的原理是：secondary 分摊读压力但读旧数据（复制延迟），nearest 就近读（跨机房），与 write concern 组合构成一致性与延迟矩阵。
【评分点】① 准确说出核心机制（read preference）；② 能带出原理层而非背结论。 ③ 版本锚点：官方文档

---

**Qmongodb-380（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「读偏好影响写入」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。原因是：secondary 分摊读压力但读旧数据（复制延迟），nearest 就近读（跨机房），与 write concern 组合构成一致性与延迟矩阵。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（官方文档）。

---

**Qmongodb-381（原理深挖·P5-P7）**
【面试官】「read preference」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：secondary 分摊读压力但读旧数据（复制延迟），nearest 就近读（跨机房），与 write concern 组合构成一致性与延迟矩阵。落到结论：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。
【评分点】① 讲出读偏好层面的机制；② 结论与机制对应不脱节。

---

**Qmongodb-382（工程落地·P7-P9）**
【面试官】在你带过的项目里，「read preference」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。补充要点：读写分离策略。常见误区要规避：读偏好影响写入。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qmongodb-383（结论依据·P8-P10）**
【面试官】关于「read preference」，你的结论依据什么出处？回答时怎么限定而不说绝对？
【标准回答话术】来源锚点：官方文档。事实与结论：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。表述时带出处限定（如「以当前版本源码为准」）而非绝对化断言。
【评分点】① 结论可溯源（说出依据类别）；② 表述带限定词不绝对化。

---

**Qmongodb-384（边界追问·P6-P9）**
【面试官】「read preference」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「读偏好影响写入」是常见误区。正确的边界：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。使用要点：读写分离策略。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qmongodb-385（追问链·P5-P8）**
【面试官】追问：如果有人按「secondary 读保证最新」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：读偏好：primary（默认）/primaryPreferred/secondary/secondaryPreferred/nearest。原理：secondary 分摊读压力但读旧数据（复制延迟），nearest 就近读（跨机房），与 write concern 组合构成一致性与延迟矩阵。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
