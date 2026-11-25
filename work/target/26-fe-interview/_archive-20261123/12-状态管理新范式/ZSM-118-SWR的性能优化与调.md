---
title: [ZSM-118] 一个页面几十个 useSWR 会不会有性能问题？SWR 的性能调优手段有哪些？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-118：一个页面几十个 useSWR 会不会有性能问题？SWR 的性能调优手段有哪些？
**答**：
- 机制上 SWR 按 key 订阅，单 key 更新只重渲染订阅组件，几十个独立 useSWR 本身没问题；真正的坑是「一个 key 被塞进巨型对象」导致全订阅者重渲染。
- 调优手段：key 拆细粒度（列表 key + 详情 key 分开）；fetcher 返回结构共享（SWR v2 内置对返回值做浅/深比较，引用不变不重渲染）；列表项数据裁剪；重验证节流（focusThrottleInterval）。
- 用 `useSWRConfig().cache` 做缓存体检：开发期打印 key 数量与体积，找出超大缓存条目。
- 对比 Zustand selector 思路一致——「订阅粒度与更新粒度对齐」，能跨库总结出这条规律是加分项。

```javascript
// 反模式：整页数据一个 key，任何字段变都全页重渲染
const { data: page } = useSWR('/api/dashboard', fetcher)

// 正解：按卡片拆 key，互不影响
function StatCard({ metric }) {
  const { data } = useSWR(`/api/metrics/${metric}`)  // 只订阅自己的 key
  return <div>{data?.value}</div>
}

// 缓存体检：定位大条目
function CacheAudit() {
  const { cache } = useSWRConfig()
  useEffect(() => {
    const sizes = [...cache.keys()].map(k => [k, JSON.stringify(cache.get(k)).length])
    console.log(sizes.sort((a, b) => b[1] - a[1]).slice(0, 10)) // Top10 大 key
  }, [])
  return null
}
```
