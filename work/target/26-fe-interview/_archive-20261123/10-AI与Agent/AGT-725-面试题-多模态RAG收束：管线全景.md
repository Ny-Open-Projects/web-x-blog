---
title: [AGT-725] 把多模态 RAG 收束成管线全景（入库/检索/生成/引用四段），与纯文本 RAG 的关键差异？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-725：把多模态 RAG 收束成管线全景（入库/检索/生成/引用四段），与纯文本 RAG 的关键差异

**答**：
- 四段全景：入库（版面分析→图文分流→描述/提取→双索引，质量门禁贯穿）；检索（意图路由：文本 query/图片 query/混合 query 三路）；生成（预算分配按模态，优先预提取数据而非重读原图）；引用（跨模态引用卡：图坐标/视频时间戳/表行级，可跳转可核对）。
- 与纯文本 RAG 的三大差异：① 表示层多了「描述/提取」中间产物（质量决定一切）；② 成本结构完全不同（vision 调用贵，缓存是生命线）；③ 引用必须可回溯到视觉区域（页码坐标/时间戳）。
- 落地顺序建议：先文本+图片描述索引（80% 价值），再跨模态索引（20% 场景），最后视频/音频专项。

```javascript
const MM_RAG = {
  ingest: ['layout', 'split', 'describe/extract', 'dual-index', 'qualityGate'],
  retrieve: { routes: ['text', 'image', 'mixed'], fuse: 'weighted' },
  generate: { budget: 'modality-aware', prefer: 'pre-extracted' },
  cite: { image: 'bbox', video: 'timestamp', table: 'rowRef' },
};
function rolloutPlan() {
  return ['text+desc-index(80%)', 'clip-index(20%)', 'video/audio'];
}
```

