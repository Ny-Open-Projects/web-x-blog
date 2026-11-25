---
title: [ZSM-643] Query 缓存的通知扇出：一次 setData 通知了多少 observer
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-643：Query 缓存的通知扇出：一次 setData 通知了多少 observer

**答**：
- 扇出路径：`query.setData()` → `query.observers.forEach(o => o.updateResult())` → 每个 observer 跑 select/比较 → **只在选出的结果变化时才 setState 通知组件**。扇出成本 = observer 数 × updateResult 成本（含 select 执行），React 渲染成本 = 结果真正变化的组件数。
- 两个优化闸门：1) **observer 内的结果比较**——updateResult 先算新结果，与上次结果 `replaceEqualDeep`/浅比较，相同则不通知（这就是 select 返回稳定引用的价值）；2) **notifyBatch**——同一 tick 内多次 setData 合并成一轮通知（批处理，类似 React batching）。
- 诊断扇出：给 observer 挂探针统计 `notify 次数 / setData 次数` 比值——比值 > 组件数说明有重复通知或风暴；给 React 渲染挂 Profiler 统计「每条通知触发的重渲数」。
- 大扇出场景：`invalidateQueries({ queryKey: ['todos'] })` 命中 50 个缓存条目 × 每 10 个 observer = 500 次 updateResult——大批量失效要评估扇出量，或改用更精确的 key。
- 追问钩子：v5 的 observer 通知走 `emitter` 事件（cache 的 subscribe 是给 devtools/invalidate 用的）——事件源分层：Query 层事件（数据变了）vs Observer 层事件（结果变了），下游订阅后者。

```javascript
// 通知扇出骨架
class Query {
  observers = []
  setData(data, opts) {
    const prevResult = this.observers[0]?.currentResult
    this.state = nextState
    // 批处理：同 tick 合并
    this.notifyCount = (this.notifyCount ?? 0) + 1
    if (!scheduled) {
      scheduled = true
      queueMicrotask(() => {
        scheduled = false
        let notified = 0
        for (const o of this.observers) {
          const newResult = o.updateResult()      // ① select + 计算
          if (o.shouldNotify(newResult)) {        // ② 结果比较闸门
            o.notify()                            // ③ 才 setState
            notified++
          }
        }
        console.debug(`扇出: setData → ${this.observers.length} observer → ${notified} 通知`)
      })
    }
  }
}

// 探针：诊断扇出
let setDataCount = 0, notifyCount = 0
queryClient.getQueryCache().subscribe((e) => {
  if (e.type === 'updated') setDataCount++
})
// observer.onQueryUpdate 里计数 notify
// 比值 = notify / setData：理想 ≈ 活跃组件数，异常放大 → 查重复订阅

// 扇出优化对照
useQuery({ queryKey: ['todos'], queryFn })                              // 整 data 订阅：每次全通知
useQuery({ queryKey: ['todos'], queryFn, select: (d) => d.length })     // 标量：值没变不通知
```
