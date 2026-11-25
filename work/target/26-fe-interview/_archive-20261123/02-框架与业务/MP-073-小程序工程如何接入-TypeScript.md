---
title: [MP-073] 小程序工程如何接入 TypeScript？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-073：小程序工程如何接入 TypeScript？
**答**：
- 开发者工具/Taro/uni-app 均支持 TS：源码 .ts/.tsx 编译到 js；关键是**类型声明**——`miniprogram-api-typings`（wx API）、Taro/uni-app 自带类型。
- 注意：小程序运行时与浏览器差异大，tsconfig target/lib 要贴合（ES2020 内），DOM lib 关闭，用 typings 提供 wx/Page/Component 全局类型。
- Taro 项目 TS 支持最完整（React + TS 是官方推荐组合）。

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "CommonJS",
    "strict": true,
    "lib": ["ES2020"],
    "types": ["miniprogram-api-typings"]
  },
  "include": ["miniprogram/**/*.ts", "typings/**/*.d.ts"]
}
```
