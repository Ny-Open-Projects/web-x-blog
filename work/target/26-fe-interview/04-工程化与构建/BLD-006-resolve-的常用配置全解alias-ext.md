---
title: [BLD-006] resolve 的常用配置全解？alias、extensions、mainFields、enforceExtension 分别怎么用？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-006：resolve 的常用配置全解？alias、extensions、mainFields、enforceExtension 分别怎么用？
**答**：
- alias：路径映射，`@/` 指向 src，`$` 精确匹配结尾；alias 会跳过部分解析逻辑，是最常用的提效配置。
- extensions：无后缀导入时的尝试列表，`['.js', '.ts', '.tsx', '.json']`，列表越长解析越慢，尽量精简并排高频后缀在前。
- mainFields：解析 package.json 的入口字段顺序，默认 `['browser', 'module', 'main']`（target: web 时），库打包场景常改为 `['module', 'main']` 优先 ESM。
- enforceExtension：true 时导入必须写后缀（默认 false）；resolve.modules 收缩查找目录、mainFiles 指定目录默认文件名。
- 面试延伸：alias 配置错会导致 monorepo 里引用到错误包版本；extensions 里出现重复后缀会重复 IO。

```javascript
// webpack.config.js
const path = require('path');

module.exports = {
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src'),
      'vue$': 'vue/dist/vue.runtime.esm-bundler.js', // $ 表示精确匹配
    },
    extensions: ['.js', '.ts', '.tsx', '.json'], // 按命中率排序 尽量短
    mainFields: ['browser', 'module', 'main'],   // web 目标默认值 优先浏览器版与 ESM 版
    mainFiles: ['index'],
    modules: [path.resolve(__dirname, 'node_modules'), 'node_modules'], // 收缩查找范围
    enforceExtension: false, // true 时 import './a' 报错 必须写 './a.js'
    enforceModuleExtension: false,
    symlinks: true, // 解析软链接真实路径 pnpm/monorepo 需要关注
  },
};
```
