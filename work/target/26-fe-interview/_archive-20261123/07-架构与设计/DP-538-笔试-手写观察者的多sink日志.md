---
title: [DP-538] 笔试：手写多 sink 日志系统
date: 2026-11-21
categories: [设计模式]
tags: [前端面试, 笔试题, 设计模式]
type: 笔试题
---

## DP-538：笔试：手写日志系统

**题目**：实现日志系统：① 多 sink：console/远程上报/本地存储——同一日志多目的地；② 级别过滤：prod 只 info 以上（debug 零成本关闭）；③ 管道处理：脱敏（手机号正则）→ 采样（info 10%）→ 批量（error 即时）；④ 上下文注入：traceId/路由自动附加（调用方无感知）；⑤ 零开销关断：debug 关闭后调用立即返回（无序列化成本）。写出实现。

```javascript
function createLogger({ level = 'info', sinks, context = () => ({}), sampleRate = 1 }) {
  const LEVELS = { debug: 0, info: 1, warn: 2, error: 3 };
  const PII = /1[3-9]\d{9}|(sk|pk)-[\w-]+/g;
  const sanitize = (s) => String(s).replace(PII, '[REDACTED]');
  function make(lvl) {
    return (...args) => {
      if (LEVELS[lvl] < LEVELS[level]) return;         // 关断: 立即返回
      if (lvl === 'info' && Math.random() > sampleRate) return;   // 采样
      const entry = { level: lvl, msg: args.map(sanitize).join(' '),
        ...context(), t: Date.now() };                 // 上下文注入
      for (const sink of sinks) { try { sink.write(entry); } catch {} }
    };
  }
  return { debug: make('debug'), info: make('info'), warn: make('warn'), error: make('error') };
}
// sinks: [{ write: console.log }, { write: batchReport }, { write: idbStore }]
// error 即时 / info 批量 — sink 内部决定
```

**评分点**：
- 多 sink 同一分发（console/远程/存储）
- 脱敏在管道中（PII 正则——合规）
- 级别关断的零开销（立即 return——无序列化）
- 上下文自动注入（traceId/路由——调用方无感）
