---
title: [ENG-210] 依赖安全治理（SCA/供应链攻击）怎么体系化？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-210：依赖安全治理怎么体系化？
**答**：
- 三道防线：入库前（新依赖引入评审：维护活跃度/下载量/许可证/已知漏洞）、运行中（SCA 持续扫描 lockfile，CVE 告警分级）、构建时（锁文件校验 + 完整性：npm provenance/integrity）。
- 供应链攻击形态与对策：恶意新版本（锁死版本 + 升级时 diff 审查）、typosquatting（包名白名单校验）、install 脚本投毒（禁 postinstall 或白名单）、间接依赖投毒（SBOM 全量透明）。
- SBOM 实践：构建产出 SBOM（CycloneDX），事件发生时 5 分钟内回答「我们受影响吗、哪些产物含它」——没有 SBOM 的事后排查是数天级。
- 应急预案：核心依赖出 0day 的预案（降级路径/临时补丁 fork/registry 替代）。
- 追问钩子：为什么「lockfile 是安全边界」——lockfile 固定完整性 hash，CI 用 frozen install 确保构建产物与审查过的依赖树一致；绕过 lockfile 的 install 就打开了投毒入口。

```bash
# CI 三件套
pnpm audit --audit-level high          # CVE 扫描
pnpm install --frozen-lockfile        # lockfile 完整性
cyclonedx-npm --output-file sbom.json # SBOM 产出
# postinstall 白名单
# .npmrc: ignore-scripts=true（按需开启，显式允许必要脚本）
```
