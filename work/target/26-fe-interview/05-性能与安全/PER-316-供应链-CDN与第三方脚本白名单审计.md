---
title: [PER-316] 页面加载了 30 个第三方脚本，如何做"来源审计"并收敛到最小白名单？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-316：页面加载了 30 个第三方脚本，如何做"来源审计"并收敛到最小白名单？

**答**：
- 盘点：Production 抓取（Lighthouse third-party 报告 / Performance 面板 Third-party track / RUM 按资源域聚合），产出清单：域、脚本、体积、阻塞时长（LoAF）、加载方式（同步/异步）、调用方（哪个业务引入）。
- 逐项裁决：四选一——必须同步（极少，如合规组件）→ 收进白名单 + SRI；可异步/延迟 → 统一加载器；可用 facade → 替换；无人认领/僵尸 → 下线。审计的常见发现：30 个里 8 个早已没人用。
- 收敛手段：统一三方网关（一个域出全部三方脚本，白名单一个域搞定 CSP 与 SRI）；版本锁定（网关侧固定 SDK 版本，供应商更新走评审）；CI 卡口（新 script.src 必须在白名单清单内，PR diff 有新域即拦）。
- 持续化：白名单清单进仓库版本管理，审计季度化；RUM 持续按域归因阻塞时长，新增域自动出现在周报里。

```text
第三方脚本审计表（样例）：
域                     脚本           体积   阻塞   方式     裁决
maps.example.com      sdk.js         890KB  340ms  同步     → facade（点击加载）
stats.ad.com          tracker.js     45KB   210ms  同步     → idle 延迟
chat.biz.io           widget.js      220KB  180ms  异步     → 保留（网关统一出）
legacy.jquery.com     jquery.js      90KB   120ms  同步     → 下线（无人认领 18 个月）
…
收敛结果：30 → 9 个，全部经统一网关域 + 白名单 + SRI；CSP script-src 收敛到网关域
```
