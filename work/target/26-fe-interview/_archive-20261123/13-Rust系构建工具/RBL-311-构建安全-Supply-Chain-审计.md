---
title: [RBL-311] 构建供应链安全审计怎么做
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-311：构建供应链安全审计怎么做

**答**:
- 审计三层：依赖（lockfile 锁定 + pnpm audit/npm audit + SBOM 生成）、安装脚本（postinstall 是投毒主通道——pnpm 默认禁脚本，白名单放行）、工具二进制（Native binding hash 校验）
- 漏洞响应闭环：告警分级（可利用性评估：CVSS + 实际调用链）→ 修复窗口（critical 24h）→ 升级验证（回归测试）——告警不修等于没扫
- lockfile 纪律：CI 强制 frozen-lockfile、PR diff 审查 lockfile 变更（新增依赖必有人审）、禁 registry 漂移（.npmrc 锁 registry）
- SBOM：产物依赖清单（cyclonedx 格式）随发布存档——出 CVE 时分钟级定位受影响产物

```text
供应链基线：lockfile frozen + postinstall 白名单 + audit 分级响应 + SBOM 存档 + binding hash 校验
```
