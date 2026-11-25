---
title: [ENG-004] 什么是幽灵依赖 phantom dependencies？如何治理？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-004：什么是幽灵依赖 phantom dependencies？如何治理？
**答**：
- 幽灵依赖：代码 import 了未声明在 package.json 里的包，只因扁平化安装让它恰好存在。
- 上游包某天不再传递依赖它，项目就莫名其妙构建失败，属于隐性脆弱点。
- pnpm 默认隔离直接暴露这类问题；npm/yarn 项目要靠 lint 规则或 import 检查工具治理。
- 治理动作：显式 add 需要的包，必要时用 pnpm why 排查依赖来源。

```bash
# 查看某个包为什么被安装、谁依赖它
pnpm why lodash

# 把实际使用的包显式声明进 package.json
pnpm add lodash-es

# npm 项目可用 depcheck 扫描未声明依赖
npx depcheck
```
