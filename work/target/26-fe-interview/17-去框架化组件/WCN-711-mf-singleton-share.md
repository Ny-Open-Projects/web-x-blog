---
title: [WCN-711] 微前端里多个子应用都用到同一套 WC，怎么做资源去重与单例共享？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-711：微前端里多个子应用都用到同一套 WC，怎么做资源去重与单例共享？

**答**：
- 结论：用 Module Federation 的 `singleton: true` 把 @ds/core 等共享包声明为单例，配合 `eager:false` 与版本协商，避免组件实例重复注册、状态割裂。
- 对自定义元素注册表做「先到先得」保护：`customElements.get(tag)` 存在就复用，不重复 define；共享 CSS 用 adoptedStyleSheets 复用同一份 CSSStyleSheet。
- 追问钩子：两个子应用要求不同大版本的同一组件怎么办？考察 multi-version 共存与 tag 前缀隔离的组合方案。

```javascript
// Module Federation 配置片段
const federation = {
  shared: {
    '@ds/core': { singleton: true, requiredVersion: '^2.0.0', eager: false },
    '@ds/button': { singleton: true },
  },
};
// 注册保护：先到先得
function safeDefine(tag, cls) {
  if (!customElements.get(tag)) customElements.define(tag, cls);
  return customElements.get(tag);
}
console.log('单例共享避免重复注册与状态割裂');
```
