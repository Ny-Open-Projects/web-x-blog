---
title: [WEB-151] XSS 三种类型的代码长什么样？分别怎么修？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-151：XSS 三种类型的代码长什么样？分别怎么修？
**答**：
- 存储型：恶意脚本入库（如评论），所有访问者中招，危害最大。
- 反射型：脚本藏在 URL 参数，服务端原样回显，需要诱导点击。
- DOM 型：纯前端把不可信数据写进 innerHTML/eval/location 等危险 sink，服务端无感知。
- 修复原则：默认用 textContent/setAttribute 等安全 API；富文本过 DOMPurify 白名单消毒；配合 CSP 兜底；框架默认转义，但别用 dangerouslySetInnerHTML 或 v-html 插未消毒 HTML。

```html
<!-- DOM 型 XSS 的漏洞与修复对照 -->
<script>
  const name = new URLSearchParams(location.search).get('name');
  // 漏洞：?name=<img src=x onerror=alert(1)> 会被当 HTML 执行
  document.getElementById('greet').innerHTML = 'Hi, ' + name;
  // 修复 1：纯文本一律 textContent
  document.getElementById('greet').textContent = 'Hi, ' + name;
  // 修复 2：确需富文本时白名单消毒
  document.getElementById('rich').innerHTML = DOMPurify.sanitize(name, { ALLOWED_TAGS: ['b', 'i', 'em'] });
</script>
<!-- 存储型与反射型同理：服务端按输出上下文转义，HTML 属性 JS URL 各有不同转义规则 -->
```
