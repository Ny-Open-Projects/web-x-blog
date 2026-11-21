---
title: [NODE-131] 依赖供应链安全如何审计（npm audit 与 lock 完整性）？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-131：依赖供应链安全如何审计（npm audit 与 lock 完整性）？
**答**：
- 三条攻击面：恶意版本（typosquatting）、已有包被投毒（事件溯源 script）、传递依赖里的漏洞——`package-lock.json` 是唯一事实源。
- CI 必做：`npm ci --ignore-scripts`（锁精确安装 + 跳过 install 脚本）、`npm audit` 高危阻断、审计 pre/postinstall 脚本。
- 治理机制：Renovate/Dependabot 自动提 PR、新依赖引入走 review（周下载量/维护活跃度/是否首包）、私有 registry 托管关键依赖。
- 应急预案：某依赖爆雷时能快速定位"谁引用了它"（`npm ls pkg --all`）并 pin 到安全版本。

```bash
# 1. CI 审计：高危漏洞阻断合并
npm audit --audit-level=high

# 2. 锁定安装 + 跳过安装脚本（防 postinstall 投毒）
npm ci --ignore-scripts
grep -E '"(pre|post)?install"' package-lock.json | head  # 人工复审带脚本依赖

# 3. 溯源：谁引入了有问题的包
npm ls lodash --all
npm audit --json | jq '.vulnerabilities | to_entries[] | {name: .key, via: .value.via}'

# 4. 收紧发布面：禁止本仓库发未审计包；.npmrc 指向私有 registry
# registry=https://registry.npmmirror.com
# @company:registry=https://npm.internal.company.com
```
