---
title: [BLD-178] 构建知识沉淀：常见坑 wiki 与自动化 FAQ 体系。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-178：构建知识沉淀：常见坑 wiki 与自动化 FAQ 体系。
**答**：
- 沉淀三层：**错误码手册**（构建报错 → 原因 → 修复，结构化 YAML，可被工具消费）、**决策记录 ADR**（为什么选 Rspack/为什么关 CSS CodeSplit，防"考古"与反复横跳）、**FAQ**（高频问题一键可复制的修复命令）。
- 自动化闭环：CI 失败时拿 stderr 匹配错误码手册，直接在 PR 评论修复建议（命中即省一次排查）；命中率低的条目定期清理。
- 组织机制：构建群"值班轮询"收集问题 → 周会评审进 wiki → 季度清理过期内容；wiki 的评价标准不是条数而是"新同学求助率下降"。
- 落点：错误码手册结构化后还能驱动 CI 的自动重试/自动降级（如 OOM 自动加大内存重跑）。

```yaml
# docs/build-errors/errors.yaml：结构化错误码手册（可被机器人消费）
- id: E-BUNDLE-001
  match: "Module not found: Error: Can't resolve"
  cause: 路径大小写、缺扩展名、exports 字段屏蔽、幽灵依赖
  fixes:
    - "pnpm why <pkg> 确认依赖是否真实存在"
    - "检查 tsconfig paths 与 webpack alias 是否同步"
    - "package.json exports 是否漏放行该子路径"
  autohint: true          # CI 失败时自动评论本条
- id: E-MEM-002
  match: "JavaScript heap out of memory"
  cause: Terser/大仓构建内存峰值超限
  fixes:
    - "NODE_OPTIONS=--max-old-space-size=6144 pnpm build"
    - "TerserPlugin parallel: 2 降低并发内存"
  autoRetry:              # CI 自动降级重试
    command: "NODE_OPTIONS=--max-old-space-size=8192 pnpm build"
    maxAttempts: 1
```

```javascript
// scripts/ci-error-assistant.js：构建失败 → 命中手册 → 自动评论
const errors = require('../docs/build-errors/errors.yaml').default ?? require('../docs/build-errors/errors.yaml');
const stderr = process.env.CI_STDERR ?? '';
const hits = errors.filter((e) => stderr.includes(e.match));
if (hits.length) {
  const body = hits.map((h) =>
    `### ${h.id}\n**原因**：${h.cause}\n**修复**：\n${h.fixes.map((f) => `- \`${f}\``).join('\n')}`
  ).join('\n\n');
  execSync(`gh pr comment $PR_NUMBER --body "${body.replace(/"/g, '\\"')}"`);
}
// 值班数据回流：每月统计 hits 命中率，手册按需增删
```

## 二十章 综合实战（BLD-179 ~ BLD-200）
