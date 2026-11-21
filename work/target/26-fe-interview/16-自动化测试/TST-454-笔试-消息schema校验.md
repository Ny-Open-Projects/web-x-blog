---
title: [TST-454] 笔试：事件消息的 schema registry 校验（版本兼容）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-454：笔试：事件消息的 schema registry 校验（版本兼容）。
**题目**：registry `{'order.paid': {v1: schema, v2: schema}}`。实现 `validateMessage(topic, body)`：取 body.schemaVersion 对应 schema 校验；无版本默认最新；版本不存在报错并列出可用版本。

```javascript
function validateMessage(registry, topic, body, ajv) {
  const versions = registry[topic];
  if (!versions) throw new Error(`未知 topic: ${topic}`);
  const v = body.schemaVersion ?? Math.max(...Object.keys(versions).map(Number));
  const schema = versions[v];
  if (!schema) throw new Error(`版本不存在: ${topic}@v${v}；可用: ${Object.keys(versions)}`);
  const ok = ajv.validate(schema, body.payload);
  return { ok, errors: ok ? [] : ajv.errors.map(e => `${e.instancePath} ${e.message}`), version: v };
}

```

**评分点**：
- 版本路由（显式版本优先，缺省最新）。
- 校验失败附版本与错误路径。
- 未知版本错误带可用版本清单（可诊断）。
- 未知 topic 明确报错（契约缺口）。
