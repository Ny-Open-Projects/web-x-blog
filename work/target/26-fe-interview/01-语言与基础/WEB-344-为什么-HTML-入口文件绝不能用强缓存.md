---
title: [WEB-344] 为什么 HTML 入口文件绝不能用强缓存？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 缓存]
type: 面试题
---

## WEB-344：为什么 HTML 入口文件绝不能用强缓存？
**答**：
- HTML 引用带 hash 的 js/css；若 HTML 被强缓存，新版本发布后用户拿到的 HTML 仍指向旧资源—— Worse：旧资源文件被删则直接白屏。
- 正确姿势：HTML 用 no-cache（每次协商）或短 max-age+must-revalidate；静态资源长 max-age+immutable+内容 hash。
- 回滚方案同理：发布要保留上一版本资源文件，等旧 HTML 过期窗口过后再清理。

```javascript
const headers = {
  '/index.html': 'no-cache',                          // 每次协商
  '/assets/app.9f2c1.js': 'max-age=31536000, immutable',
};
// 发布顺序: 先传新 js → 再更新 HTML → 保留旧 js 一段时间
console.log('HTML 强缓存 = 用户永远拿不到新版本');
```
