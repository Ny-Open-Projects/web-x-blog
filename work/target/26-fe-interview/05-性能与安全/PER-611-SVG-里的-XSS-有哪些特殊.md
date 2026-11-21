---
title: [PER-611] SVG 里的 XSS 有哪些特殊攻击面？<use> 外链、<foreignObject> 与事件属性怎么防？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-611：SVG 里的 XSS 有哪些特殊攻击面？<use> 外链、<foreignObject> 与事件属性怎么防？

**答**：
- SVG 的特殊面：**SVG 支持内嵌 script 与事件属性**（`<svg onload>` 是最经典的过滤绕过载体）；`<use href="//evil.com/icon.svg#x">` 可跨域引用外部 SVG 并执行其中定义的脚本（现代浏览器已限制，但旧内核/WebView 仍可）；`<foreignObject>` 可嵌 HTML 再次引入全套 HTML 攻击面；SVG 里的 `<animate>` 可动态改属性绕过静态检测。
- 典型事故：用户上传 SVG 当头像/图标直接同域部署——同源 SVG 打开即执行脚本，等同存储型 XSS。
- 防御：SVG 白名单净化（剔除 script/foreignObject/on* 事件属性/animate 的 attributeName 可疑目标、use 仅允许同域）；上传的 SVG **跨域隔离存放**（独立文件域名 + `Content-Disposition: attachment` 或直接转 PNG 渲染）；展示场景用 `<img>` 引用 SVG（img 内脚本不执行）而不是 inline svg。
- 追问钩子：为什么 `<img src="x.svg">` 安全而 innerHTML 注入不安全？——img 文档模式禁脚本，innerHTML 是活动文档上下文。

```javascript

// SVG 白名单净化（关键差异点）
const SVG_BLOCK_TAGS = new Set(['script', 'foreignObject', 'animate', 'set', 'handler', 'listener']);
function sanitizeSvg(svgText) {
  const doc = new DOMParser().parseFromString(svgText, 'image/svg+xml');
  const svg = doc.documentElement;
  if (svg.tagName !== 'svg' || doc.querySelector('parsererror')) return null;
  doc.querySelectorAll('*').forEach(el => {
    if (SVG_BLOCK_TAGS.has(el.tagName.toLowerCase())) return el.remove();
    [...el.attributes].forEach(a => {
      if (/^on/i.test(a.name)) return el.removeAttribute(a.name);         // 事件属性
      if (a.name === 'href' && el.tagName.toLowerCase() === 'use') {
        const u = new URL(a.value, 'https://x.invalid');
        if (u.origin !== location.origin) return el.removeAttribute(a.name); // use 仅同域
      }
    });
  });
  return new XMLSerializer().serializeToString(svg);
}
// 展示层约束：<img src="avatar.svg"> 而非 innerHTML；上传文件走独立文件域名
```
