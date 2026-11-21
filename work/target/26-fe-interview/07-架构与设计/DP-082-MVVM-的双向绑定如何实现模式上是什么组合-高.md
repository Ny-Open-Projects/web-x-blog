---
title: [DP-082] MVVM 的双向绑定如何实现？模式上是什么组合？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-082：MVVM 的双向绑定如何实现？模式上是什么组合？（高频）
**答**：
- 双向绑定 = 数据→视图（观察者/发布订阅）+ 视图→数据（事件监听回写）两条通路合环。
- Vue2：`Object.defineProperty` + Dep + Watcher + 指令编译（compile 时把 v-model 编译成绑定 + input 监听）。
- Vue3：Proxy 代理 + effect（观察者）+ `v-model` 语法糖（`:value` + `@input`）。
- 模式组合：代理（拦截数据）+ 观察者（通知更新）+ 外观（ViewModel 统一入口）+ 模板方法（编译流水线）。

```javascript
// mini 双向绑定：defineProperty 版（Vue2 原理）+ v-model 编译
function observe(obj) {
  const deps = new Map(); // key -> Set<更新函数>
  Object.keys(obj).forEach((key) => {
    let val = obj[key];
    if (!deps.has(key)) deps.set(key, new Set());
    Object.defineProperty(obj, key, {
      get() { return val; },
      set(nv) {
        val = nv;
        deps.get(key).forEach((fn) => fn(nv)); // 数据 -> 视图（观察者通知）
      },
    });
  });
  return { deps };
}
// 编译器：扫描带 v-model 的节点，建立双向通路
function compile(el, model, deps) {
  el.querySelectorAll('[v-model]').forEach((node) => {
    const key = node.getAttribute('v-model');
    // 通路1：数据 -> 视图
    const updater = (v) => { node.value = v; };
    deps.get(key).add(updater);
    node.value = model[key]; // 初始同步
    // 通路2：视图 -> 数据
    node.addEventListener('input', (e) => { model[key] = e.target.value; });
  });
}
// 装配 MVVM
const app = document.createElement('div');
app.innerHTML = '<input v-model="name"/><span v-model="name"></span>';
const vm = { name: 'Tom' };
const { deps } = observe(vm);          // Model 层：代理拦截
compile(app, vm, deps);                // 编译 View 与 Model 的绑定
const input = app.querySelector('input');
input.value = 'Jerry';
input.dispatchEvent(new Event('input')); // 用户输入 -> 数据更新 -> 视图全同步
console.log(vm.name);                  // Jerry
console.log(app.querySelector('span').value); // Jerry —— 两处绑定同时更新
// Vue3 差异：defineProperty -> Proxy（可拦截新增/删除/数组），编译产出 -> render 函数 + effect
```
