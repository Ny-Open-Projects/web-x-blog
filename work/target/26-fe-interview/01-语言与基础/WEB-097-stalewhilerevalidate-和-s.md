---
title: [WEB-097] stale-while-revalidate 和 stale-if-error 分别解决什么问题？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-097：stale-while-revalidate 和 stale-if-error 分别解决什么问题？
**答**：
- `stale-while-revalidate=N`：保鲜期过后 N 秒内，先用旧内容立即响应，同时后台异步刷新——用户零等待，内容最终一致。
- `stale-if-error=N`：源站故障（5xx/断网）时 N 秒内回退到过期缓存，牺牲新鲜度换可用性。
- 两者都只对"允许过期使用"的缓存有意义，常与 max-age 组合；CDN 与现代浏览器均已支持。
- 适用：容忍短暂陈旧的内容（列表页、配置 JS）；支付余额等强一致内容不要用。

```http
HTTP/1.1 200 OK
Cache-Control: max-age=60, stale-while-revalidate=30, stale-if-error=86400
Content-Type: application/json

# 时间线解读：
# 0-60s    强缓存命中，零请求
# 60-90s   先返回旧数据（毫秒级），同时后台向源站重新验证，结果回填缓存
# 90s+     后台刷新完成，恢复正常强缓存；若期间源站 5xx，1 天内继续兜底旧数据
# 前端无感知：请求既快又不断流，代价是可能读到最长 90 秒前的数据
```
