---
title: "[话术AI-083] Agent·GenAI 约定（观测）· 7 问"
date: 2026-11-18
categories: [Java面试, AI应用]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Agent · GenAI 约定（观测）—— 7 类问法与标准话术

**Qai-575（概念考察·P1-P3）**
【面试官】请谈谈你对「Agent」中「GenAI 约定」的理解。
【标准回答话术】OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。背后的原理是：跨框架可对比（LangChain/Spring AI 一套仪表盘），属性含 model/input tokens/cost，与通用 trace 融合（Agent 步骤与 HTTP 调用同链路），是观测标准化方向。
【评分点】① 准确说出核心机制（GenAI 约定）；② 能带出原理层而非背结论。 ③ 版本锚点：2024-2025

---

**Qai-576（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「GenAI 约定是某厂商私有」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。原因是：跨框架可对比（LangChain/Spring AI 一套仪表盘），属性含 model/input tokens/cost，与通用 trace 融合（Agent 步骤与 HTTP 调用同链路），是观测标准化方向。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（2024-2025）。

---

**Qai-577（原理深挖·P5-P7）**
【面试官】「GenAI 约定」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：跨框架可对比（LangChain/Spring AI 一套仪表盘），属性含 model/input tokens/cost，与通用 trace 融合（Agent 步骤与 HTTP 调用同链路），是观测标准化方向。落到结论：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。
【评分点】① 讲出观测层面的机制；② 结论与机制对应不脱节。

---

**Qai-578（工程落地·P7-P9）**
【面试官】在你带过的项目里，「GenAI 约定」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Agent 观测落地（AI-042 实现）。事实依据：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）常见误区要规避：GenAI 约定是某厂商私有。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qai-579（版本演进·P8-P10）**
【面试官】关于「GenAI 约定」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：2024-2025。事实层面：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qai-580（边界追问·P6-P9）**
【面试官】「GenAI 约定」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「GenAI 约定是某厂商私有」是常见误区。正确的边界：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。使用要点：Agent 观测落地（AI-042 实现）。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qai-581（追问链·P5-P8）**
【面试官】追问：如果有人按「只支持 Python」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：OpenTelemetry GenAI 语义约定：统一 LLM 调用的 trace 属性（模型/token/温度）。原理：跨框架可对比（LangChain/Spring AI 一套仪表盘），属性含 model/input tokens/cost，与通用 trace 融合（Agent 步骤与 HTTP 调用同链路），是观测标准化方向。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
