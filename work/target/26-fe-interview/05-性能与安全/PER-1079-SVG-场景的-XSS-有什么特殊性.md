---
title: [PER-1079] SVG 场景的 XSS 有什么特殊性
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1079：SVG 场景的 XSS 有什么特殊性

**答**：
- SVG 支持内嵌 <script>、事件属性、foreignObject，且作为独立文档打开（img 引用的 SVG 不执行脚本，直接访问会执行）。
- 上传 SVG 必须消毒（DOMPurify 支持 svg profile）+ 服务端强制 Content-Disposition: attachment + Content-Type: image/svg+xml（不作为文档渲染）。
- SVG 内 <use xlink:href> 可引用外部资源（fetch 泄露），需剥除或限制同源。
- CSP 对独立打开的 SVG 文件同样生效（确保部署覆盖）。

```javascript
function sanitizeSVG(svgText) {
  const doc = new DOMParser().parseFromString(svgText, 'image/svg+xml');
  if (doc.querySelector('parsererror')) throw new Error('非法 SVG');
  doc.querySelectorAll('script, foreignObject').forEach(n => n.remove());
  doc.querySelectorAll('use').forEach(n => {
    const href = n.getAttribute('href') ?? n.getAttribute('xlink:href') ?? '';
    if (href && !href.startsWith('#')) n.remove();   // 禁外链 use
  });
  doc.querySelectorAll('*').forEach(n => {
    [...n.attributes].forEach(a => {
      if (/^on/i.test(a.name)) n.removeAttribute(a.name);
    });
  });
  return new XMLSerializer().serializeToString(doc);
}
```
