---
title: [PER-620] 前端如何防界面伪装类攻击（Trust UI 攻击）？地址栏伪装、全屏钓鱼与界面注入的防御
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-620：前端如何防界面伪装类攻击（Trust UI 攻击）？地址栏伪装、全屏钓鱼与界面注入的防御

**答**：
- 一族不依赖代码漏洞、纯靠视觉欺骗的攻击：**地址栏伪装**（全屏 API 全屏钓鱼页隐藏地址栏、Unicode 同形字符做仿冒域名）、**tabnabbing**（用户切走标签页后原页被改成钓鱼页）、**界面注入**（浏览器插件/网络注入改 UI）。
- 防御分层：站方可做的——外链强制 `rel=noopener noreferrer` 防 tabnabbing 反向利用（`window.opener` 控制）、关键页面 `Fullscreen` 前置确认与全屏状态标识、域名用 punycode 校验提示（显示 IDN 警告）；用户教育层的——支付页永不申请全屏。
- 浏览器已有防线：全屏时显示"xxx 正在全屏提示、IDN 同形字策略、跨域 opener 主动置空（现代浏览器 noopener 默认化）——站方要做的是不破坏这些防线（别用 `window.open` 带 opener 语义传递敏感页）。
- 检测清单：grep `window.open(` 是否传 opener；检查关键操作是否有来源可信标记（防插件注入改 UI——用 CSP 禁内联脚本让注入脚本难落地）。

```javascript

const trustUiDefense = {
  links: {
    rule: 'target=_blank 必须配 rel=noopener noreferrer',
    scan: /<a[^>]+target=["']_blank["'](?![^>]*noopener)/g, // CI 扫描正则
  },
  fullscreen: {
    rule: '支付/登录页禁止申请全屏；全屏退出按钮常驻',
    detect: document.fullscreenElement !== null,
  },
  opener: {
    rule: '敏感页 window.open 后立即 opener=null；现代浏览器默认 noopener',
    code: "const w = window.open(url); w.opener = null;",
  },
  idn: { rule: '外链展示前做 punycode/同形字检测，可疑域名标红' },
  note: '界面伪装攻击的防线一半在浏览器默认行为，站方职责是不破坏它们并补齐 opener/全屏两点',
};
console.log(trustUiDefense.note);
```
