---
title: [PER-1155] 前端如何处理"数据主体请求"（DSAR）的全链路
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1155：前端如何处理"数据主体请求"（DSAR）的全链路

**答**：
- 类型：访问/更正/删除/可携/撤回同意/投诉——统一入口、统一工单、统一 SLA。
- 链路：用户提交 → 身份验证（防冒领）→ 工单路由到各数据系统 → 汇总执行 → 回执 → 审计归档。
- 技术：请求编排服务（orchestrator）向各系统广播任务，收集完成状态；超时升级。
- 前端：进度可视化（各系统完成状态）、结果通知（邮件+站内）。

```javascript
// DSAR 编排器
async function dsar(uid, type) {
  const systems = ['account', 'orders', 'events', 'replay', 'logs'];
  const results = await Promise.all(systems.map(async s => {
    const r = await withTimeout(dispatch(s, { uid: hash(uid), type }), 86400_000)
      .catch(() => ({ status: 'timeout' }));
    return { system: s, status: r.status ?? 'done' };
  }));
  const done = results.every(r => r.status === 'done');
  return { ticket: `dsar-${type}-${Date.now()}`, done, results,
    sla: type === 'erase' ? 30 : 15 };
}
// done=false 时按 system 列出未完成方并升级告警
```
