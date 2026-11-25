---
title: [ZSM-645] staleTime 与 gcTime 三组合行为速查与误配诊断
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-645：staleTime 与 gcTime 三组合行为速查与误配诊断

**答**：
- 两个时间轴的语义：staleTime 管「**还要不要重新请求**」（新鲜期内挂载/聚焦/重连都不拉），gcTime 管「**没引用了缓存留多久**」（内存回收）。二者独立，gcTime 从最后一个 observer unmount 起算。
- 三组合速查：1) `staleTime: 0, gcTime: 5min`（默认）——挂载必拉；切走 5 分钟后缓存清除；2) `staleTime: Infinity, gcTime: Infinity`——一次拉取永续（配置/枚举类），注意内存不回收只适合小数据；3) `staleTime: 60s, gcTime: 30s`——新鲜期 60s 但 30s 无引用即被回收：新鲜数据没活到过期就没了，重新挂载还是拉。**gcTime ≥ staleTime 是常规配置**，反过来属合法但反直觉。
- 误配诊断三症状：1) 来回切 tab 每次闪骨架 → gcTime < 用户平均离开时长，调大 gcTime；2) 页面数据「太旧不更新」→ staleTime 太长且没有 invalidate 兜底；3) 请求风暴 → staleTime: 0 + 频繁 refetchOnWindowFocus + 多组件同 key（每次聚焦全量拉），收敛靠 staleTime 或精简订阅。
- invalidate 覆盖一切：invalidateQueries 强制标脏，staleTime: Infinity 也会重拉一次——「绝对新鲜」的正确写法是 staleTime: Infinity + 业务动作时显式 invalidate。
- 追问钩子：gcTime 清除只发生在「无 observer」时，正在渲染的组件不受影响；被清除后重新挂载 = 新 Query 实例 + 新请求（data 引用全新）。

```javascript
// 组合速查表
// | 场景          | staleTime | gcTime  | 行为 |
// |--------------|-----------|---------|------|
// | 交易实时数据   | 0         | 1min    | 挂载即拉，切走 1min 清 |
// | 半静态列表     | 60s       | 10min   | 60s 内挂载直接用缓存 |
// | 配置/枚举     | Infinity  | Infinity | 拉一次永续 |
// | 搜索结果      | 30s       | 30s     | 短期复用快速回收 |

// 误配诊断
// 症状1：切 tab 闪骨架 → gcTime 调大
useQuery({ queryKey: ['feed'], gcTime: 10 * 60 * 1000 })
// 症状2：数据陈旧 → staleTime 缩短或业务动作 invalidate
queryClient.invalidateQueries({ queryKey: ['static'] })   // Infinity 也能强制重拉
// 症状3：请求风暴 → 收敛
useQuery({ queryKey: ['todos'], staleTime: 30_000, refetchOnWindowFocus: false })
```
