---
title: [ZSM-603] selector 开销的量化方法：怎么知道 selector 是热路径
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-603：selector 开销的量化方法：怎么知道 selector 是热路径

**答**：
- 判定标准：selector 单次执行耗时 × 执行频率。O(n) 的过滤 selector 在 5000 条列表上跑 3ms，一次 store 变更触发 200 个组件的 selector 重算 = 600ms 阻塞——单次不贵，乘上频率就是热路径。
- 量化手段一：**探针计时**——包一层 selector 计时器，累计 selfTime/calls，超阈值打点上报。开发期就能拿到「selector 排行榜」。
- 量化手段二：Chrome Performance 火焰图——React commit 前的「selector 重算块」通常在 getSnapshot / useSyncExternalStoreWithSelector 内联，找长条用户函数。
- 量化手段三：**变更放大系数**——`selector 执行次数 / 实际变更次数`，大于「订阅组件数」说明有重复订阅或风暴。
- 修复优先级排序的依据也是量化：修「平均耗时 × 频率」最高的 selector，而不是代码里看起来最丑的。修完复测同口径数据。

```javascript
// selector 计时探针
function profiledSelector(selector, label, { budget = 1 } = {}) {
  const stats = { calls: 0, total: 0, worst: 0 }
  return function (state) {
    const t0 = performance.now()
    const result = selector(state)
    const dt = performance.now() - t0
    stats.calls++
    stats.total += dt
    stats.worst = Math.max(stats.worst, dt)
    if (dt > budget) {
      console.warn(`[selector] ${label} ${dt.toFixed(2)}ms (calls=${stats.calls}, avg=${(stats.total / stats.calls).toFixed(3)}ms)`)
    }
    return result
  }
}

// 用法：包装怀疑的 selector
const useFilteredItems = () =>
  useStore(profiledSelector(
    (s) => s.items.filter((i) => i.active).sort((a, b) => b.score - a.score),
    'filteredItems',
    { budget: 2 }   // 单次超 2ms 告警
  ))

// 热路径判定公式
// selfTime = total；放大系数 = calls / storeChanges
// 排行榜：total 降序 → 修最上面
export function reportSelectorPerf() {
  return [...profStats.entries()]
    .map(([label, s]) => ({ label, ...s, avg: s.total / s.calls }))
    .sort((a, b) => b.total - a.total)
}
```
