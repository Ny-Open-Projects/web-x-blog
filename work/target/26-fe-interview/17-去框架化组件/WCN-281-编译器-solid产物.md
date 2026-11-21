---
title: [WCN-281] SolidJS 编译器把 JSX 编译成什么样（真实产物形态）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-281：SolidJS 编译器把 JSX 编译成什么样（真实产物形态）？
**答**：
- JSX 静态部分提取为模板 clone（innerHTML 一次性创建），动态部分生成定向 createEffect。
- 表达式按「读信号的粒度」拆分：`<div class={a() + b()}>` 拆成两个 effect 各写 class 的一部分（字符串拼接场景合并）。
- 组件函数体只执行一次（无重渲染）——props 解构被编译器警告（丢失响应性）。
- 产物可读性：编译输出接近手写信号代码——这是「编译器响应式」的可验证性优势。

```javascript
// 输入
<div class="card {active() ? 'on' : ''}">{title()}</div>
// 编译产物（简化）
const t = template(`<div class="card"></div>`);
const n = t(); n.classList.toggle('on', !!active());  // 静态前缀保留
createEffect(() => n.classList.toggle('on', !!active()));
createEffect(() => n.firstChild.textContent = title());
r
```
