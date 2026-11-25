---
title: [ENG-319] 笔试题——实现 AI 产物采纳率统计（人工修改 diff 归因）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-319：手写 AI 采纳率统计

**需求与边界**：
- 需求：AI 生成代码块带标记（标记文件 + 生成时间 + prompt 摘要 hash）；后续提交对标记块的 diff 归因——零修改=完全采纳、局部修改=部分采纳（修改行占比）、整体重写=拒绝；按 prompt 类型/文件类型聚合采纳率。
- 边界：① 标记块跨提交跟踪（格式化/重命名不算拒绝——diff 相似度 >0.85 视为等价）；② 部分采纳计算行级 diff；③ 低采纳类型输出改进建议（prompt 模板迭代）。

**答**：
```javascript
function aiAdoptionStats(aiBlocks, commits, { equivalent = 0.85 } = {}) {
  const byType = {};
  for (const block of aiBlocks) {
    const later = commits.filter(c => c.ts > block.ts && touches(c, block.file));
    const finalText = later.length ? latestContent(later, block.file) : block.content;
    const sim = similarity(block.content, finalText);   // 行级相似度
    const outcome = sim >= equivalent ? 'ADOPTED'
      : sim > 0.3 ? 'PARTIAL' : 'REJECTED';
    const type = `${block.promptType}|${ext(block.file)}`;
    byType[type] ??= { total: 0, adopted: 0, partial: 0, rejected: 0 };
    byType[type].total++;
    byType[type][outcome.toLowerCase()]++;
  }
  return Object.entries(byType).map(([type, s]) => ({
    type,
    adoptionRate: s.adopted / s.total,
    partialRate: s.partial / s.total,
    suggest: s.adopted / s.total < 0.3
      ? `prompt 类型 ${block?.promptType ?? type} 采纳率低，迭代模板（附团队规范上下文）` : null,
  }));
}
// 格式化/重命名等价判定：similarity > 0.85 不算拒绝（跨提交跟踪的噪声防御）
```

**评分点**:
- 三态归因（采纳/部分/拒绝）与行级 diff 量化。
- 等价阈值（格式化重命名不算拒绝——跨提交噪声防御）。
- 按 prompt 类型×文件类型聚合（ENG-213 度量落点）。
- 低采纳类型出 prompt 模板迭代建议（闭环）。
