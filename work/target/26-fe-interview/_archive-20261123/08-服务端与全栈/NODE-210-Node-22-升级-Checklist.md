---
title: [NODE-210] Node 22 升级 Checklist？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-210：Node 22 升级 Checklist？
**答**：
- 依赖兼容：native 模块重编译（node-gyp）、引擎依赖版本（undici/openssl 变更点）、deprecated API 扫描（--pending-deprecation 跑全测试）。
- 行为差异：ESM/CJS 解析（require(esm) 开启后的行为）、AbortSignal 语义、npm 版本。
- 基线对比：autocannon 压测 + 内存曲线（NODE-206），错误率对比；影子流量灰度。
- CI/CD：CI runner node 版本、Docker base image、引擎字段（"engines": { "node": ">=22" }）与 lockfile。
- 回滚预案：镜像多版本并存、发布平台一键切回旧 base。

```yaml
# 升级清单（示例）
steps:
  - scan: 'npx depcheck && node --pending-deprecation --test'   # deprecated API 扫描
  - rebuild: 'npm rebuild'                                      # native 模块
  - bench: { before: 'v20.bench', after: 'v22.bench', gate: 'p95_reg < 5%' }
  - canary: { ratio: 0.05, watch: ['errRate', 'rss', 'elu'] }
  - full: { gate: 'canary 绿色 4h' }
# Dockerfile
# FROM node:22-alpine  ← 多版本并存，回滚改一行
```
