---
title: [WEB-378] 前端埋点 SDK 和第三方脚本的安全审查清单有哪些？
date: 2026-11-18
categories: [网络与浏览器]
tags: [前端面试, 面试题或笔试题, 安全]
type: 面试题
---

## WEB-378：前端埋点 SDK 和第三方脚本的安全审查清单有哪些？
**答**：
- 来源：是否官方域名、是否走 SRI、域名是否进 CSP 白名单最小化；版本是否有已知 CVE。
- 行为：读哪些 storage/Cookie、发数据到哪（检查网络请求目的地）、是否执行 eval/动态 script 注入。
- 运维：稳定版锁版本不跟 latest、加载失败不影响主流程（异步+超时）、下线渠道留 DNS/DOM 清理（防子域劫持/残留引用）。

```javascript
const auditSDK = (sdk) => ({
  origin: new URL(sdk.url).hostname.endsWith('.trusted-cdn.com'),
  sri: !!sdk.integrity,
  data: sdk.requests.every(r => ALLOWED_TARGETS.includes(new URL(r).hostname)),
  eval: !sdk.usesEval,
});
console.log('第三方脚本 = 给别人同源执行权，按最高风险对待');
```
