---
title: [WCN-780] 设计系统 token 的 Figma → 代码 → 运行时三端一致性如何校验？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-780：设计系统 token 的 Figma → 代码 → 运行时三端一致性如何校验？

**答**：
- 结论：以 Figma Variables 为源导出 token JSON（经转换器），代码端从同一 JSON 生成 CSS 变量/TS 常量，运行时加载同一份产物；三端用「token hash」校验一致性。
- CI 中重跑 Figma 导出与代码生成，对比产物 hash 是否一致；不一致则说明某端手工改过，阻止合并。
- 追问钩子：设计师在 Figma 改了值但没重新发布怎么办？考察「webhook 触发 + 自动生成 PR」的同步机制。

```javascript
function tokenHash(tokens) {
  const s = JSON.stringify(tokens, Object.keys(tokens).sort());
  let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) >>> 0;
  return h.toString(16);
}
const figmaTokens = { '--primary': '#06f', '--bg': '#fff' };
const codeTokens = { '--primary': '#06f', '--bg': '#fff' };
const runtime = { '--primary': '#06f', '--bg': '#000' };  // 运行时被手改
console.log('figma==code:', tokenHash(figmaTokens) === tokenHash(codeTokens));
console.log('figma==runtime:', tokenHash(figmaTokens) === tokenHash(runtime));
```
