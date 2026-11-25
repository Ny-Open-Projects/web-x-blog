---
title: [PER-1078] 富文本编辑器的 XSS 防护怎么做
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1078：富文本编辑器的 XSS 防护怎么做

**答**：
- 双层消毒：粘贴时 sanitize（DOMPurify 白名单标签/属性）+ 渲染时再 sanitize（不信任任何"已消毒"声明）。
- 白名单而非黑名单：只允许有限标签与安全属性（class/style 白名单值），事件属性与 javascript: URI 一律剥离。
- 样式风险：CSS 注入可外链（background:url）泄露，style 属性需值级校验。
- 协作编辑场景：服务端入库前也必须消毒（客户端不可信），且版本升级要重新校验历史数据。

```javascript
import DOMPurify from 'dompurify';
const CFG = {
  ALLOWED_TAGS: ['p', 'b', 'i', 'u', 'a', 'img', 'ul', 'ol', 'li', 'br', 'strong', 'em', 'blockquote'],
  ALLOWED_ATTR: ['href', 'src', 'alt', 'class'],
  ALLOW_DATA_ATTR: false,
};
DOMPurify.addHook('uponSanitizeAttribute', (node, data) => {
  if (data.attr === 'style') {                       // style 值级白名单
    data.keepAttr = /^(color:\s*#\w{3,6};?|font-size:\s*\d+(px|rem);?)*$/.test(data.attrValue);
  }
  if (data.attr === 'href' || data.attr === 'src')
    data.keepAttr = /^(https?:|\/|mailto:)/i.test(data.attrValue ?? '');  // 禁 javascript:
});
export const cleanRichText = html =>
  DOMPurify.sanitize(html, { ...CFG, RETURN_TRUSTED_TYPE: false });
```
