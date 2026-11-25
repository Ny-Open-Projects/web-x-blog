---
title: [BAS-118] npm 扁平化和幽灵依赖是怎么回事？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-118：npm 扁平化和幽灵依赖是怎么回事？
**答**：
- npm v3+ 把依赖尽量拍平到 node_modules 顶层，导致 package.json 没声明的包也能 require 到——幽灵依赖。
- 危险：上游某天不再依赖它，你的代码直接崩；pnpm 用符号链接的严格结构天然杜绝幽灵依赖。
- 防御：用到的包显式声明进 package.json，用 depcheck 扫描漏声明的依赖。

```bash
npm ls --all | head   # 查看依赖树结构
npx depcheck          # 找出未声明或未使用的依赖
# 即使顶层能直接找到，也要显式 npm i <pkg> 声明
```
