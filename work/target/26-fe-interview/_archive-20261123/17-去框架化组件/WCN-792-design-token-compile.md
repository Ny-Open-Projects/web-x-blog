---
title: [WCN-792] 设计即代码：编译期如何把设计 token 注入模板样式？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-792：设计即代码：编译期如何把设计 token 注入模板样式？

**答**：
- 结论：编译器在生成 CSS/样式对象时，把模板里引用的语义 token（如 `var(--color-primary)`）在编译期解析为具体主题值或保留为 CSS 变量引用；结合 token 元数据生成「design token → 运行时变量」映射。
- 好处：设计变更只需改 token 源，编译产物自动更新；编译期能校验 token 引用是否存在、是否废弃，提前报错。
- 追问钩子：运行时动态换肤时编译期注入的固定值怎么办？考察「注入 CSS 变量引用而非字面值」以支持运行时切换。

```javascript
const TOKENS = { 'color.primary': '#06f', 'space.md': '16px' };
function compileStyle(css, tokens) {
  // 把 token() 语法编译为 CSS 变量引用（保留运行时换肤能力）
  return css.replace(/token\(([\w.]+)\)/g, (m, name) => {
    if (!(name in tokens)) throw new Error(`未知 token: ${name}`);
    return `var(--${name.replace('.', '-')}, ${tokens[name]})`;
  });
}
console.log(compileStyle('button{color:token(color.primary);padding:token(space.md)}', TOKENS));
```
