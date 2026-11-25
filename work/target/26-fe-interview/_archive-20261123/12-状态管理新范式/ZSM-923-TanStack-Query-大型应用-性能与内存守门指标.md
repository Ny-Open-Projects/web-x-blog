---
title: [923] TanStack Query 的性能与内存守门指标
date: 2026-11-17
categories: [状态管理新范式]
tags: [前端面试, 面试题, TanStack Query, 性能]
type: 面试题
---

## 923：TanStack Query 的性能与内存守门指标

**答**：
- 指标三组：请求健康（缓存命中率、同 Key 并发重复率——重复 = Key 设计烂）、内存（缓存条目数/最大单条体积——无限列表与大数据对象是膨胀源）、渲染（useQuery 引起的重渲染次数——select 收窄 + 结构共享让无关字段更新不渲染）。
- 守门手段：devtools 缓存体积巡检（人工+脚本扫大条目）、CI 请求计数断言（关键页面挂载请求次数不回退——防瀑布回归）、结构共享验证（无关更新时对象引用不变测试）。
- 结构共享的重要性：Query 默认 replaceEqualDeep——列表改一条，未变项引用不变（React.memo 子组件不重渲染）；关掉它大列表全量重渲染。
- 追问钩子：为什么 select 要引用稳定？——select 每次返回新对象会让组件认为 data 变了（即使源数据没变），内联箭头 + 非浅比较 = 重渲染风险。

```ts
useQuery({ queryKey: ['big', id], queryFn, select: useCallback(
  d => ({ items: d.items.map(pickBrief) }), []),        // select 收窄+引用稳定
  structuralSharing: true,                              // 默认开启别关
});
```

