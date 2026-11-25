---
title: [WCN-705] 微前端多实例下自定义元素 tag 名冲突，如何在运行时做前缀重写？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-705：微前端多实例下自定义元素 tag 名冲突，如何在运行时做前缀重写？

**答**：
- 结论：同一页面加载多个子应用时，各应用可能注册同名 tag（如 ds-button）；用构建期给 tag 加应用前缀（如 app1-ds-button）或运行时作用域注册表隔离。
- 运行时方案：代理 customElements.define/get，按当前执行上下文映射真实 tag；注意 DSD 与样式选择器也要同步改写。
- 追问钩子：前缀重写后，跨应用的事件 composed 路径与 CSS ::part 选择器会失效吗？考察对边界影响的评估。

```javascript
// 运行时 tag 前缀重写（简化）
const realDefine = customElements.define.bind(customElements);
const realGet = customElements.get.bind(customElements);
const SCOPE = '__APP1__';
const scoped = new Map();
customElements.define = function (name, cls, opts) {
  const real = SCOPE + name;                 // 加前缀
  scoped.set(name, real);
  return realDefine(real, cls, opts);
};
customElements.get = function (name) {
  return realGet(scoped.get(name) || name);
};
console.log('已隔离注册:', scoped.has('ds-button'));
```
