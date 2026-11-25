---
title: [ENG-001] npm、yarn、pnpm 的核心区别？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-001：npm、yarn、pnpm 的核心区别？
**答**：
- npm 早期采用嵌套 node_modules 造成依赖地狱，npm 3/yarn 改为扁平化，但带来幽灵依赖问题。
- yarn 1 的贡献是 lockfile 与并行安装，大幅提升安装速度与一致性。
- pnpm 用全局内容寻址 store + 硬链接存储包，node_modules 内用符号链接组织，磁盘省、速度快。
- pnpm 默认严格隔离：只能 import 声明过的依赖，从根源解决幽灵依赖。

```bash
# 三种包管理器常用命令对照
npm install
yarn
pnpm install

npm run dev
yarn dev
pnpm dev

# 查看项目声明的包管理器与版本
grep packageManager package.json
```
