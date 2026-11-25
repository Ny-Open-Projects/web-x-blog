---
title: [BAS-119] peerDependencies 装包时会发生什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-119：peerDependencies 装包时会发生什么？
**答**：
- peerDependencies 声明"我需要宿主提供某包"：插件要求宿主装 react，而不是自己再带一份，避免双实例（hooks 报错、context 断裂）。
- npm v7+ 默认自动安装 peer 依赖，v6 要自己装；版本不满足会告警，`--legacy-peer-deps` 可跳过安装。
- 写组件库、eslint 插件时的必看字段。

```json
{
  "name": "my-ui-lib",
  "peerDependencies": {
    "react": ">=18"
  },
  "devDependencies": {
    "react": "^18.3.0"
  }
}
```
