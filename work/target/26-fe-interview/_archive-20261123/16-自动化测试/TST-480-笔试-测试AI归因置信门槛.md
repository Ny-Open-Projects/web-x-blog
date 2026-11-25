---
title: [TST-480] 笔试：AI 失败归因的置信门槛路由（采纳/复核/转人）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-480：笔试：AI 失败归因的置信门槛路由（采纳/复核/转人）。
**题目**：AI 归因输出 `{cause, confidence, evidence}`。路由：≥ 0.85 自动标注采纳；0.6-0.85 人工快审；< 0.6 转人工深查。输出路由与快审队列排序。

```javascript
function routeAttribution(results, { adopt = 0.85, review = 0.6 } = {}) {
  const adopted = [], queue = [], human = [];
  for (const r of results) {
    if (r.confidence >= adopt) adopted.push(r);
    else if (r.confidence >= review) queue.push(r);
    else human.push(r);
  }
  queue.sort((a, b) => a.confidence - b.confidence);
  return { adopted, reviewQueue: queue, humanEscalate: human };
}

```

**评分点**：
- 三段阈值路由（边界明确）。
- 快审队列按置信升序（最不确定优先）。
- evidence 随条目透传（审计）。
- 阈值可配置。
