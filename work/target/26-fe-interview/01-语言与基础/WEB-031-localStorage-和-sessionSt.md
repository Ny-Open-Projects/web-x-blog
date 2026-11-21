---
title: [WEB-031] localStorage 和 sessionStorage 有什么区别？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-031：localStorage 和 sessionStorage 有什么区别？
**答**：
- 生命周期：localStorage 持久化，手动清除才消失；sessionStorage 属于会话级，标签页关闭即清空。
- 作用域：localStorage 同源共享（所有标签页）；sessionStorage 每个标签页独立，新标签页打开同链接也不继承（复制标签页除外）。
- 容量约 5MB，均为字符串 KV 存储，对象要 `JSON.stringify` 序列化，且写入是同步的，大对象会阻塞主线程。
- 均可被同源 JS 读取，敏感信息（token 以外）不建议明文放，XSS 可直接拿走。

```javascript
// localStorage / sessionStorage 的典型用法与差异验证
const user = { id: 42, name: 'Wang' };

localStorage.setItem('user', JSON.stringify(user)); // 必须手动序列化
const cached = JSON.parse(localStorage.getItem('user') || 'null');
console.log(cached.name); // Wang

sessionStorage.setItem('draft', '未提交的表单内容'); // 标签页级，防误关丢稿
localStorage.setItem('theme', 'dark');

// 监听同源其他标签页的写入（跨标签页通信的经典用法）
window.addEventListener('storage', (e) => {
  // 本标签页自己 setItem 不触发，只有其他标签页修改才触发
  console.log(`key=${e.key} oldValue=${e.oldValue} newValue=${e.newValue}`);
  if (e.key === 'logout') location.href = '/login';
});

localStorage.removeItem('user');
localStorage.clear(); // 清空全部
```
