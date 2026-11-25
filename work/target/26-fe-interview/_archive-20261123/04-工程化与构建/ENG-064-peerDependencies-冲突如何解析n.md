---
title: [ENG-064] peerDependencies 冲突如何解析？npm8+ 的自动安装意味着什么？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-064：peerDependencies 冲突如何解析？npm8+ 的自动安装意味着什么？
**答**：
- peer 依赖表达"我需要宿主提供某个包，且版本要与你兼容"，库作者用它声明对 react/vue 等的兼容范围。
- npm 7+（8 起更完善）会自动安装 peer 依赖，代价是版本不兼容时直接 ERESOLVE 报错而不是警告。
- 处理冲突：宿主升版本满足范围；或库侧放宽范围（^18.0.0 || ^19.0.0）；最后手段才用 overrides 仲裁。
- pnpm 的策略更精细：允许同一 peer 的多个版本共存于不同子树，必要时用 pnpm.overrides 强制对齐。

```json
{
  "name": "@myorg/ui-lib",
  "peerDependencies": {
    "react": "^18.0.0 || ^19.0.0"
  },
  "peerDependenciesMeta": {
    "react": { "optional": false },
    "react-dom": { "optional": true }
  },
  "devDependencies": {
    "react": "^19.0.0"
  }
}
```
