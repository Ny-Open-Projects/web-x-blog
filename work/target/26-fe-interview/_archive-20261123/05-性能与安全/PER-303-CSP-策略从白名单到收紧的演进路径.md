---
title: [PER-303] 大型存量站点如何把 CSP 从"几乎不拦"演进到严格白名单？路线图怎么排？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-303：大型存量站点如何把 CSP 从"几乎不拦"演进到严格白名单？路线图怎么排？

**答**：
- 存量站点不能一步到位：几十个页面、上百个三方脚本、历史内联脚本遍地都是，直接上严格策略等于全站故障。演进核心是 report-only 先行 + 按域分批收敛。
- 路线图四阶段：① `Content-Security-Policy-Report-Only` 全量部署 4~8 周，只收集不拦截，产出"违规来源 Top 清单"（哪些内联、哪些三方域、哪些 eval）；② 逐类消化——三方脚本收敛到统一网关/白名单域、内联脚本改 nonce 或外链化、eval 场景逐个改造（JSON.parse 替代 eval、模板引擎换安全版）；③ 分业务线切强制（`script-src 'self' 'nonce-xxx'`），先低流量线验证；④ 收紧到 hash/nonce + `strict-dynamic`，删掉宽松的 `unsafe-inline`/`unsafe-eval`/宽域白名单。
- 收紧纪律：每一步都有 report 数据支撑（违规量降到 < 1/百万 PV 才切下一档）；每次收紧保留 report-uri 双头（强制 + report-only 精细版）持续观察。
- 与前端工程配合：构建期给每个 script 注入 nonce（模板层）、开发环境用宽松策略或 meta CSP 提示，避免"开发没问题上线全红"。

```text
阶段化策略示例（同一站点）：
阶段1: Report-Only: script-src 'self' https:; report-uri /csp-report
        # 只收集：发现 200 个三方域、300 处内联
阶段2: 强制 script-src 'self' cdn.trusted-list... + 'unsafe-inline'（过渡）
阶段3: script-src 'self' cdn.example.com 'nonce-{RANDOM}' 'strict-dynamic'
        report-uri /csp-report   # nonce + strict-dynamic：动态加载由已信任脚本授权
阶段4: 删 report-only、白名单收敛到 5 个域、加 frame-ancestors 'none'
验收指标：拦截率 < 0.001%、业务报错 0、XSS 事件 0
```
