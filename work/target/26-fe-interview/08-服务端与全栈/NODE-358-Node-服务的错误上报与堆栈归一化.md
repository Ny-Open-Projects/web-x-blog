---
title: [NODE-358] Node 服务的错误上报与堆栈归一化如何做？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-358：Node 服务的错误上报与堆栈归一化
**答**:
- 捕获收口：三个兜底（process.on('uncaughtException') 记录后退出、unhandledRejection 记录并告警——不退出但必须治理、Koa/Express 错误中间件）；Promise 链严格 .catch（lint 规则 no-floating-promises）。
- 堆栈归一化：内部路径转相对（剥离 /app/ 前缀）、node_modules 折叠、压缩后 sourcemap 还原（构建产物 map 归档，与前端同思路）、错误指纹（去行列号 + 消息参数归一化，ARC-406）——指纹聚合才能看趋势。
- 上下文强制：错误上报带 reqId/traceId/uid/路由/参数摘要（白名单脱敏）——没有上下文的错误无法排障。
- 上报通道：Sentry 自建/商用 APM；错误速率与新版发布关联（发布标注，ARC-422）；重复错误去重合并（同指纹 5 分钟窗口聚合计数）。
- 分级：业务预期错误（如校验失败）不进错误监控（是正常流量），只统计指标；真异常才告警。
```javascript
function fingerprint(err) {
  const frames = (err.stack || '').split('\n').slice(1, 4)
    .map(s => s.replace(/:\d+:\d+\)?$/, '').replace(/^.*?node_modules\//, 'nm:').replace(/^.*?\/app\//, ''));
  const norm = (err.message || '').replace(/\d+/g, '?');
  return hash(frames.join('|') + '::' + norm);                   // 指纹聚合
}
process.on('unhandledRejection', (err) => report(err, { type: 'unhandled' }));
```
