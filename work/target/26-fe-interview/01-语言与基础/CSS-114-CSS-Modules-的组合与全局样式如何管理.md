---
title: [CSS-114] CSS Modules 的组合与全局样式如何管理？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-114：CSS Modules 的组合与全局样式如何管理？

**答**：
- 每个文件独立作用域，导入即拿到哈希后的类名映射对象，杜绝全局冲突。
- `composes` 在编译期把多个类拼接为一个 class 字符串，实现"继承式复用"且零运行时。
- 跨文件组合 `composes: base from "./base.module.css"` 生成多类名，注意不能出现在条件分支里。
- `:global()` 局部逃逸写全局样式，反过来 `:local` 显式声明哈希。
- 全局基础样式与模块样式的边界：reset/token/字体归全局入口文件，一切组件样式走模块。

```css
/* base.module.css */
.base {
  display: inline-flex; align-items: center;
  border-radius: var(--radius-md);
}
```

```css
/* Button.module.css */
.primary {
  composes: base from "./base.module.css"; /* 编译后 class="base_hash primary_hash" */
  background: var(--color-accent);
  color: #fff;
}
/* 全局逃逸：命中第三方类 */
.wrapper :global(.ant-input) { border-radius: 0; }
```

```javascript
import styles from './Button.module.css';
// styles.primary === "base_hash primary_hash"
button.className = styles.primary;
```
