---
title: "[话术JA-171] Spring AI·默认值（builder）· 7 问"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Spring AI · 默认值（builder）—— 7 类问法与标准话术

**Qjava-ai-1191（概念考察·P1-P3）**
【面试官】请谈谈你对「Spring AI」中「默认值」的理解。
【标准回答话术】ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。背后的原理是：公共提示与参数在构建期固定，调用期只传差异部分，是模板分层（全局/会话/请求）的落点。
【评分点】① 准确说出核心机制（默认值）；② 能带出原理层而非背结论。 ③ 版本锚点：Spring AI 1.0 GA

---

**Qjava-ai-1192（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「默认值与调用值不能共存」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。原因是：公共提示与参数在构建期固定，调用期只传差异部分，是模板分层（全局/会话/请求）的落点。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Spring AI 1.0 GA）。

---

**Qjava-ai-1193（原理深挖·P5-P7）**
【面试官】「默认值」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：公共提示与参数在构建期固定，调用期只传差异部分，是模板分层（全局/会话/请求）的落点。落到结论：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。
【评分点】① 讲出builder层面的机制；② 结论与机制对应不脱节。

---

**Qjava-ai-1194（工程落地·P7-P9）**
【面试官】在你带过的项目里，「默认值」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。补充要点：提示词分层装配。常见误区要规避：默认值与调用值不能共存。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-ai-1195（版本演进·P8-P10）**
【面试官】关于「默认值」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：Spring AI 1.0 GA。事实层面：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-ai-1196（边界追问·P6-P9）**
【面试官】「默认值」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「默认值与调用值不能共存」是常见误区。正确的边界：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。使用要点：提示词分层装配。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-ai-1197（追问链·P5-P8）**
【面试官】追问：如果有人按「defaultSystem 会覆盖每次 system」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：ChatClient.Builder 支持预设默认值：defaultSystem/defaultUser/defaultOptions/defaultAdvisors。原理：公共提示与参数在构建期固定，调用期只传差异部分，是模板分层（全局/会话/请求）的落点。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
