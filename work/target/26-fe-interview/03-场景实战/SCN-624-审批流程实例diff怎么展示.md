---
title: [SCN-624] 两个审批实例/流程版本的对比 diff 怎么展示？
date: 2026-11-21
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-624：审批实例/流程定义 diff 怎么展示？
**答**：
- 三类 diff：表单数据 diff（字段级新旧值对照）、流程定义 diff（节点增删/审批人规则变化）、审批路径 diff（实际走的分支不同）。
- 展示形式：表单 diff 用左右双栏 + 字段级高亮（新增绿/删除红/修改黄）；流程定义 diff 用双图对齐布局（同层节点对齐，差异标记）。
- 语义化映射：diff 不做纯文本比较——字段用 label 而非 name，金额/日期格式化后比较，枚举值翻译；否则 diff 出来一堆 ID 看不懂。
- 使用场景：审计回溯（这单和上一单为什么结论不同）、流程改版评审（新版影响哪些在途）。
- 追问钩子：路径 diff 怎么算——两个实例的节点序列做 LCS，公共路径对齐，差异段标出（走了不同分支的位置）。

```javascript
function pathDiff(pathA, pathB) {
  const lcs = longestCommonSubsequence(pathA, pathB);      // 公共节点序列
  const merged = [];
  let i = 0, j = 0;
  for (const common of lcs) {
    while (i < pathA.length && pathA[i] !== common) merged.push({ side: 'A', node: pathA[i++] });
    while (j < pathB.length && pathB[j] !== common) merged.push({ side: 'B', node: pathB[j++] });
    merged.push({ side: 'both', node: common });
    i++; j++;
  }
  while (i < pathA.length) merged.push({ side: 'A', node: pathA[i++] });
  while (j < pathB.length) merged.push({ side: 'B', node: pathB[j++] });
  return merged;                                   // 差异段 side 标记渲染
}
```
