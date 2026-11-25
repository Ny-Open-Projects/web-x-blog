---
title: [TST-211] 多浏览器（Chromium/Firefox/WebKit）矩阵与分布式如何组合？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-211：多浏览器（Chromium/Firefox/WebKit）矩阵与分布式如何组合？
**答**：
- 矩阵维度 = 浏览器 × shard，CI 矩阵展开（每 job 一个浏览器+分片）。
- WebKit 在 Linux 容器有额外依赖，官方镜像已含。
- 按业务分配矩阵：核心流程全浏览器，长尾只 Chromium——控制总时长。
- 报告合并按浏览器分目录，失败按「浏览器×用例」归因。

```javascript
# CI 矩阵：browser × shard
strategy:
  matrix:
    browser: [chromium, firefox, webkit]
    shard: [1, 2, 3, 4]
# command: npx playwright test --project=${{ matrix.browser }} --shard=${{ matrix.shard }}/4
r
```
