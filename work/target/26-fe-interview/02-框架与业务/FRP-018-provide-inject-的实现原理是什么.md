---
title: [FRP-018] provide/inject 的实现原理是什么？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-018：provide/inject 的实现原理是什么？

**答**：
- 每个组件实例都有 `provides` 对象；初始化时 `provides = parent ? Object.create(parent.provides) : { appContext }`——用**原型链继承**父级 provides。
- 这就是"子可以读父/祖先注入、同名注入就近覆盖"的原因：沿原型链查找，最近的实例属性先命中。
- inject 就是 `provides[key]` 的链式查找（原型链自动完成）；响应式注入值（ref/reactive）自然继承响应性。
- 用 Symbol 作 key 可避免组件库之间的 key 冲突；`app.provide` 挂在 appContext 上作为原型链末端兜底。

```javascript
// 简化实现，帮助理解 provides 原型链
const currentInstance = { provides: null };

function createComponentInstance(parent) {
  const instance = {
    parent,
    provides: parent
      ? Object.create(parent.provides) // 关键：原型链继承父级 provides
      : { appProvide: true },          // 根组件兜底 app.provide 的内容
  };
  return instance;
}

function provide(key, value) {
  currentInstance.provides[key] = value; // 写在自己的 provides 上（子就近可见）
}

function inject(key, defaultValue) {
  // 原型链查找：__proto__ 一路向上，最近的 provide 先命中
  let instance = currentInstance;
  if (key in instance.provides) return instance.provides[key];
  if (arguments.length > 1) return typeof defaultValue === 'function' ? defaultValue() : defaultValue;
  console.warn(`injection "${String(key)}" not found`);
}

// 验证：孙组件读到的 theme 是 Parent就近覆盖的值
const app = createComponentInstance(null);
const parent = createComponentInstance(app);
const child = createComponentInstance(parent);

currentInstance.provides = app.provides;   app.provides.theme ??= null;
// 模拟 provide 链
parent.provides.theme = 'parent-theme';    // Parent provide('theme', ...)
child.provides.theme = 'child-theme';      // Child 覆盖 provide('theme', ...)

console.log(child.provides.theme);  // child-theme —— 就近覆盖
console.log(parent.provides.theme); // parent-theme
console.log('未注册的 key 沿原型链找不到，走默认值：', inject('missing', 'fallback'));
```
