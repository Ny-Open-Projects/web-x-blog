---
title: [BLD-056] 重复依赖如何发现与去重？resolve.dedupe、overrides、lockfile 各自角色？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-056：重复依赖如何发现与去重？resolve.dedupe、overrides、lockfile 各自角色？
**答**：
- 发现：analyzer 里同名库两块面积、`npm ls lodash` 多条路径、duplicate-package-checker 插件构建期报 warning。
- 手段一（pnpm/yarn）：overrides/resolutions 在 package.json 强制统一版本；手段二（webpack）：resolve.dedupe 指定包名强制只解析一份（对 hooks 类库 react/vue/scheduler 必须唯一）。
- 原因分析：peerDependencies 未声明、lockfile 分叉、monorepo 子包各自安装；根治靠 pnpm 的严格符号链接 + workspace 协议。
- 去重后跑全量回归：部分库真的需要双版本（如 Node 内部包），不要无脑收口。

```json
// package.json：pnpm overrides / yarn resolutions 强制版本统一
{
  "pnpm": {
    "overrides": {
      "lodash": "^4.17.21",
      "react": "$react"
    }
  },
  "resolutions": {
    "react": "18.3.1"
  }
}
```

```javascript
// webpack.config.js：构建期兜底
module.exports = {
  resolve: {
    dedupe: ['react', 'react-dom', 'vue', '@vue/reactivity', 'scheduler'],
    alias: {
      // 极端情况直接把子包别名到主版本
      'react$': require.resolve('react'),
    },
  },
  plugins: [
    // 重复包检测
    new (require('duplicate-package-checker-webpack-plugin'))({ emitError: true }),
  ],
};
```
