---
title: [1131] 新旧编排器并存过渡期怎么保证任务不乱
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 多Agent, 发布]
type: 面试题
---

## 1131：新旧编排器并存过渡期怎么保证任务不乱

**答**：
- 并存期的三条边界：消息协议兼容（新旧编排器发出的消息互相可解析——共用 schema 或版本字段）、状态 schema 兼容（黑板条目带版本号，旧版读不懂的字段忽略而非报错）、任务粘性（任务从创建到结束由同一版本处理）。
- 过渡期长度由「任务最长时长」决定：并存期 ≥ 最长任务时长 + 缓冲，确保旧版能跑完存量任务再下线。
- 监控重点：并存期的「跨版本交互」事件（旧版收到新版消息）——每个都应被协议兼容层处理并计数，异常即兼容层有 bug。
- 追问钩子：能不能干脆不做并存，停机发布？——Agent 任务分钟级且不可中断（中断即浪费已花成本），停机发布对长任务系统通常是不可接受的，并存是常态需求。

```ts
const envelope = z.object({ v: z.number(), payload: z.unknown() });
function recv(msg) {
  const { v, payload } = envelope.parse(msg);
  if (v < MY_VERSION) return migrate(payload, v);   // 旧消息迁移
  if (v > MY_VERSION) return ignoreUnknownFields(payload); // 新字段忽略
  return payload;
}
// 下线检查：旧版在途任务清零才停
await waitUntil(() => inflight(OLD) === 0, { timeout: '30m' });
```

