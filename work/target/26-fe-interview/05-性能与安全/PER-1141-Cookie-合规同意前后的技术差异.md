---
title: [PER-1141] Cookie 合规：同意前后的技术差异怎么做
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1141：Cookie 合规：同意前后的技术差异怎么做

**答**：
- 规则：非必需 Cookie（分析/广告）同意前不得写入；必需 Cookie（会话/安全）可豁免但要在政策说明。
- 实现：CMP 拦截——同意前 SDK 不初始化、cookie 写入走 wrapper（非白名单直接拒绝）、同意后补初始化。
- 技术细节：页面加载时同步注入 CMP（避免竞态先写 cookie）；服务器端配合：未同意会话不种分析 cookie。
- 展示：同意横幅必须等权（拒绝与接受同样容易点击）。

```javascript
// Cookie 写入 wrapper
const NECESSARY = new Set(['session', 'csrf', 'lang']);
const origSet = document.cookie.bind(document);
Object.defineProperty(document, 'cookie', {
  set(v) {
    const name = v.split('=')[0].trim();
    if (!NECESSARY.has(name) && !consent.get().analytics) {
      report({ type: 'cookie-blocked', name });
      return v;                                   // 拒绝写入
    }
    return origSet(v);
  },
  get() { return origGetCookie(); },
});
// CMP 初始化时序：内联脚本在 head 最前，先于一切分析 SDK
```
