---
title: [SCN-376] 文档评论 AI——评论聚合总结与待办提取？
date: 2026-11-20
categories: [场景实战]
tags: [前端面试, 面试题, 场景实战]
type: 面试题
---

## SCN-376：文档评论很多时，AI 总结评论与提取待办怎么实现？

**答**:
- 评论聚合总结：评论量大的文档（百条评论——阅读成本高），AI 总结（按主题聚合评论观点：支持/反对/建议——AGT-212 上下文压缩组装评论集），总结呈现（评论面板顶部摘要卡+原文评论跳转——可溯源到具体评论）。
- 待办提取：评论中行动项识别（"请补充数据"/"下周五前改完"→待办结构化：任务/负责人/时间——AGT-376 评论转任务复用），待办确认（提取结果人工确认后建任务——AI 提取人工拍板）、任务追踪（转任务后状态回显在评论——SCN-346 实体引用联动）。
- 持续性：新评论增量总结（新增评论只总结增量——上下文带旧摘要）、总结更新通知（作者关注文档→新评论摘要推送）。
- 边界：AI 总结的准确性标注（"AI 生成摘要，以原评论为准"）、隐私（评论内容送 AI 的企业开关——SCN-341 权限复用）。

```javascript
async function summarizeComments(docId) {
  const comments = await api.all(docId);
  const digest = await ai.summarize(comments, {
    schema: ['观点倾向', '待办事项', '争议点'],
    incremental: lastDigest,               // 增量：带旧摘要
  });
  renderDigestCard(digest, {
    jumpTo: (ref) => locateComment(ref),   // 溯源跳转
  });
  const todos = digest.todos.filter(t => confirmTodo(t))
    .map(t => createTask(t));              // 确认后建任务
  todos.forEach(t => linkToComment(t));    // 状态回显评论
}
```
