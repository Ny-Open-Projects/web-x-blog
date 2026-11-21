---
title: [WEB-495] 笔试：手写富文本白名单 sanitizer
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 笔试题, 安全]
type: 笔试题
---

## WEB-495：笔试：手写富文本白名单 sanitizer

**题目**：实现 `sanitize(html)`：只允许白名单标签（p/b/i/a/img/ul/li）与白名单属性（a 的 href 需为 http(s) 链接，img 的 src）；移除 script/style/事件属性；不使用第三方库。

**答**：
```javascript
const ALLOWED = new Set(['P', 'B', 'I', 'A', 'IMG', 'UL', 'OL', 'LI', 'BR']);

function sanitize(html) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const walk = (node) => {
    [...node.children].forEach(el => {
      if (!ALLOWED.has(el.tagName)) { el.replaceWith(...el.childNodes); return; }
      // 白名单属性
      [...el.attributes].forEach(attr => {
        const ok =
          (el.tagName === 'A' && attr.name === 'href') ||
          (el.tagName === 'IMG' && attr.name === 'src');
        if (!ok) return el.removeAttribute(attr.name);
        if (/^javascript:|^data:/i.test(attr.value)) el.removeAttribute(attr.name); // 危险协议
      });
      if (el.tagName === 'A') {
        el.setAttribute('rel', 'noopener noreferrer');
        el.setAttribute('target', '_blank');
      }
      walk(el);
    });
  };
  walk(doc.body);
  return doc.body.innerHTML;
}
```

**评分点**：
- 用 DOMParser 解析成 DOM 再操作，绝不正则处理 HTML（错误模式识别）
- 未知标签「保留子内容、移除壳」，而非整段删除
- 危险协议（javascript:/data:）拦截是高频失分点
- 属性白名单逐标签区分；a 标签补 rel/target
