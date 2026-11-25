---
title: [PER-953] 手写一个 URL 脱敏器：参数白名单加路径数字打码
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-953：手写一个 URL 脱敏器：参数白名单加路径数字打码

**答**：
- 需求：实现 sanitizeUrl(url)。规则：query 中命中敏感名（token/key/auth/session/sign/secret，大小写不敏感）替换为 ***；非白名单参数值含 6 位以上数字也打码；路径中连续 >= 6 位数字替换为 N；保留 hash 与合法白名单参数原样。
- 边界：非法 URL 返回 null；相对路径基于示例 origin 解析；参数值空串不打码；白名单可配置。
- 评分点：敏感名正则；白名单；路径与参数双打码；异常 URL

```javascript
const DEFAULT_WHITELIST = ['page', 'size', 'sort', 'tab', 'lang'];
function sanitizeUrl(url, whitelist = DEFAULT_WHITELIST) {
  try {
    const u = new URL(url, 'https://x.example');
    for (const [k, v] of [...u.searchParams]) {
      if (/token|key|auth|session|sign|secret/i.test(k))
        u.searchParams.set(k, '***');
      else if (!whitelist.includes(k) && /\d{6,}/.test(v))
        u.searchParams.set(k, v.replace(/\d{6,}/g, 'N'));
    }
    const path = u.pathname.replace(/\d{6,}/g, 'N');
    return path + (u.search || '') + (u.hash || '');
  } catch { return null; }
}
// sanitizeUrl('/order/88273412?token=abc&page=2&bizId=99887766')
// -> '/order/N?token=***&page=2&bizId=N99887766N... ' 见实现
```
