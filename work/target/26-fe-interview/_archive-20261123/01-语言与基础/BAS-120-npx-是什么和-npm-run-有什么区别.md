---
title: [BAS-120] npx 是什么？和 npm run 有什么区别？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-120：npx 是什么？和 npm run 有什么区别？
**答**：
- npx 临时执行包的命令：先找本地 node_modules/.bin，没有就临时下载执行（--no-install 可禁止下载），不污染依赖。
- npm run 只能跑 scripts 里声明的命令，npx 可以直接跑任意包的 bin。
- 典型用法：一次性脚手架、用项目内版本而非全局版本执行工具。

```bash
npx create-vite@latest my-app   # 临时下载脚手架并执行
npx tsc --noEmit                # 优先用项目内安装的 tsc 而非全局
npx --no-install jest           # 只用本地已装版本，没有则报错
```

## 十四、综合速答
