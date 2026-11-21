---
title: [ALG-171] 富文本评论区允许用户发 `<b>`、`<a>` 等标签，但要防 XSS。如何实现一个简化 DOMPurify（白名单过滤）？
date: 2026-11-17
categories: [场景算法]
tags: [前端面试, 笔试题, 15]
type: 笔试题
---

## ALG-171：富文本评论区允许用户发 `<b>`、`<a>` 等标签，但要防 XSS。如何实现一个简化 DOMPurify（白名单过滤）？
**答**：白名单而非黑名单：用 `DOMParser` 解析后遍历 DOM 树，不在标签白名单的直接移除，不在属性白名单的直接删除，`javascript:` 伪协议的 href 额外拦截；外链补 `rel="noopener noreferrer"`。要点：① 黑名单永远漏（svg/mathml/大小写/编码绕过），白名单宁缺勿滥；② 产出用 innerHTML 前确认树里已无危险节点；③ 生产直接用 DOMPurify，此为原理演示。O(节点数)。

```javascript
const ALLOWED_TAGS = new Set(['p', 'b', 'i', 'a', 'ul', 'ol', 'li', 'br', 'span']);
const ALLOWED_ATTR = new Set(['href', 'class']);
function sanitize(html) {
  const root = new DOMParser().parseFromString(html, 'text/html').body;
  const walk = node => {
    [...node.children].forEach(el => {
      if (!ALLOWED_TAGS.has(el.tagName.toLowerCase())) return el.remove(); // 白名单外移除
      [...el.attributes].forEach(a => {
        const unsafe = !ALLOWED_ATTR.has(a.name) ||                        // 属性白名单
          (a.name === 'href' && /^\s*javascript:/i.test(a.value));         // 伪协议拦截
        if (unsafe) el.removeAttribute(a.name);
      });
      if (el.tagName === 'A' && el.hasAttribute('href')) {
        el.setAttribute('rel', 'noopener noreferrer');                     // 防 window.opener
      }
      walk(el);
    });
  };
  walk(root);
  return root.innerHTML;
}
// sanitize('<p onclick="alert(1)">hi<script>x</script></p>') => '<p>hi</p>'
```
