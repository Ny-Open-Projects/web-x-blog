---
title: [CSS-044] CSS 变量与 Sass/Less 变量的本质区别？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-044：CSS 变量与 Sass/Less 变量的本质区别？

**答**：
- Sass/Less 变量在**编译期**替换为字面量，产物中不存在；CSS 变量在**运行时**生效，保留在产物里。
- CSS 变量遵循级联与继承，可按 DOM 子树局部覆盖；预处理器变量无作用域概念进入 CSS 后不可变。
- CSS 变量能被 JS 读写、能进 media query 里重定义，预处理器变量不行。
- 组合用法：预处理器负责 mixin/嵌套，运行时动态性交给原生变量。

```scss
// Sass：编译期
$primary: #409eff;
.a { color: $primary; }       // 产物: color: #409eff，变量消失
@media (prefers-color-scheme: dark) {
  // $primary 无法在此被“换成另一个 Sass 变量后再被组件感知”
}

// CSS 变量：运行时
:root { --primary: #409eff; }
.b { color: var(--primary); }
@media (prefers-color-scheme: dark) {
  :root { --primary: #79bbff; } // .b 自动跟随，无需重新编译
}
```
