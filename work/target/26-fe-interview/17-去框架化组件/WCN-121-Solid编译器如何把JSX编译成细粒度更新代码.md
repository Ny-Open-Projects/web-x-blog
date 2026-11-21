---
title: [WCN-121] Solid 编译器如何把 JSX 编译成细粒度更新代码？编译产物的结构是什么？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 编译器方向]
type: 面试题
---

## WCN-121：Solid 编译器如何把 JSX 编译成细粒度更新代码？

**答**：
- 编译流水线：babel-plugin-jsx（solid）解析 JSX → 标记响应式节点（含 signal/computed 读取的表达式）→ 生成"DOM 构建代码 + 每个动态点一个 renderEffect"。
- 产物结构（伪码）：`const el = template(...)`（克隆静态模板）→ `insert(el, () => expr())`、`effect(() => setText(span, name()))`；静态属性直接内联，不再进入更新路径。
- 关键优化：`template()` 用 innerHTML 预建静态骨架，运行时 `cloneNode` 复用——比逐个 createElement 快且省内存。
- 表达式包装：编译器自动把动态表达式包成 getter（`() => props.name`），保持响应性；这是"解构丢响应"问题的根源。
- 控制流组件：`<For>`/`<Show>`/`<Switch>` 是编译器识别的专用节点，生成 keyed 增量更新代码而非重建。

```jsx
// 源码
const App = () => {
  const [n, setN] = createSignal(0);
  return <div><span class="num">{n()}</span><span>静态文本</span></div>;
};

// 编译产物（示意）
const _tmpl = template(`<div><span class="num"></span><span>静态文本</span></div>`);
const App = () => {
  const [n, setN] = createSignal(0);
  const el = _tmpl.cloneNode(true);
  (effect(() => setText(el.firstChild, n())));   // 只有动态点
  return el;
};
```
