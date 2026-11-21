---
title: [CSS-066] :user-invalid 解决了 :invalid 的什么问题？
date: 2026-11-17
categories: [CSS]
tags: [前端面试, 面试题, 03]
type: 面试题
---

## CSS-066：:user-invalid 解决了 :invalid 的什么问题？

**答**：
- `:invalid` 在页面加载、用户尚未输入时就匹配（如 required 空值），导致"一进页面就报错"。
- `:user-invalid` 只在用户交互过且当前值不合法时匹配；`:user-valid` 同理。
- 适合做错误提示的入场动画：先有交互，再淡入错误态，体验更自然。
- 兼容：Chrome 119+ / Safari 16.5+ / Firefox 88+，老浏览器用 `:invalid` 兜底逻辑。
- 配合 `:placeholder-shown` 可以区分"还没填"和"填错了"。

```css
.field input {
  border: 1px solid var(--border-color);
  transition: border-color 0.2s, box-shadow 0.2s;
}

/* 只有用户真的输错了才标红，避免初始页面全红 */
.field input:user-invalid {
  border-color: var(--color-danger);
  box-shadow: 0 0 0 3px color-mix(in srgb, var(--color-danger) 15%, transparent);
}

/* 错误提示随交互淡入 */
.field .error {
  opacity: 0;
  transform: translateY(-2px);
  transition: opacity 0.2s;
}
.field:has(input:user-invalid) .error { opacity: 1; transform: none; }
```

## 十三、布局专题实战
