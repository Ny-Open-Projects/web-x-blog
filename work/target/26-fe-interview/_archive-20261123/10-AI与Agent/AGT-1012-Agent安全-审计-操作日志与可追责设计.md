---
title: [1012] Agent 操作审计怎么设计才能「事后可追责」
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 审计]
type: 面试题
---

## 1012：Agent 操作审计怎么设计才能「事后可追责」

**答**：
- 审计五要素：谁（agentId + 会话）、为什么（触发它的任务与上下文摘要）、做什么（工具 + 参数全文）、依据（模型当时的理由输出）、结果（成功/失败 + 副作用清单）；五缺一就是事故现场查不清。
- 不可篡改：审计日志追加写 + 哈希链（每条含前条哈希），或写入 WORM 存储；「能改的审计日志」等于没有。
- 审计与审批联动：人工审批记录（谁批的、批的是哪个版本的参数）与执行记录关联，事后能完整重现决策链。
- 追问钩子：审计日志量太大怎么查？——按任务 ID 结构化索引 + 高危操作单独分级存储，事件溯源（按任务聚合的时线视图）优先于全文搜索。

```ts
let prevHash = '0';
function audit(ev) {
  const rec = { ...ev, ts: Date.now(), prev: prevHash,
    hash: sha256(JSON.stringify(ev) + prevHash) };
  prevHash = rec.hash;                  // 哈希链防篡改
  return wormStore.append(rec);         // 一次写入不可改
}
// 追责查询：按任务聚合
const timeline = await wormStore.byTask(taskId); // agent->approval->exec 全链
```
