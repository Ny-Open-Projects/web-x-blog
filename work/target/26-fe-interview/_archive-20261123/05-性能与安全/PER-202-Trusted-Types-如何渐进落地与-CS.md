---
title: [PER-202] Trusted Types 如何渐进落地？与 CSP、DOMPurify 怎么配合？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-202：Trusted Types 如何渐进落地？与 CSP、DOMPurify 怎么配合？

**答**：
- 机制：CSP 头 `require-trusted-types-for 'script'` 让 `innerHTML/outerHTML`、`eval`、`script.src`、`iframe.srcdoc`、`document.write` 等典型 DOM-XSS sink **只接受 TrustedTypes 对象**（TrustedHTML/TrustedScript/TrustedScriptURL），直接塞字符串抛 TypeError——把"XSS 静默利用"变成"报错即可见"。
- 2025-2026 支持口径：Chrome/Edge 83 起长期支持；Safari 18.2、Firefox 135（2025 年，先实验性随后默认开启）相继跟进，三大引擎齐备。生产强制前仍建议查 caniuse 确认目标用户版本，并留足 report-only 观察期。
- 渐进启用三步：`Content-Security-Policy-Report-Only` 收集 sink 违规清单摸清迁移面 → 逐类适配显式 policy + `default` policy 兜底 → 切强制并保留 `report-uri` 监控。先 report-only 再强制是不可跳过的纪律，否则上线即大面积功能报错。
- 配套：DOMPurify 在支持 Trusted Types 的环境自动返回 TrustedHTML，可直接作为 policy 的清洗实现；旧浏览器用 polyfill 只做类型检查、不提供真实防护，必须由 CSP 兜底；`trustedTypes.defaultPolicy` 兜底所有未显式适配的 sink——强制期后建议把 default policy 从"清洗放行"收紧为"直接抛错"，逼出遗漏点。

```javascript
// 1. 默认 policy：迁移期兜底（清洗放行，防遗漏变 XSS；稳定后可收紧为抛错）
const ALLOWED_SCRIPT_HOSTS = new Set(['cdn.example.com', 'static.example.com']);

if (window.trustedTypes) {
  trustedTypes.createPolicy('default', {
    createHTML: (s) => DOMPurify.sanitize(s),        // 默认清洗而不是原样放行
    createScriptURL: (s) => {
      const url = new URL(s, location.origin);
      if (ALLOWED_SCRIPT_HOSTS.has(url.host)) return s;        // 白名单校验
      throw new TypeError(`script.src 不在白名单: ${s}`);
    },
    createScript: () => { throw new TypeError('eval 类 sink 全局禁用'); },
  });
}

// 2. 显式 policy：业务模块专用，类型不可与裸字符串混淆
const commentPolicy = window.trustedTypes
  ? trustedTypes.createPolicy('comment', {
      createHTML: (s) => DOMPurify.sanitize(s, { ALLOWED_TAGS: ['b', 'i', 'a'], ALLOWED_ATTR: ['href'] }),
    })
  : { createHTML: (s) => DOMPurify.sanitize(s) };    // 不支持 TT 的环境退化为纯清洗

el.innerHTML = commentPolicy.createHTML(userInput);
// 强制模式下：el.innerHTML = userInput 直接 TypeError，漏网的注入在开发期就暴露
```

```http
# 第一步：只上报不拦截，摸清 sink 违规面（观察期至少一个迭代）
Content-Security-Policy-Report-Only: require-trusted-types-for 'script'; report-uri /csp-report

# 第二步：违规清零后切强制，保留上报通道监控回归
Content-Security-Policy: require-trusted-types-for 'script'; report-uri /csp-report
```
