---
title: [PER-622] 前端如何安全处理 URL 跳转（开放重定向）？返回链接 returnTo 的校验怎么做？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-622：前端如何安全处理 URL 跳转（开放重定向）？返回链接 returnTo 的校验怎么做？

**答**：
- 开放重定向危害：`/login?returnTo=https://evil.com` 钓鱼跳转、配合 OAuth 授权码窃取（redirect_uri 换成攻击者域）；前端常见载体是 `returnTo/redirect/backurl` 参数与 `history.back` 替代逻辑。
- 校验规则：**同源优先**——只允许以 `/` 开头的站内相对路径（禁止 `//`、`/\`、`https://` 开头的绝对 URL）；确需跨域白名单（如跳子域），做 origin 白名单精确匹配；禁止协议相对 URL 与控制字符（`\r\n` 防响应拆分）。
- 落地封装：统一 `safeRedirect(param)` 函数收口所有跳转点，非法值回退默认页而不是报错；OAuth redirect_uri 是服务端职责，前端要保证不自行拼接。
- 测试用例清单固化进 CI：`https://evil.com`、`//evil.com`、`/\evil.com`、`javascript:alert(1)`、`/abc\r\nX`、`%2f%2fevil.com` 等变体全部断言被拒。

```javascript

function safeRedirect(param, fallback = '/') {
  const raw = param ?? '';
  const decode = (s) => { try { return decodeURIComponent(s); } catch { return ''; } };
  const url = decode(raw.trim());
  // 1) 仅允许站内相对路径
  if (!url.startsWith('/') || url.startsWith('//') || url.startsWith('/\\')) return fallback;
  // 2) 协议与控制字符兜底
  if (/^[a-z][a-z0-9+.-]*:/i.test(url) || /[\r\n]/.test(url)) return fallback;
  // 3) 跨域白名单（按需启用）
  const CROSS = ['https://vip.example.com'];
  if (CROSS.includes(new URL(url, location.origin).origin) === false &&
      new URL(url, location.origin).origin !== location.origin) {
    return fallback;
  }
  return url;
}
// CI 用例表：
const CASES = ['https://evil.com', '//evil.com', '/\\evil.com', 'javascript:alert(1)',
  '/a\r\nb', '%2f%2fevil.com', '/ok/path?q=1'];
CASES.forEach(c => console.log(c, '->', safeRedirect(c)));
```
