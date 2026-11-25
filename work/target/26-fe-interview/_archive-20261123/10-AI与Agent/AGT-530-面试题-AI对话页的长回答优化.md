---
title: [AGT-530] 超长回答（上万字）的渲染与阅读优化怎么做？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-530：超长回答（上万字）的渲染与阅读优化怎么做

**答**：
- 渲染：长回答分段渲染（按二级标题切块，视口外不渲染），完成后生成大纲目录（锚点导航）固定在侧边；流式期间只渲染尾部窗口。
- 阅读：全文/摘要双模式（先给模型生成的摘要 TL;DR + 关键要点卡，展开看全文）；长表格折叠分页。
- 交互：阅读进度记忆（切走再回来回到原位置）、段内搜索、"只看代码/只看结论"过滤器（按块类型过滤）。

```javascript
function useOutline(answer) {
  const blocks = useMemo(() => parseBlocks(answer), [answer]);
  const headings = blocks.filter(b => b.type === 'heading');
  const outline = headings.map(h => ({ level: h.level, text: h.text,
    anchor: `blk-${h.id}` }));
  return { blocks, outline,
    filter: (t) => blocks.filter(b => t === 'all' || b.type === t) };
}
```

