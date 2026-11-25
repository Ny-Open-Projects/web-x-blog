---
title: [WCN-455] 笔试：实现动态 class 的编译产物（静态保留 + 逐项 toggle）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-455：笔试：实现动态 class 的编译产物（静态保留 + 逐项 toggle）。
**题目**：输入 `{staticClass, dynamic: [{cls, cond}]}`。产物：静态 add 一次；每个条件项一个 `classList.toggle(cls, !!cond)` 的 effect。

```javascript
function compileClass({ staticClass = '', dynamic = [] }) {
  const lines = [];
  if (staticClass) lines.push(`n.classList.add(${staticClass.split(/\s+/).map(c => `'${c}'`).join(',')});`);
  for (const { cls, cond } of dynamic)
    lines.push(`createEffect(() => n.classList.toggle('${cls}', !!(${cond})));`);
  return lines.join('\n');
}
console.log(compileClass({ staticClass: 'card', dynamic: [
  { cls: 'on', cond: 'active()' }, { cls: 'big', cond: 'size() > 2' }] }));
// 2 个 effect（可审计：effect 数 = 动态项数）

```

**评分点**：
- 静态类一次添加（不进 effect）。
- 条件项逐个 toggle（精确到类）。
- 字符串模板形式（c-{color()}）→ style 属性绑定（补充说明）。
- 产物 effect 数 = 动态项数（可审计）。
