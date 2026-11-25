---
title: [WEB-362] DOM 型 XSS 有哪些隐蔽场景？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-362：DOM 型 XSS 有哪些隐蔽场景？
**答**：
- innerHTML/outerHTML/document.write 直插用户数据；location.hash/search 拼进 DOM 不经过服务端，报文审计看不到。
- 富文本回显（评论/IM 消息）与 URL 参数渲染（?name=xxx 回显欢迎语）是高频入口；第三方组件的 dangerouslySetInnerHTML 同样是口子。
- 加固：一律 textContent 或净化库；URL 参数渲染前转义；CSP 兜底让注入的脚本无处执行。

```javascript
const dangerous = [
  () => el.innerHTML = location.hash.slice(1),      // #<img onerror>
  () => document.write(new URLSearchParams(location.search).get('q')),
  () => el.innerHTML = '<div>' + comment.content + '</div>',
];
// 修复
el.textContent = location.hash.slice(1);
el.innerHTML = DOMPurify.sanitize(comment.content);
console.log('DOM XSS 不经过服务器 → 只能靠前端自律');
```
