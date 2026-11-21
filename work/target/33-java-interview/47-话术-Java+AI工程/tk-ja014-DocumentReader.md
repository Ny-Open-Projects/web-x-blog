---
title: "[话术JA-014] Spring AI·DocumentReader（ETL）· 7 问"
date: 2026-11-18
categories: [Java面试, Java+AI工程]
tags: [Java面试, 话术卡, 33]
type: 话术卡
disableNunjucks: true
---

## Spring AI · DocumentReader（ETL）—— 7 类问法与标准话术

**Qjava-ai-92（概念考察·P1-P3）**
【面试官】请谈谈你对「Spring AI」中「DocumentReader」的理解。
【标准回答话术】Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。背后的原理是：TokenTextSplitter 把长文档切分为带元数据的 Document 列表，TikaDocumentReader 支持解析 PDF/Word 等格式。
【评分点】① 准确说出核心机制（DocumentReader）；② 能带出原理层而非背结论。 ③ 版本锚点：Spring AI 1.0 GA

---

**Qjava-ai-93（误用纠错·P4-P7）**
【面试官】我在别的团队见过这样的说法：「ETL 三步可以乱序」。你觉得对吗？
【标准回答话术】这个说法不正确。准确的表述是：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。原因是：TokenTextSplitter 把长文档切分为带元数据的 Document 列表，TikaDocumentReader 支持解析 PDF/Word 等格式。
【评分点】① 快速识别误区不顺着说；② 给出正确的版本锚定表述（Spring AI 1.0 GA）。

---

**Qjava-ai-94（原理深挖·P5-P7）**
【面试官】「DocumentReader」为什么会这样设计？背后的机制是什么？
【标准回答话术】机制层面：TokenTextSplitter 把长文档切分为带元数据的 Document 列表，TikaDocumentReader 支持解析 PDF/Word 等格式。落到结论：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。
【评分点】① 讲出ETL层面的机制；② 结论与机制对应不脱节。

---

**Qjava-ai-95（工程落地·P7-P9）**
【面试官】在你带过的项目里，「DocumentReader」你是怎么用的？踩过什么坑？
【标准回答话术】使用要点：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。补充要点：知识入库管道。常见误区要规避：ETL 三步可以乱序。
【评分点】① 给出可落地的要点而非概念；② 主动暴露一个真实踩坑并给出规避方案。

---

**Qjava-ai-96（版本演进·P8-P10）**
【面试官】关于「DocumentReader」，版本上有什么需要特别注意的？
【标准回答话术】版本锚点：Spring AI 1.0 GA。事实层面：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。
【评分点】① 知道机制随版本的变化；② 面试回答带版本限定词（禁绝对化）。

---

**Qjava-ai-97（边界追问·P6-P9）**
【面试官】「DocumentReader」有没有不适用或需要特别小心的边界场景？
【标准回答话术】边界提示：认为「ETL 三步可以乱序」是常见误区。正确的边界：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。使用要点：知识入库管道。
【评分点】① 能说出适用边界而非万金油式回答；② 主动给出规避方式。

---

**Qjava-ai-98（追问链·P5-P8）**
【面试官】追问：如果有人按「DocumentTransformer 负责写入向量库」来实施，会发生什么？
【标准回答话术】该说法不成立，正确机制：Spring AI 的 ETL 管道：DocumentReader 读→DocumentTransformer 切→DocumentWriter 存。原理：TokenTextSplitter 把长文档切分为带元数据的 Document 列表，TikaDocumentReader 支持解析 PDF/Word 等格式。
【评分点】① 能推演错误实施的具体后果；② 用机制解释而非背诵结论。

---
