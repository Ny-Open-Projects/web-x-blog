---
title: [PER-363] 一个真实站点的 CSP 迁移案例：从 Report-Only 到 strict-dynamic 的 12 周路线？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-363：一个真实站点的 CSP 迁移案例：从 Report-Only 到 strict-dynamic 的 12 周路线？

**答**：
- 周期拆解（可复用的模板）：W1-2 Report-Only 全量部署，产出违规基线（220 个三方域、380 处内联、40 处 eval）；W3-4 三方收敛——按"无人认领即下线、可异步即网关化"把域从 220 → 34，内联脚本外链化 300 处，eval 改造（模板引擎替换）；W5-6 分业务线切强制（先内部工具站验证策略正确性，再切低流量业务）；W7-8 引入 nonce（SSR 模板注入）+ strict-dynamic，处理动态 chunk 与三方 loader 的信任链；W9-10 收紧 unsafe-inline/宽域移除，report 监控持续；W11-12 稳定观察 + 全量推广 + 文档沉淀。
- 关键数据：违规量曲线（周报）、拦截误伤数（业务报错）、最终策略文本、收益（XSS 攻击 report 归零、白名单域从 220 → 12）。
- 踩坑记录：CDN 缓存的旧 HTML 带旧 nonce 导致误拦（切 hash/边缘改写解决，PER-306）；某个三方 SDK 用 eval 兜底（供应商版本升级解决）；report-uri 被爬虫刷量（限流 + UA 过滤）。
- 可复用结论：report 期 ≥ 4 周才切强制；每步只动一个变量；白名单收敛靠"下线"而不是"加白"。

```text
迁移周报曲线（关键指标）：
W2: 违规 12.4 万/周（三方 220 域、内联 380、eval 40）
W4: 违规 2.1 万/周（三方 34 域、内联 80）—— 消化完成 83%
W6: 首个业务线强制，拦截 0、误伤 0 → 扩量
W8: nonce + strict-dynamic 上线，动态 chunk 正常
W10: 移除 unsafe-inline/unsafe-eval，白名单 12 域
W12: 违规 < 100/周（残留为爬虫噪音），XSS report 归零，推广全站
```
