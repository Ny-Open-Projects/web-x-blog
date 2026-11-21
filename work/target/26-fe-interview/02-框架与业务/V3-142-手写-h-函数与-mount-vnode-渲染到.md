---
title: [V3-142] 手写 h 函数与 mount（vnode 渲染到 DOM）？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-142：手写 h 函数与 mount（vnode 渲染到 DOM）？
**答**：
- h 只是 createVNode 的语法糖：返回 `{ type, props, children }` 的普通 JS 对象，"模板编译产物 + 运行时"共同消费它。
- mount 处理三类 children：字符串/数字（textContent）、数组（递归挂载）、单个 vnode；props 分成 onXxx 事件与普通属性。
- vnode.el 反向挂回元素上，是后续 patch、unmount、动画的锚点。
- 分层延伸：mount 里的 createElement/appendChild 属于 runtime-dom，把这部分抽出去换掉就得到 custom renderer——canvas、终端渲染器就是这么来的。

```javascript
// mini-h-mount.js
function h(type, props, children) {
  return { type, props, children }; // vnode：对 DOM 的 JS 描述
}

function mount(vnode, container) {
  const el = (vnode.el = document.createElement(vnode.type)); // el 挂回 vnode 供 patch 用
  for (const key in vnode.props) {
    if (key.startsWith("on")) {
      // onClick -> click
      el.addEventListener(key.slice(2).toLowerCase(), vnode.props[key]);
    } else {
      el.setAttribute(key, vnode.props[key]);
    }
  }
  // children 三分支
  if (typeof vnode.children === "string" || typeof vnode.children === "number") {
    el.textContent = vnode.children;
  } else if (Array.isArray(vnode.children)) {
    vnode.children.forEach((child) => mount(child, el)); // 递归挂载子节点
  } else if (vnode.children) {
    mount(vnode.children, el); // 单个 vnode
  }
  container.appendChild(el);
  return el;
}

// 用法：等价于 <div class="box"><span>hi</span><button @click>点我</button></div>
const vnode = h("div", { class: "box" }, [
  h("span", null, "hi"),
  h("button", { onClick: () => console.log("clicked") }, "点我"),
]);

mount(vnode, document.querySelector("#app"));

// 后续扩展方向（口述即可）：
// unmount：vnode.el.remove()
// patch：新旧 type 不同直接替换；相同则更新 props 差异并 diff children（最长递增子序列）
// 平台无关：把 createElement/appendChild 抽象成 options 注入，即 custom renderer
```

## 第三十一章 指令系统实战

自定义指令是"给已有元素附加行为"的最小成本方案，大厂高频题集中在 loading、权限、复制、长按、懒加载这类通用行为，以及指令与组件的选型边界。
