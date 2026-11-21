---
title: [NODE-150] 配置中心的推拉结合、版本与回滚怎么设计（nacos/apollo 思想）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-150：配置中心的推拉结合、版本与回滚怎么设计（nacos/apollo 思想）？
**答**：
- 推拉结合：**长轮询** = 拉的成本 + 推的实时性——客户端带已知版本挂 30s，版本一变立即返回，否则 304 后立刻发起下一轮。
- 版本化：每次发布生成**不可变快照**追加历史，当前版本是指针；回滚 = 指针指回旧版本，数据不动，秒级完成。
- 客户端三原则：本地 last-good 快照兜底（配置中心挂了用旧值）、收到变更先过 schema 校验再热更（NODE-089/155）、灰度发布配置本身（先推 10% 实例观察）。
- 治理：发布带审计（谁/何时/备注）、敏感项加密存储、环境隔离（dev/staging/prod 物理隔离）。

```javascript
// 服务端核心：版本化 + 长轮询 + 回滚
const history = new Map(); // key → [{ version, data, operator, ts, comment }]
const current = new Map(); // key → version

// 读：拉当前版本快照
app.get('/configs/:key', (ctx) => {
  const list = history.get(ctx.params.key) ?? [];
  ctx.body = list.find((v) => v.version === current.get(ctx.params.key)) ?? null;
});

// 长轮询：版本一变立即返回，实时性≈推
app.get('/configs/:key/watch', async (ctx) => {
  const known = Number(ctx.query.version ?? 0);
  const deadline = Date.now() + 30_000;
  while (Date.now() < deadline) {
    if ((current.get(ctx.params.key) ?? 0) !== known) {
      ctx.body = { version: current.get(ctx.params.key) };
      return;
    }
    await new Promise((r) => setTimeout(r, 500));
  }
  ctx.status = 304; // 超时未变，客户端立即发起下一轮
});

// 发布：不可变新版本 + 指针前移
app.post('/configs/:key/publish', auth('config:write'), async (ctx) => {
  const list = history.get(ctx.params.key) ?? [];
  const version = (list.at(-1)?.version ?? 0) + 1;
  list.push({ version, data: ctx.request.body, operator: ctx.state.uid,
    ts: Date.now(), comment: ctx.request.body.comment });
  history.set(ctx.params.key, list);
  current.set(ctx.params.key, version);
  auditLog.info({ key: ctx.params.key, version, by: ctx.state.uid });
  ctx.body = { version };
});

// 回滚：指针指回旧版本，秒级生效
app.post('/configs/:key/rollback', auth('config:write'), async (ctx) => {
  const list = (history.get(ctx.params.key) ?? []).slice();
  const target = ctx.body?.version ? list.find((v) => v.version === ctx.body.version) : list.at(-2);
  current.set(ctx.params.key, target.version);
  auditLog.info({ rollback: true, key: ctx.params.key, to: target.version });
  ctx.body = { version: target.version };
});
```
