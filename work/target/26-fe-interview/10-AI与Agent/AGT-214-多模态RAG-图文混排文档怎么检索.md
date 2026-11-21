---
title: [AGT-214] 多模态 RAG——图文混排文档（PDF 里的图表）怎么检索？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-214：PDF 里的图表/流程图怎么进 RAG——多模态检索怎么设计？

**答**:
- 图表是纯文本解析的盲区：OCR 抽不出图表里的趋势与对比关系，"第三季度为什么下滑"的证据往往在图里——多模态 RAG 的核心是把图变成可检索可用的知识。
- 主流方案：图表描述入库（用多模态模型给每张图生成详细描述+关键数据点，以文本形式索引，检索命中后把原图+描述一起给生成模型）、多模态 embedding（CLIP 类直接对图向量检索）、VLM 直接问答（把页面截图给视觉模型，成本高但细节强）——生产常用"描述入库"为主。
- 版面关联：图与其上下文段落、所属章节必须绑定存元数据，检索命中图时同时带上"图所在段落"，否则图表脱离语境无法解读。
- 成本结构：描述生成是一次性索引成本；生成阶段把原图喂 VLM 的 token 成本高，用"描述优先、原图按需"策略控制。

```javascript
async function indexDocument(pdf) {
  const { text, images } = await parsePDF(pdf);
  for (const img of images) {
    const desc = await vlm(`详细描述这张图：类型、
      关键数据点、趋势结论。`, img);
    await index({ type: 'image', desc, imageRef: img.id,
                  section: img.section,           // 版面关联
                  surrounding: img.nearbyText }); // 邻近段落
  }
  // 检索命中 image 块 → 返回 desc + 原图引用
  // 生成阶段：需要细节时再让 VLM 看原图
}
```
