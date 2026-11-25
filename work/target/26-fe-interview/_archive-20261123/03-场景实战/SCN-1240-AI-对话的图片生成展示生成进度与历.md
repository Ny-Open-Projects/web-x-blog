---
title: [SCN-1240] AI 对话的图片生成展示（生成进度与历史）
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1240：AI 对话的图片生成展示（生成进度与历史）

**答**：
- 展示：图片生成（进度/多候选图网格/放大查看），失败重试。
- 历史：生成历史（prompt+参数+图）复现（同参数再生成）。
- 合规：生成图水印（AI 生成标识）与敏感内容过滤。

```javascript
// 图片生成
async function imageGen(prompt, { n = 4 } = {}) {
  const r = await api('/image/gen', { prompt, n });
  return {
    candidates: r.images,                              // 多候选网格
    watermark: 'AI 生成标识已嵌入',
    regenerate: () => imageGen(prompt, { n }),
    history: saveGenHistory(prompt, r),
  };
}
function saveGenHistory(p, r) { return r.images.length; }
```
