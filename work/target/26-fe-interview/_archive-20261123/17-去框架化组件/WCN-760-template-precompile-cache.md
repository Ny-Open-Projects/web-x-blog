---
title: [WCN-760] 响应式框架如何做模板预编译缓存（precompiled template cache）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-760：响应式框架如何做模板预编译缓存（precompiled template cache）？

**答**：
- 结论：构建期把模板编译成渲染函数并缓存到模块 Map，运行时用模板 id/字符串 hash 直接取缓存，避免重复编译；开发期可用运行时编译但生产必须用预编译产物。
- 缓存 key 用模板内容 hash，内容变则失效；配合 HMR 在模板更新时清对应缓存条目。
- 追问钩子：动态拼接的模板字符串（如 `render('<div>'+x+'</div>')`）能用预编译缓存吗？考察「动态模板无法预编译」的边界。

```javascript
const cache = new Map();                          // hash -> render fn
function hash(str) { let h = 0; for (const c of str) h = (h * 31 + c.charCodeAt(0)) >>> 0; return h; }
function getRender(template) {
  const key = hash(template);
  if (cache.has(key)) return cache.get(key);
  const fn = compileToRender(template);             // 构建期/首次编译
  cache.set(key, fn);
  return fn;
}
function compileToRender(t) { return (data) => `<div>${data}</div>`; }
console.log(getRender('<div>{{x}}</div>') === getRender('<div>{{x}}</div>')); // true 复用
```
