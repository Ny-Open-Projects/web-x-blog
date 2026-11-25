---
title: [NODE-719] 服务端安全加固清单有哪些？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 面试题, Node.js与BFF]
type: 面试题
---

## NODE-719：安全加固清单有哪些？
**答**：
- 输入面：schema 校验全接口（SCN-NODE-695）、SQL 注入防御（参数化查询强制——ORM 默认+审计）、SSRF 防御（出站 URL 白名单——用户可控 URL 的出站调用）、路径穿越（文件接口路径归一化校验）。
- 输出面：安全响应头（helmet——CSP/XFO/HSTS，SCN-BLD-246）、错误脱敏（SCN-NODE-676）、日志脱敏（SCN-NODE-698）。
- 依赖面：SCA 扫描（SCN-ENG-210）、install 脚本禁用、lockfile 冻结。
- 运行面：最小权限（容器非 root——文件系统只读）、进程隔离、诊断端点内网（SCN-NODE-704）、secrets 管理（SCN-ENG-229）。
- 追问钩子：为什么「SSRF 防御」在服务端安全清单里最容易被漏——SSRF 的入口是「服务端代发请求」的场景（webhook/URL 预览/文件导入——业务特性决定），没有通用中间件可覆盖；攻击目标是内网（metadata 服务/内网 API）——每个「服务器代发请求」的功能点都要单独做 URL 白名单校验（含 DNS rebinding 防御——解析后校验 IP）。

```javascript
// SSRF 防御
async function safeFetch(userUrl) {
  const url = new URL(userUrl);
  if (!ALLOWED_HOSTS.includes(url.hostname)) throw new Error('SSRF_BLOCKED');
  const ip = await dns.lookup(url.hostname);           // DNS 解析后校验（防 rebinding）
  if (isInternalIp(ip.address)) throw new Error('INTERNAL_BLOCKED');   // 内网 IP 拒绝
  return fetch(userUrl, { redirect: 'error' });        // 禁重定向（重定向绕过）
}
```
