---
title: [DP-041] MVC/MVVM 和设计模式是什么关系？（高频）
date: 2026-11-17
categories: [设计模式]
tags: [前端面试, 面试题, 21]
type: 面试题
---

## DP-041：MVC/MVVM 和设计模式是什么关系？（高频）
**答**：
- MVC/MVVM 是**架构模式**（宏观分层），GoF 模式是**实现手段**（微观组合）——一个架构模式由多个 GoF 模式拼装而成。
- MVC：视图观察模型变化（观察者）、控制器/视图按事件分派策略（策略）、视图层级（组合）。
- MVVM：View 与 Model 双向绑定（观察者 + 代理/发布订阅）、ViewModel 对 View 暴露统一接口（外观）。
- 面试答法：先说分层职责，再落到模式实现，避免"背概念对不上代码"。

```javascript
// mini-MVVM：观察者(数据绑定) + 代理(拦截) + 外观(ViewModel 统一入口)
const bus = {                       // 观察者中枢
  map: new Map(),
  on(k, fn) { (this.map.get(k) ?? this.map.set(k, new Set()).get(k)).add(fn); },
  emit(k, v) { (this.map.get(k) || []).forEach((fn) => fn(v)); },
};

// Model：纯数据，被代理拦截
function createModel(data) {
  return new Proxy(data, {
    set(t, k, v) { t[k] = v; bus.emit(k, v); return true; }, // 写时通知视图（观察者）
  });
}

// ViewModel：对外统一入口（外观），编排 Model 与 View
class ViewModel {
  constructor(model, bindings) {
    this.model = model;
    bindings.forEach(([key, el]) => {
      bus.on(key, (v) => { el.textContent = v; });          // 数据->视图
      el.addEventListener('input', (e) => { model[key] = e.target.value; }); // 视图->数据
      el.value = model[key];
    });
  }
  set(key, value) { this.model[key] = value; } // 简化入口：业务只跟 ViewModel 打交道
}

// View：DOM
const nameInput = document.createElement('input');
const nameLabel = document.createElement('span');

// 组装 MVVM
const model = createModel({ name: 'Tom' });
const vm = new ViewModel(model, [['name', nameInput]]);
vm.set('name', 'Jerry');
console.log(nameLabel.textContent); // Jerry —— 数据变了视图自动更新
```

**追问**：

1. 组件化、微前端时代 MVC 还有意义吗，现代框架算哪一类？ → 算 MVVM 的变体：响应式代理替代手动同步、虚拟 DOM 承担视图更新；分层职责没变，只是数据绑定吃掉了 Controller 的一部分。
2. 双向绑定在复杂表单里出了名难调试，你怎么看？ → 复杂状态改单向数据流加受控组件，双向绑定只留给叶子表单控件，避免一个值被多处写入还找不到源头。
3. 让你评价"React 到底算 MVC 的 V 还是 MVVM"，怎么答？ → React 只提供视图层与状态原语，Controller 与 ViewModel 由业务代码承担，hooks 相当于把 VM 逻辑函数化，不必硬套字母。
