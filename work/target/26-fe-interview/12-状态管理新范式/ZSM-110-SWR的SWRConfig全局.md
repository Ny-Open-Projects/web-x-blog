---
title: [ZSM-110] SWRConfig 全局配置怎么组织？fetcher、fallback 数据、按模块覆盖分别怎么做？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-110：SWRConfig 全局配置怎么组织？fetcher、fallback 数据、按模块覆盖分别怎么做？
**答**：
- 全局放通用项：统一 fetcher、dedupingInterval、重试策略、onError 上报；局部 useSWR 第三参覆盖默认值，配置就近优先。
- `fallback: { key: data }` 用于 SSR/预取数据注入：服务端取好的数据直接塞进缓存，客户端首屏零请求零 loading，是 SWR 版的 dehydrate/hydrate。
- fetcher 统一收口后，鉴权 token 刷新、错误规范化、埋点都只需写一处；组件里不允许再手写 fetch。
- fallbackData（单请求级）与 fallback（全局批量）并存：单卡测试用 fallbackData，整页预取用 fallback。

```javascript
import { SWRConfig } from 'swr'
import useSWR from 'swr'

// api/fetcher.js —— 统一收口
export const fetcher = async (url) => {
  const res = await fetch(url, { headers: authHeaders() })
  if (!res.ok) throw Object.assign(new Error(res.statusText), { status: res.status })
  return res.json()
}

export function Root({ preload }) {          // preload: 服务端预取结果
  return (
    <SWRConfig value={{
      fetcher,
      dedupingInterval: 2000,
      fallback: preload,                     // key -> data 注入缓存
      onError: (err, key) => report(err, key),
    }}>
      <App/>
    </SWRConfig>
  )
}

function UserCard() {
  const { data } = useSWR('/api/user', { fallbackData: guestProfile }) // 单卡兜底
  return <Avatar user={data}/>
}
```
