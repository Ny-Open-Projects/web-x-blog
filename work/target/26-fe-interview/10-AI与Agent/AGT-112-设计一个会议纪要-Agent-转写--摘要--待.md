---
title: [AGT-112] 设计一个会议纪要 Agent（转写 → 摘要 → 待办提取）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-112：设计一个会议纪要 Agent（转写 → 摘要 → 待办提取）？
**答**：
- 链路：ASR 转写文本 → 文本规整（口语词/重复/错别字）→ 分段摘要（map）→ 汇总纪要（reduce：决议/讨论/风险）→ 待办提取（schema 化）。
- 分段摘要再汇总优于整段直塞：超长会议既省 token 又不丢中间细节；说话人信息要保留，待办归属依赖它。
- 待办结构化且可执行：事项/负责人/截止时间对接任务系统；字段缺失标注「待确认」而不是猜。
- 输出三件套给用户确认：纪要全文、待办清单、可编辑后一键同步任务系统。

```typescript
import { z } from 'zod';

// 会议纪要：分段摘要 → 汇总 → 待办提取
const ActionItemSchema = z.object({
  task: z.string(),
  owner: z.string().nullable(),     // 缺失置 null，不猜
  due: z.string().nullable(),
  status: z.enum(['明确', '待确认']),
});

export async function meetingMinutes(transcript: string) {
  // 1. 分段摘要（map）：按长度切段，逐段提炼，保留说话人与关键数字
  const segments = splitByToken(transcript, 3000);
  const sectionSummaries = await Promise.all(segments.map((s) =>
    chatOnce([{ role: 'user', content: `提炼该段会议内容要点，保留说话人与关键数字：\n${s}` }]),
  ));
  // 2. 汇总纪要（reduce）
  const minutes = await chatOnce([
    { role: 'user', content: `将各段摘要合并成会议纪要，分三节：核心决议 / 讨论要点 / 风险。\n${sectionSummaries.join('\n---\n')}` },
  ]);
  // 3. 待办提取：schema 化，缺失字段标待确认
  const { items } = await structuredLLM(
    [{ role: 'user', content: `从纪要提取待办。负责人或截止时间缺失时对应字段置 null 且 status 为待确认：\n${minutes}` }],
    z.object({ items: z.array(ActionItemSchema) }),
  );
  return { minutes, actionItems: items }; // items 可同步到任务系统
}
```
