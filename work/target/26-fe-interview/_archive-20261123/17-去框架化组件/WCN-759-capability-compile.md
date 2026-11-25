---
title: [WCN-759] 编译平台如何做目标能力探测与降级编译（capability-based compile）？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-759：编译平台如何做目标能力探测与降级编译（capability-based compile）？

**答**：
- 结论：编译器读取目标环境的能力清单（如是否支持 Proxy、CSS nesting、top-level await、Web Components），按能力选择代码生成策略：支持则用原生特性，不支持则注入 polyfill 或降级语法。
- 用 browserslist + caniuse-lite 决定 targets；产物分「modern/legacy」两份，通过 `module/nomodule` 或 importmap 分流。
- 追问钩子：运行时才发现能力缺失（如用户禁用了 JS 特性）怎么办？考察「能力探测 + 运行时降级分支」的兜底。

```javascript
const CAPS = { proxy: true, cssNesting: false, topLevelAwait: true };
function compile(src, caps) {
  let out = src;
  if (!caps.proxy) out = injectPolyfill(out, 'proxy');           // 降级：注入 polyfill
  if (!caps.cssNesting) out = flattenCss(out);                  // 展开嵌套 CSS
  if (!caps.topLevelAwait) out = wrapAsync(out);               // 包成 async 函数
  return out;
}
function injectPolyfill(s, n) { return `/* polyfill:${n} */\n` + s; }
function flattenCss(s) { return s.replace(/&:hover/g, ':hover'); }
function wrapAsync(s) { return `(async()=>{${s}})()`; }
console.log(compile('a:hover{}', CAPS));
```
