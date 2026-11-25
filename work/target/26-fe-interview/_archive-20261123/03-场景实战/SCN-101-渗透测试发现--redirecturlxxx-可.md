---
title: [SCN-101] 渗透测试发现 /redirect?url=xxx 可以跳转到任意外部钓鱼站，如何修复开放重定向漏洞？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-101：渗透测试发现 /redirect?url=xxx 可以跳转到任意外部钓鱼站，如何修复开放重定向漏洞？
**答**：
- 修复原则：跳转目标只放行"站内相对路径"或白名单域名，其余一律回退默认页，绝不跟随用户提供的绝对地址。
- 两个绕过必须防：协议相对地址（//evil.com）会被解析为外部域名；URL 编码（https%3A%2F%2Fevil.com）要先 decode 再校验。
- 拦截事件本身上报监控，观察是否有真实攻击行为；必要时对可疑来源展示"即将跳转到 xxx"确认页作为兜底。

```javascript
// 开放重定向修复：decode 后白名单校验，仅放行站内路径
const TRUSTED_HOSTS = ['example.com', 'm.example.com'];

function safeRedirect(rawUrl, fallback = '/') {
  let url;
  try {
    // 先解码再解析，防编码绕过；相对路径以当前 origin 为基
    url = new URL(decodeURIComponent(rawUrl), location.origin);
  } catch {
    return fallback;
  }
  // 放行条件：同源相对路径，或 host 在白名单内
  if (url.origin === location.origin) return url.pathname + url.search;
  if (TRUSTED_HOSTS.includes(url.hostname)) return url.href;
  // 其余一律回退默认页
  report({ type: 'open-redirect-blocked', raw: rawUrl });   // 拦截记录，观察攻击
  return fallback;
}

// 使用：登录回跳
location.href = safeRedirect(getQueryParam('redirect'));
```
