---
title: [AGT-709] 用户既贴截图又打字提问（例如这个报错怎么解决+错误截图），query 理解与检索怎么做？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-709：用户既贴截图又打字提问（例如这个报错怎么解决+错误截图），query 理解与检索怎么做

**答**：
- 检索前先做「图文联合理解」：vision 先把图片转成结构化描述（错误码/界面文字/元素），与文本 query 融合成「增强 query」再去检索——图片本身不直接做向量检索（截图检索召回差）。
- 路由判断：截图是否是提问核心（报错截图→搜错误码相关文档）还是辅助（"帮我总结这个文档"→直接读图不走检索），意图分类决定管线。
- 消歧：图文信息冲突时（文字说 B 方案图里是 A），显式向用户澄清而不是猜。

```javascript
async function mixedQuery(text, image) {
  const intent = await classify(text, image,
    ['image-is-question', 'image-is-context']);
  if (intent === 'image-is-context')              // 图片即对象：直接读
    return llm.answer(text, { image });
  const imgDesc = await vision(image,
    '提取图中的错误码、界面文字与关键元素');
  const enriched = `${text}\n[图片信息] ${imgDesc}`; // 融合增强query
  return ragPipeline(enriched, { boost: ['errorCode'] });
}
```

