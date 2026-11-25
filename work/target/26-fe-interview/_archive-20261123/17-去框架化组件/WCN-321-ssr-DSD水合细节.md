---
title: [WCN-321] DSD（声明式 Shadow DOM）的解析时序与自研 polyfill 边界？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-321：DSD（声明式 Shadow DOM）的解析时序与自研 polyfill 边界？
**答**：
- 现代浏览器 HTML 解析器原生解析 template[shadowrootmode] 并自动 attach——元素注册前后均可。
- polyfill 场景（旧浏览器）：解析器不处理模板，需要 polyfill 手动 attachShadow+clone——时序在元素定义前。
- 检测：'HTMLTemplateElement' in window && 'shadowRootMode' in HTMLTemplateElement.prototype 判断原生支持。
- 注册时序坑：元素 connectedCallback 早于 shadowRoot attach（polyfill）→ 需等待 attach 完成再渲染。

```javascript
const nativeDSD = 'shadowRootMode' in HTMLTemplateElement.prototype;
if (!nativeDSD) await import('@webcomponents/template-shadowroot'); // polyfill 先行
r
```
