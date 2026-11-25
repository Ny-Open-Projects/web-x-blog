---
title: [BLD-029] 怎么排查"该 shake 的没 shake"或"不该 shake 的被 shake 了"？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-029：怎么排查"该 shake 的没 shake"或"不该 shake 的被 shake 了"？
**答**：
- 先确认链路前提：模块是 ESM（import/export）、mode: production、usedExports 与 minimize 打开、依赖包提供 module/exports 入口。
- 定位产物来源：webpack --stats-modules-space 2000 或 stats.toJson({ modules: true })，看每个模块的 providedExports / usedExports 标记（true/false/null）。
- 产物级验证：grep 关键导出名在 dist 中是否存在；配合 webpack-bundle-analyzer 看大模块是否整包进入。
- 没被 shake 的常见原因：CJS 源、`import * as` 或 default 对象导出、动态 require、顶层副作用未声明 sideEffects。
- 不该被 shake 的：给文件加 /*#__PURE__*/ 排查是不是注解误标、检查 sideEffects 数组是否误匹配。

```javascript
// webpack.config.js：诊断配置
module.exports = {
  mode: 'production',
  stats: {
    modules: true,
    reasons: true,          // 输出保留原因 便于定位哪个入口引用了它
    usedExports: true,      // 打印每个模块的导出使用情况
    providedExports: true,
  },
};

// CLI 排查命令
// npx webpack --stats-modules-space 2000 --json > stats.json
// node -e "const s=require('./stats.json');
//   for (const m of s.modules) {
//     if (/lodash/.test(m.name)) {
//       console.log(m.name, m.providedExports, m.usedExports);
//     }
//   }"
```
