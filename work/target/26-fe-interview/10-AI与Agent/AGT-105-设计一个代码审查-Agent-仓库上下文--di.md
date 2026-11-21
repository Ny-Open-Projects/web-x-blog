---
title: [AGT-105] 设计一个代码审查 Agent（仓库上下文 + diff 分析 + 评论输出全链路）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-105：设计一个代码审查 Agent（仓库上下文 + diff 分析 + 评论输出全链路）？
**答**：
- 链路：拉取 PR diff → 按 hunk 切块并附周边上下文 → 逐块检索仓库相关代码与规范 → 逐块评审 → 汇总结构化评论写回 PR。
- 只审 diff 及其影响面，不全量扫仓库：上下文装不下也不聚焦；每个 hunk 检索相关文件片段与团队规范作为参考。
- 输出 schema 化：{file, line, severity, comment, suggestion}；severity 分级过滤噪音，nit 聚合进 summary 不单独发评论。
- 防刷屏机制：单 PR 评论上限、同问题去重、issues 为空就不打扰。

```typescript
import { z } from 'zod';

// 代码审查 Agent 主链路
const ReviewSchema = z.object({
  issues: z.array(z.object({
    file: z.string(), line: z.number(),
    severity: z.enum(['blocker', 'warn', 'nit']),
    comment: z.string(), suggestion: z.string().optional(),
  })),
});

export async function reviewPR(prId: string) {
  const { description, hunks } = await gh.getPRDiff(prId); // 每个 hunk 含 file/line/code
  const allIssues: z.infer<typeof ReviewSchema>['issues'] = [];
  for (const hunk of hunks) {
    const related = await retrieveRepoContext(hunk.file, hunk.code); // 向量检索仓库相关代码与规范
    const { issues } = await structuredLLM(
      [{
        role: 'user',
        content: `你是资深前端评审。只评论 diff 中真实存在的问题（bug/安全/性能/规范），没有问题返回空数组。
PR 描述：${description}
相关上下文：${related}
变更（${hunk.file} 第 ${hunk.line} 行附近）：\n${hunk.code}`,
      }],
      ReviewSchema,
    );
    allIssues.push(...issues.map((i) => ({ ...i, file: hunk.file, line: i.line + hunk.line })));
  }
  // 防刷屏：blocker/warn 才发评论，nit 聚合进 summary，总数封顶
  const toPost = allIssues.filter((i) => i.severity !== 'nit').slice(0, 20);
  await gh.postReview(prId, {
    body: `AI Review：共 ${allIssues.length} 个发现，其中 ${toPost.length} 个需要关注`,
    comments: toPost,
  });
  return { total: allIssues.length, posted: toPost.length };
}
```
