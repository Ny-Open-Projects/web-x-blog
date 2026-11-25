---
title: [JS-151] 手写 observe + compile 的 MVVM 思想？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 笔试题, 04]
type: 笔试题
---

## JS-151：手写 observe + compile 的 MVVM 思想？

**答**：
- MVVM 三件套：Observer 递归劫持数据、Compile 解析模板里的插值与指令、Watcher 把两者连起来。
- Observer 对数据每个 key 做 defineProperty，set 时通知所有订阅该数据的更新函数。
- Compile 扫描 DOM，找到 `{{}}` 插值，为每个插值注册一个更新函数，数据变化时重算文本。
- 真正的 Vue 是「Compile 生成更新函数 + 数据变化精准通知对应 Watcher」，本例用简化广播演示数据到视图的单向流动。

```javascript
const updateFns = [];                 // 所有视图更新函数的队列

// Observer：递归劫持数据
function observe(data) {
  if (typeof data !== 'object' || data === null) return;
  Object.keys(data).forEach((key) => {
    let val = data[key];
    observe(val);                     // 深层对象也要劫持
    Object.defineProperty(data, key, {
      get() { return val; },
      set(nv) {
        val = nv;
        observe(nv);                  // 新赋值的对象同样劫持
        updateFns.forEach((fn) => fn()); // 简化广播：真实实现按 key 精准通知
      },
    });
  });
}

// Compile：解析模板中的插值，产出更新函数
function compile(el, data) {
  const render = () => {
    el.innerHTML = el.innerHTML.replace(/\{\{\s*([\w.]+)\s*\}\}/g, (_, path) => {
      const v = path.split('.').reduce((o, k) => (o == null ? o : o[k]), data);
      return v == null ? '' : v;
    });
  };
  updateFns.push(render);             // 数据变化时重新渲染
  render();                           // 首次渲染
}

// Mini MVVM 串起来
const vmData = { user: { name: 'Alice' }, age: 18 };
observe(vmData);
const root = document.createElement('div');
root.innerHTML = '<p>姓名 {{ user.name }} 年龄 {{ age }}</p>';
document.body.appendChild(root);
compile(root, vmData);                // 显示：姓名 Alice 年龄 18
vmData.age = 20;                      // 触发 setter → 广播 → 视图变为 年龄 20
```
