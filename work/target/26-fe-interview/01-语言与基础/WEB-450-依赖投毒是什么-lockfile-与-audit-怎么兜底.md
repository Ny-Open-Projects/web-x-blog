---
title: [WEB-450] 依赖投毒是什么，lockfile 与 audit 怎么兜底
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-450：依赖投毒是什么，lockfile 与 audit 怎么兜底

**答**：
- 投毒形式：npm 包名抢注（typosquatting）、维护者账号被盗推恶意版本、install 脚本直接执行恶意代码
- 三道防线：lockfile 锁死版本与哈希（npm ci 安装）、`npm audit`/`osv-scanner` 查已知 CVE、CI 里禁 postinstall 或审计安装脚本
- 升级策略：固定小版本 + 定期 Dependabot/Renovate 批量升级，避免「半年不升级一次性升」
- 私有源：公司内部走 verdaccio/Artifactory 白名单源，屏蔽新包直装
- 兜底监控：构建产物做 SRI（外部 CDN 场景）+ 产物 diff 审查，防构建链路被投毒

```bash
npm ci --omit=dev          # 严格按 lockfile 装，不解析 semver
npm audit --production     # 只看运行时依赖的漏洞
cat package.json | jq '.scripts | keys' | grep -i prepare # 警惕可疑钩子
```
