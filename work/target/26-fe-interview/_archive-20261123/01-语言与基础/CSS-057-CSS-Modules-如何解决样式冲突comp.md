---
title: [CSS-057] CSS Modules 如何解决样式冲突？composes 怎么用？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-057：CSS Modules 如何解决样式冲突？composes 怎么用？

**答**：
- 构建时把类名编译成 `文件名__类名__hash` 的唯一标识，天然局部作用域，无全局污染。
- JS 侧 `import styles from './a.module.css'` 引用编译后的真实类名。
- `composes` 复用同文件或其他文件（来自 foundation）的类，实现类似继承。
- 缺点：动态类名拼接不便、与 UI 库全局样式对接需要 :global。

```css
/* Button.module.css */
.btn {
  padding: 8px 16px;
  border-radius: 4px;
}
.primary {
  composes: btn;                 /* 复用同文件 */
}
.outline {
  composes: btn from "./base.css"; /* 跨文件复用 */
}

/* :global 逃逸 */
.wrapper :global(.ant-btn) {
  margin-right: 8px;
}
```

```javascript
// Button.jsx
import styles from './Button.module.css';
// styles.primary === "Button_primary__1x2y3"（编译后唯一名）
export function Button({ type = 'primary', children }) {
  return <button className={styles[type]}>{children}</button>;
}
```
