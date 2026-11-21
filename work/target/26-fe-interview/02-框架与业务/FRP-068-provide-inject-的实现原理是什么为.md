---
title: [FRP-068] provide/inject 的实现原理是什么？为什么说它是"原型链查找"？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-068：provide/inject 的实现原理是什么？为什么说它是"原型链查找"？

**答**：
- 初始化组件实例时：`instance.provides = parent ? parent.provides : appContext.provides`（根组件用 app 级 provides）。**默认不复制对象，而是子组件直接引用父的 provides**。
- 当组件**自己调用 provide(key, value)** 时才创建新对象：`instance.provides = Object.create(currentInstance.provides)`——用原型链继承父级 provides，自己 provided 的 key 挂在自身这一层。
- inject 查找就是 **一次原型链属性访问**：`inject(key)` 即 `currentInstance.provides[key]`，顺着 `__proto__` 向祖先链走，最近提供者优先（就近覆盖远端），找不到回退到 `defaultValue`（函数则惰性求值）。
- 优势：O(链深) 的一次 JS 属性查找，无需逐层遍历/传递；这也是嵌套 provide 同名 key"就近生效"的实现机制。

```javascript
// 简化实现，帮助理解原型链式 provide/inject
function createComponentInstance(parent) {
  return {
    parent,
    // 关键：默认直接引用父级 provides，不新建
    provides: parent ? parent.provides : Object.create(null),
    providesProvided: false,
  };
}

function provide(instance, key, value) {
  if (!instance.providesProvided) {
    // 首次 provide 才建新对象，以父 provides 为原型
    instance.provides = Object.create(instance.provides);
    instance.providesProvided = true;
  }
  instance.provides[key] = value; // 挂在自己这一层
}

function inject(instance, key, defaultValue) {
  const val = instance.provides[key]; // 一次属性访问，沿 __proto__ 向上找
  if (val !== undefined) return val;
  if (defaultValue !== undefined) {
    return typeof defaultValue === 'function' ? defaultValue() : defaultValue; // 惰性默认值
  }
  console.warn(`[inject] key "${String(key)}" 未找到提供者`);
}

// 层级：Root -> Child -> GrandChild
const root = createComponentInstance(null);
const child = createComponentInstance(root);
const grand = createComponentInstance(child);

provide(root, 'theme', 'dark');        // 祖先提供
provide(child, 'size', 'large');       // 中间层提供

console.log(inject(grand, 'theme'));   // dark：沿原型链跨两层找到
console.log(inject(grand, 'size'));    // large
console.log(inject(grand, 'miss', () => 'fallback')); // fallback 惰性默认值
provide(child, 'theme', 'light');      // 中间层就近覆盖
console.log(inject(grand, 'theme'));   // light：近层优先
console.log(inject(root, 'theme'));    // dark：root 自身不受影响
```
