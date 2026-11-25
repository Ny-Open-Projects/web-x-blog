---
title: [1038] 回答里引用图表时，怎么保证图文一致不出错
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, RAG, 多模态]
type: 面试题
---

## 1038：回答里引用图表时，怎么保证图文一致不出错

**答**：
- 图文引用一致性三件事：图与文字说明绑定索引（图 caption 和相邻文本同一 chunk 或强关联）、回答引用图时带「图号 + 出处页码」（可点击回原图）、数值类回答中涉及图表的数字必须 OCR/结构化校验（不能靠模型「看图编数」）。
- 多模态模型的「读图」只在推理阶段用（传原图），检索阶段仍然走文本化索引（caption+OCR）——检索打分必须基于文本才能准。
- 版本陷阱：图表随文档更新换代，索引里图要带版本号，回答时核对「图版本 = 文档版本」，旧图回答新问题就是事故。
- 追问钩子：图表数据模型看错了怎么办？——图表结构化抽取（表格图转 markdown 表）入库，让模型读结构化数据而不是「看图猜」，数值准确率显著提升。

```ts
async function indexFigure(fig, doc) {
  const structured = await extractTable(fig);        // 表格图 -> markdown 表
  const caption = await captionModel(fig);
  index.add({ text: caption + '\n' + (structured || ''),
    meta: { docVer: doc.ver, page: fig.page, figId: fig.id } });
}
function citeFigure(ans, fig, doc) {
  if (fig.meta.docVer !== doc.ver) return dropCitation(ans, fig); // 版本不一致剔除
  return ans;                                        // 引用带图号与页码
}
```
