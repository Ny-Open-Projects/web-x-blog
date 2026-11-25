---
title: [AIC-283] AI 生成的代码进入主干后出 bug，如何快速溯源是哪段 AI 产出引入的？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-283：AI 生成的代码进入主干后出 bug，如何快速溯源是哪段 AI 产出引入的？
**答**：
- 生成即打标：AI 产出以 co-author / 元数据标记模型与提示词版本，进 git 记录。
- 代码指纹库：AI 产出片段哈希入库，出问题时可定位生成批次与对应任务上下文。
- 事故归因流程：bug → 定位 commit → 查 AI 标记 → 提取当时提示词与评审记录 → 归因（生成问题/评审漏放/需求误解）。
- 归因结果反哺：三类归因分别对应改进提示词、加严门禁、澄清需求文档。

```javascript
// commit trailer 打标 + 归因查询
// Co-authored-by: cursor-agent <agent@cursor.sh>
// Ai-Task-Id: T-2026-0317-082
function traceIncident(bugCommit: string) {
  const meta = parseTrailers(bugCommit);
  return db.findTask(meta.taskId); // → 提示词版本/评审结论/模型版本 全链路
}
r
```
