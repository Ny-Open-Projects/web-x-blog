---
title: [V3-263] SSR 的安全风险：XSS 与序列化注入怎么防？
date: 2026-11-17
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-263：SSR 的安全风险：XSS 与序列化注入怎么防？
**答**：
- XSS 主通道：`v-html` 注入用户内容——SSR 输出未转义 HTML 直接进响应体，比客户端 XSS 更直接；必须 DOMPurify 或白名单渲染。
- 序列化注入：payload 里的 `</script>` 截断/`<!--` 注释注入，用 devalue/转义（`\u003C`），不要手拼 JSON。
- URL 类：:href/:src 绑定 `javascript:` 协议、SSR 重定向 open redirect（`redirect` 参数白名单校验）。
- 组件注入：路由 path 动态拼接导致 path traversal（`..%2F`），用白名单路径映射。
- 上下文安全：每请求独立 app/pinia 实例隔离，防止用户 A 的 session 写进全局；CSP 兜底（`script-src 'self' 'nonce-xxx'`）。

```javascript
// 反例与修复
// ❌ <div v-html="userComment">
import DOMPurify from 'isomorphic-dompurify';
const safe = computed(() => DOMPurify.sanitize(props.userComment, { ALLOWED_TAGS: ['b','i','a','p'] }));
// ✅ <div v-html="safe">
// 序列化防注入
function serialize(data) { return JSON.stringify(data).replace(/[<>&]/g, (c) => ({ '<': '\\u003C', '>': '\\u3E', '&': '\\u26' }[c])); }
// 重定向白名单
const allowed = ['/products', '/account'];
const target = getQuery(event).redirect;
if (allowed.some((p) => target.startsWith(p))) sendRedirect(event, target, 302);
```
