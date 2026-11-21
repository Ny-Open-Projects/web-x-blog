---
title: [WEB-523] 供应链安全的依赖治理 SOP
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-523：供应链安全的依赖治理 SOP

**答**：
- 盘点先行：建立 SBOM（依赖清单），知道「我们到底用了什么、谁的版本多旧」——多数团队第一步就缺
- 常态机制：CI 里跑 audit/osv 扫描 + lockfile 强制（npm ci）+ Dependabot 定期升级；高危 CVE 24h 内响应
- 引入新包三问：是否真的需要（20 行代码自己写）、维护活跃度、下载量与近期发布记录——防 typosquatting
- 运行时防线：CSP 限制外联、SRI 校验 CDN 资源、产物构建后 diff（防构建链被投毒）
- 事故预案：应急版本 pinned 回退流程 + 影响面评估（哪些业务用了被投毒的包）

```bash
npm ls --all > sbom.txt                    # 依赖树盘点
npx osv-scanner --lockfile=package-lock.json
grep -rn "postinstall\|preinstall" */package.json # 审计安装钩子
```
