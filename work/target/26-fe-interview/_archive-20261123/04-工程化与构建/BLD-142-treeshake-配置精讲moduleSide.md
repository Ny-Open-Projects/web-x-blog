---
title: [BLD-142] treeshake 配置精讲：moduleSideEffects、propertyReadSideEffects、annotations 怎么调？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-142：treeshake 配置精讲：moduleSideEffects、propertyReadSideEffects、annotations 怎么调？
**答**：
- `moduleSideEffects: 'no-external' | false | fn`：控制"import 即执行"的副作用假设；CSS 导入、polyfill 入口必须保留副作用，误关会静默丢代码（`import './setup'` 被删）。
- `propertyReadSideEffects: true`（默认）：读取对象属性可能触发 getter（Proxy/Vue2 defineProperty），保守保留完整对象展开；库若确认无 getter 可关掉，展开运算符摇得更狠。
- `annotations: true`（默认）：识别 `/*#__NO_SIDE_EFFECTS__*/`、`/*#__PURE__*/` 注解与 `@__PURE__` 调用标记——给纯函数调用显式标记是库作者最重要的摇树契约。
- 其他高频项：`tryCatchDeoptimization`（try 内不摇）、`unknownGlobalSideEffects`（读未声明全局变量视为副作用）、`correctVarValueBeforeDeclaration`（TDZ 保守）。

```javascript
// rollup.config.js：treeshake 全量配置 + 源码侧的配合注解
export default {
  input: 'src/index.ts',
  treeshake: {
    moduleSideEffects: (id, external) =>
      // CSS 与 polyfill 保留，其余业务模块默认可摇
      id.endsWith('.css') || id.includes('polyfill'),
    propertyReadSideEffects: false,   // 库无 getter/Proxy 时可关，展开与属性访问更激进
    tryCatchDeoptimization: false,    // try/catch 里的代码也参与摇树
    unknownGlobalSideEffects: false,  // 信任全局读取无副作用（有 navigator 探测库时别关）
    annotations: true,                // 尊重 PURE 注解
  },
  plugins: [typescript({ declaration: true })],
};
```

```javascript
// src/api.ts：库作者写给摇树的契约（注解配合）
const cache = new Map();
export function get(key) {
  return cache.get(key);
}
export function set(key, value) {
  return cache.set(key, value);   // 有副作用，永不摇
}
export const noop = /*#__PURE__*/ () => {};          // 显式声明无副作用

// 使用方：
// import { get } from './api'          → set 被整体摇掉
// const x = /*#__PURE__*/ normalize(input)  → 使用方侧标记：未使用时调用被删
// 注意：export const config = { onload() {...} }  在 propertyReadSideEffects: false 时
//       config.onload 这类读取不再保留——库导出含 getter 副作用的对象时必须保持 true
```
