---
title: [WEB-156] 什么是子域名接管（Subdomain Takeover）？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-156：什么是子域名接管（Subdomain Takeover）？
**答**：
- 场景：子域 CNAME 指向云资源（GitHub Pages、S3、云函数自定义域等），资源被删但 DNS 记录残留——任何人都能在云平台上认领该资源，直接控制这个子域的内容。
- 危害：在可信主域下挂钓鱼页、偷该域的 Cookie（父子域共享）、绕过基于域名的信任与 CSP。
- 发现方式：扫描子域的 CNAME 指向，再访问看是否出现云端特征 404/NXDOMAIN 页面。
- 治理：下线资源时同步删 DNS 记录；云资源保留防接管占位；CI 定期扫描告警。

```bash
# 探测残留的 CNAME：指向 GitHub Pages 但仓库已删除
dig +short abandoned.example.com CNAME
# 输出形如 app-obsolete.github.io，访问返回 GitHub 的 404 页面
curl -s -o /dev/null -w '%{http_code}\n' http://abandoned.example.com
# 返回 404 且页面含 There is not a GitHub Pages site here 类文案，即存在接管风险
```
