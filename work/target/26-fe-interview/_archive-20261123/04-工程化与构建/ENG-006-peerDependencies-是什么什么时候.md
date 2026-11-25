---
title: [ENG-006] peerDependencies 是什么？什么时候用？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-006：peerDependencies 是什么？什么时候用？
**答**：
- 表达"我与宿主环境共享某个依赖，由宿主提供"，典型如插件依赖 vite、UI 库依赖 react。
- 避免插件把 react 也装一份导致双实例（hooks 报错、context 断裂的经典事故）。
- peerDependenciesMeta.optional 声明可选 peer；npm 7+ 会自动安装 peer 依赖。
- 发布库时 peer 范围要写得宽（如 ^5.0.0 || ^6.0.0），dependencies 里绝不能再重复声明它。

```javascript
// 插件类库的 package.json
{
  "name": "my-vite-plugin",
  "peerDependencies": {
    // 由使用方的项目提供 vite，版本范围尽量宽
    "vite": "^5.0.0 || ^6.0.0"
  },
  "peerDependenciesMeta": {
    // 可选 peer：宿主没装也不告警
    "typescript": { "optional": true }
  }
}
```
