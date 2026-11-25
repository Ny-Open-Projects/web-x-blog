---
title: [NODE-209] Node 22 的 process 与 util 新 API？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-209：Node 22 的 process 与 util 新 API？
**答**：
- process.features：运行时能力探测（typescript/inspector 等），脚本按能力分支。
- util.parseArgs 增强：长选项默认值/strict 配置，CLI 开发少写解析器（NODE-198 CLI 链）。
- util.styleText：终端着色 API（ANSI 封装），CLI 输出不再手写 escape 序列。
- 事件循环观测增强：performance.eventLoopUtilization（20 起逐步强化）在 22 里做健康检查更稳（NODE-28x 集群健康探针用）。
- 追问钩子：这些小 API 的面试价值在"知道 Node 版本差异"，答出升级评估视角即可。

```javascript
// 能力探测 + CLI 着色
if (!process.features.typescript) console.warn('TS 支持未开启，.ts 路由需预构建');
import { styleText } from 'node:util';
console.log(styleText('green', '✔ migration done'));
console.log(styleText(['bold', 'red'], 'ERROR'));
// util.parseArgs
const { values } = util.parseArgs({
  options: { out: { type: 'string', default: './dist' }, watch: { type: 'boolean', default: false } },
});
// 健康检查（事件循环饱和度）
import { eventLoopUtilization } from 'node:perf_hooks';
app.get('/health', (req, res) => {
  const elu = eventLoopUtilization();
  res.json({ elu: elu.utilization, mem: process.memoryUsage().rss });
});
```
