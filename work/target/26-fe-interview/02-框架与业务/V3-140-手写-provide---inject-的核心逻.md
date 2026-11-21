---
title: [V3-140] 手写 provide / inject 的核心逻辑？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-140：手写 provide / inject 的核心逻辑？
**答**：
- 本质是组件实例上的 provides 对象：初始化时用 `Object.create(parent.provides)` 继承父实例的 provides，形成原型链。
- provide 就是往当前实例的 provides 写 key；inject 沿原型链向上查找，找不到再走默认值逻辑。
- "逐层向上查找"不需要写循环——原型链本身就是查找链，这是最优雅的实现点。
- 生产版补充：inject 的默认值支持工厂函数（避免对象类型共享引用）、提供响应式对象保持同步、找不到时开发环境告警。

```javascript
// mini-provide-inject.js —— 组件实例上下文简化模型
function createComponentInstance(parent) {
  return {
    parent,
    // 关键：provides 继承父组件的 provides，形成原型链
    provides: parent ? Object.create(parent.provides) : Object.create(null),
  };
}

function provide(instance, key, value) {
  if (key in instance.provides) {
    console.warn(`provide 的 key ${key} 已被祖先占用，将覆盖`); // 源码的同名告警
  }
  instance.provides[key] = value; // 写在当前实例上，后代沿链可查
}

function inject(instance, key, defaultValue, needDefault = false) {
  if (key in instance.provides) {
    return instance.provides[key]; // `in` 沿原型链自动向上查找
  }
  if (needDefault) {
    // 默认值支持工厂：传函数时执行取结果，避免对象默认值被多处共享
    return typeof defaultValue === "function" ? defaultValue() : defaultValue;
  }
  console.warn(`injection ${key} 未找到且未提供默认值`);
}

// 演示：爷爷 -> 父 -> 子 的注入链
const grandpa = createComponentInstance(null);
provide(grandpa, "theme", "dark");

const parent = createComponentInstance(grandpa);
provide(parent, "api", { request: () => {} }); // 父层继续提供新 key

const child = createComponentInstance(parent);
console.log(inject(child, "theme")); // dark：沿原型链找到爷爷的 provide
console.log(inject(child, "api"));   // 父层提供的对象
console.log(inject(child, "missing", () => ({ size: "md" }), true)); // 工厂默认值

// 对应组件内的等价写法
// 祖先：provide("theme", themeRef)   —— 提供响应式对象，后代读到的永远是最新的
// 后代：const theme = inject("theme", ref("light"))
```
