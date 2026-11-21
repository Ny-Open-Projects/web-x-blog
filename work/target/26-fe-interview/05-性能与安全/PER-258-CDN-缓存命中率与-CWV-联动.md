---
title: [PER-258] CDN 缓存命中率如何影响 TTFB 与 LCP？命中率调优的排查路径是什么？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-258：CDN 缓存命中率如何影响 TTFB 与 LCP？命中率调优的排查路径是什么？

**答**：
- 影响机理：CDN 未命中就要回源，TTFB 从几十 ms 涨到几百 ms；LCP 的地板直接抬高。HTML 是"不可缓存"默认值的重灾区（大量站点 HTML 不设缓存导致每用户每次都回源）。
- 排查路径：① 看 CDN 面板命中率分资源类型——静态资源命中率 < 95% 先查缓存 key（是否带无意义 query、Cookie 参与了 key）；② HTML 命中策略：s-maxage 短缓存 + stale-while-revalidate（边缘旧内容立即返回，后台刷新），配合版本化发布（HTML 指向 hash 资源）；③ 回源慢：源站预热带 + 边缘预热 API（发布时主动预热新版本）。
- 验证：RUM 按"边缘命中/回源"（CDN 响应头 X-Cache）分组看 TTFB 分布，命中组的 p75 应显著低于回源组；差值即优化收益上限。
- 面试要点：能说出"HTML 缓存 + SWR + 发布预热"这套组合拳，以及为什么静态资源命中率高但 TTFB 依旧差（瓶颈在 HTML）。

```text
缓存策略样板（HTML + 静态资源）：
HTML:  Cache-Control: max-age=0, s-maxage=60, stale-while-revalidate=300
       # 用户永远拿新 HTML（边缘 60s 内直接给 + 后台刷新），发布即预热
静态:  Cache-Control: public, max-age=31536000, immutable   # hash 文件名 + 一年缓存
API:   GET 列表可配 s-maxage=10 + SWR 60（允许边缘秒级旧数据）
验收分组：X-Cache: HIT 的 TTFB p75 应 < 80ms；MISS 组差值即回源成本
```
