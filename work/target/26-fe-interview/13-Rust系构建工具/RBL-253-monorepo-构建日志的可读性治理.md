---
title: [RBL-253] monorepo 构建日志几十屏怎么治理可读性
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-253：monorepo 构建日志几十屏怎么治理可读性

**答**:
- 分级输出：默认摘要级（每任务一行状态+耗时），失败任务展开完整日志；--verbose 才全量——默认态信息密度匹配「判断构建健康」所需
- 失败优先视图：错误汇总置顶（按任务分组），带「直接跳转文件:行」的路径；重复错误模式折叠（同类 error 只显示首条+计数）
- 日志持久化：完整日志进 CI artifact，摘要里带链接——本地终端体验与线上可追溯兼顾
- 管道友好：JSON 输出模式（--json）供工具消费（PR bot 解析错误生成评论）

```text
摘要模式示例：
  ✓ core#build        3.2s
  ✓ ui#build          5.8s
  ✗ app#build         12.1s   2 errors
      → src/pages/home.tsx:12:5 TS2304 Cannot find name 'x'
      （完整日志: artifacts/app-build.log）
```
