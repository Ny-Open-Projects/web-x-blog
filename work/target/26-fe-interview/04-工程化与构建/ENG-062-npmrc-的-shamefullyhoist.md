---
title: [ENG-062] .npmrc 的 shamefully-hoist 该不该开？幽灵依赖如何根治？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-062：.npmrc 的 shamefully-hoist 该不该开？幽灵依赖如何根治？
**答**：
- pnpm 默认严格隔离：代码只能 import 声明过的依赖，幽灵依赖直接报错，这是特性不是 bug。
- shamefully-hoist=true 恢复 npm 扁平化行为，把所有依赖提升到根 node_modules，等于把隔离关掉。
- 折中方案是 public-hoist-pattern：只提升确实存在幽灵引用问题的工具类包（如 eslint 插件）。
- 根治路线：迁移期用 hoist 模式跑通，再逐个 add 显式声明，最后关掉 hoist 让 lint 兜底。

```ini
# .npmrc
; 默认严格隔离：只允许 import package.json 声明过的依赖
shamefully-hoist=false

; 折中：只提升有跨目录调用需求的工具包，比如 eslint 插件解析
public-hoist-pattern[]=*eslint*
public-hoist-pattern[]=*prettier*

; 真实生产建议显式声明后保持空提升
; hoist-pattern[]=空数组可进一步收紧 node_modules/.pnpm 外的链接
```
