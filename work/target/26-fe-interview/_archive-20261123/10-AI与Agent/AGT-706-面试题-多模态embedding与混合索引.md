---
title: [AGT-706] 图片/图表的向量索引如何组织（描述索引 vs CLIP 跨模态索引的取舍）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-706：图片/图表的向量索引如何组织（描述索引 vs CLIP 跨模态索引的取舍）

**答**：
- 主索引用「描述文本 embedding」：语义可控、与文本检索同空间可统一排序；CLIP 类跨模态索引做补充：用户以图搜图/以图问问题时必要。
- 混合检索策略：文本 query 只走描述索引（够用且快）；query 含图片时（用户贴截图提问）走跨模态索引 + 描述索引双路，融合排序。
- 索引成本权衡：CLIP 索引只对「有检索价值的图」建（流程图/截图/产品图），装饰性图片跳过，省 60%+ 索引成本。

```javascript
async function multimodalSearch(query, { image = null } = {}) {
  const textHits = await vector.search(embedText(query),
    { index: 'desc' });
  if (!image) return rerank(textHits);
  const [clipHits, descHits] = await Promise.all([
    vector.search(embedImage(image), { index: 'clip' }),
    describeAndSearch(image),                      // 图片描述检索
  ]);
  return fuse([textHits, clipHits, descHits],      // 多路融合
    { weights: { desc: 0.5, clip: 0.3, imgDesc: 0.2 } });
}
```

