---
title: [TST-664] 基于代码变更 diff 的测试用例推荐怎么做？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-664：基于代码变更 diff 的测试用例推荐怎么做？

**答**：
- 结论：把 diff 解析成「改动函数/分支」，用符号相似度 + 历史缺陷关联召回相关用例。
- 两路召回：静态依赖图找直接相关用例，历史 commit→用例映射找间接相关。
- 推荐结果带置信度排序，低置信度不自动跑只提示。
- 追问钩子：新代码没有历史映射，冷启动怎么解决？

```javascript
function recommend(diff, history, graph) {
  const symbols = diff.match(/[A-Za-z_$][\w$]{2,}/g) || [];
  const scored = new Map();
  symbols.forEach(s => {
    (graph[s] || []).forEach(c => scored.set(c, (scored.get(c) || 0) + 2));
    history.filter(h => h.symbols.includes(s))
      .forEach(h => h.cases.forEach(c =>
        scored.set(c, (scored.get(c) || 0) + 1)));
  });
  return [...scored].sort((a, b) => b[1] - a[1]).slice(0, 10)
    .map(([id, score]) => ({ id, score }));
}
```
