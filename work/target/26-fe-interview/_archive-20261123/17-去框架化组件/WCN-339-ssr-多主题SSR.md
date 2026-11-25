---
title: [WCN-339] 多主题（暗色）在 SSR 的 DSD 输出（如何知道用户主题）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-339：多主题（暗色）在 SSR 的 DSD 输出（如何知道用户主题）？
**答**：
- 主题来源：cookie（SSR 可读）→ 服务端按主题输出对应 token 值（DSD 内联）。
- 避免闪烁： prefers-color-scheme fallback + cookie 精确匹配。
- 客户端切换：切主题 = 替换 shadow 内 CSS 变量（元素监听主题事件或宿主 root 类切换自动继承）。
- 成本：每主题一份缓存键（主题进缓存 key）。

```javascript
const theme = cookies.theme ?? prefersDark ? 'dark' : 'light';
const html = renderDSD({ ...props, theme });   // token 按主题求值内联
// 客户端切换：documentElement.classList.toggle('dark') → 变量继承更新
r
```
