---
title: [PER-315] 什么是 SBOM？高危 CVE 爆出时如何 1 小时内回答"我们受影响吗"？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-315：什么是 SBOM？高危 CVE 爆出时如何 1 小时内回答"我们受影响吗"？

**答**：
- SBOM（Software Bill of Materials，软件物料清单）：机器可读的"项目用了哪些组件+版本"清单，格式如 SPDX/CycloneDX。价值不是合规挂图，而是漏洞响应时**反查**——CVE 通告给出受影响包与版本区间，SBOM 一查即知哪些项目哪个版本命中。
- 生成与维护：构建期自动生成（`npm sbom` / cyclonedx-bom 工具），随产物归档；覆盖传递依赖（lockfile 全量）；每次发布更新版本。没有 SBOM 的团队只能全仓 grep 撞运气。
- 响应流程（目标 1 小时）：① SBOM 检索命中清单（哪些项目/版本在受影响区间）；② 判断可达性——依赖被"真正引入运行时"还是仅 devDependency/未调用（减少误报）；③ 升级/补丁评估（是否有修复版本、lock 最小变更 diff）；④ 热修发布或临时缓解（WAF 拦特征、下线功能）。
- 度量：漏洞响应 MTTR、SBOM 覆盖率（多少项目有自动 SBOM）、CVE 误报率。

```bash
# 生成（构建 CI 中）：CycloneDX 格式
npx @cyclonedx/bom . --output-file sbom.json
# CVE 爆出后的反查（伪 SQL）：
# SELECT project, version FROM sbom
# WHERE package = '<cve_pkg>' AND version IN (<affected_range>) AND dep_type = 'prod';
# => 命中清单 5 分钟出，含"是否运行时可达"标注
```
