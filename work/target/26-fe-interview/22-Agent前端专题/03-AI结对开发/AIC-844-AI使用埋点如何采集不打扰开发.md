---
title: [AIC-844] AI 使用数据的埋点怎么采集，才能不打扰开发又够用？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-844：AI 使用数据的埋点怎么采集，才能不打扰开发又够用？
**答**：
- 原则：**采集服务端事件而非要求手动填报**。从 IDE 插件、LLM 网关、CI 系统自动采集「建议-接受-拒绝-修改-提交」事件流，开发者零操作；任何需要「开发者点一下上报」的方案都会因麻烦而数据缺失。
- 采集最小化：只采行为元数据（时间、事件类型、文件类型、模型版本、采纳结果），**不采 prompt 正文和代码内容**——除非脱敏且有明确授权。这既是隐私合规要求，也降低开发者的被监视感。
- 采样与聚合：高频事件（每次补全）可采样，关键事件（接受、回滚）全采；客户端先聚合再上报，减少网络与性能开销。
- 透明与信任：向团队公开「采什么、不采什么、数据用来做什么」，并声明**个人数据不用于绩效考核**——否则会引发抵触甚至刻意规避（刷数据/关掉插件）。
- 追问钩子：能说出「明确不采 prompt 正文 + 个人数据不用于考核」的候选人，理解数据采集的信任基础，而不只是技术上能不能采。

```typescript
type AIEvent = {
  type: 'suggestion' | 'accept' | 'reject' | 'modify' | 'revert';
  ts: number; fileExt: string; modelVersion: string;
  sessionId: string; // 匿名会话，不绑定真人姓名
};

// 隐私优先的埋点：只采元数据，绝不采 prompt / 代码正文
function track(type: AIEvent['type'], ctx: { fileExt: string; model: string; session: string }) {
  if (type === 'suggestion' && Math.random() > 0.2) return; // 高频补全采样 20%
  const event: AIEvent = {
    type, ts: Date.now(), fileExt: ctx.fileExt,
    modelVersion: ctx.model, sessionId: ctx.session,
  };
  // 批量聚合后上报，避免每个事件一次请求
  buffer.push(event);
  if (buffer.length >= 50) flush();
}
const buffer: AIEvent[] = [];
function flush() { /* sendBeacon('/telemetry', buffer); buffer.length = 0; */ }

track('accept', { fileExt: 'tsx', model: 'v2', session: 'anon-9f3' });
// 关键事件（accept/revert）全采，补全类采样，且不含任何代码内容
```
