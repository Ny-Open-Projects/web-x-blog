---
title: [ZSM-105] SWR 有哪些自动重验证触发时机？revalidateOnFocus 的原理是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-105：SWR 有哪些自动重验证触发时机？revalidateOnFocus 的原理是什么？
**答**：
- 内置触发时机：组件挂载遇到 stale 缓存、浏览器 `visibilitychange` 变为可见、网络 `online` 事件、dedupingInterval 过期后的新订阅。
- revalidateOnFocus 原理：SWR 全局监听 `document.visibilityState` 与 `focus` 事件，恢复可见时对「当前活跃组件订阅的 key」批量触发 revalidate——适合切标签比价、回来看消息这类场景，IM/行情类业务体验提升明显。
- 三个总开关：`revalidateOnFocus`、`revalidateOnReconnect`、`revalidateIfStale`，都可全局配置或按请求覆盖；低频后台类页面建议关 focus 重验证省流量。
- 追问钩子：配合 `refreshInterval` 可做轮询，`refreshWhenHidden: true` 还能在后台标签继续轮询（默认暂停），面试可延伸到「可见性驱动的取数」设计。

```javascript
import { SWRConfig } from 'swr'

// 全局默认：办公内网看板场景
<SWRConfig value={{
  revalidateOnFocus: true,
  revalidateOnReconnect: true,
  dedupingInterval: 2000,      // 2s 内同 key 请求合并
  focusThrottleInterval: 5000, // 焦点重验证节流
}}>
  <App/>
</SWRConfig>

// 行情组件：后台也持续轮询
function Ticker({ symbol }) {
  const { data } = useSWR(`/api/quote/${symbol}`, fetcher, {
    refreshInterval: 3000,
    refreshWhenHidden: true,    // 默认 false：页面隐藏时暂停轮询
    refreshWhenOffline: false,
  })
  return <span>{data?.price}</span>
}
```
