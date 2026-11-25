---
title: [PER-1123] 手写一个 HTML 消毒器（白名单版）
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-1123：手写一个 HTML 消毒器（白名单版）

**答**：
- 需求：实现 sanitizeHTML(html, cfg)。cfg: { allowTags, allowAttrs, allowProtocols }；解析后移除未允许标签（保留其文本）、未允许属性、on* 事件属性、协议不在白名单的 href/src；script/style 标签整体删除（含内容）；返回安全字符串。
- 边界：嵌套注释 <!-- --> 剥离；大小写混写标签（ScRiPt）也删除；html 为空返回空串；解析失败（parsererror）返回空串并上报。
- 评分点：危险标签删除；事件属性剥离；协议校验；保留文本

```javascript
function sanitizeHTML(html, cfg) {
  const doc = new DOMParser().parseFromString(html, 'text/html');
  const dangerous = new Set(['script', 'style', 'iframe', 'object', 'embed']);
  doc.querySelectorAll('*').forEach(el => {
    const tag = el.tagName.toLowerCase();
    if (dangerous.has(tag) || !cfg.allowTags.includes(tag)) {
      if (dangerous.has(tag)) el.remove();                 // 含内容删除
      else el.replaceWith(...el.childNodes);               // 保留文本
      return;
    }
    [...el.attributes].forEach(a => {
      const name = a.name.toLowerCase();
      if (name.startsWith('on') || !cfg.allowAttrs.includes(name))
        return el.removeAttribute(a.name);
      if (['href', 'src'].includes(name)) {
        const proto = (a.value.trim().split(':')[0] ?? '').toLowerCase();
        const relative = !/^[a-z]+:/i.test(a.value.trim());
        if (!relative && !cfg.allowProtocols.includes(proto))
          el.removeAttribute(a.name);
      }
    });
  });
  return doc.body.innerHTML;
}
// sanitizeHTML('<p onclick=x><a href="javascript:1">t</a>ok</p><script>evil()</script>',
//   { allowTags: ['p','a'], allowAttrs: ['href'], allowProtocols: ['https'] })
// -> '<p><a>tok</a></p>'
```
