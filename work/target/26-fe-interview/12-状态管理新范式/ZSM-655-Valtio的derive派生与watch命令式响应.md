---
title: [ZSM-655] Valtio 的 derive 与 watch：读式派生和命令式响应的两条路径
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-655：Valtio 的 derive 与 watch：读式派生和命令式响应的两条路径

**答**：
- Valtio 的派生有两条路径：**`derive(proxy, mapFn)`**——读式派生，mapFn 返回的对象也是 proxy，读取派生属性时才计算（惰性）+ 跟踪依赖（内部用 useSnapshot 相同的访问跟踪），组件订阅派生值与订阅原始值同一机制；**`watch(proxy, fn)`**——命令式响应，proxy 变化时 fn 运行（回调里可执行副作用），不产出数据。
- 分工原则：产出「渲染用的数据」用 derive；执行「副作用」（打日志、同步到 worker、调 API、改另一个 store）用 watch。watch 里改被观察的 proxy 自己要小心——加条件防自触发死循环。
- derive 的实现要点：mapFn 里只能通过 snapshot 访问（`snap(state)`），直接读 proxy 不会建立依赖跟踪；派生链（derive 依赖 derive）支持但要注意惰性求值的级联成本。
- watch 的语义：批量（一次事件循环内的多次修改合并为一次回调）；返回 unsubscribe；**在组件外使用是常驻的**，组件内使用建议在 useEffect 里并退订——与 Zustand subscribeWithSelector 语义对齐。
- 追问钩子：valtio 官方明确警告「watch 里写 proxy 引发的连锁更新」是头号坑——写其他 store、或对同一 store 的不相干字段写，都要做相等性短路。

```javascript
import { proxy, derive, watch } from 'valtio'

const state = proxy({ items: [{ price: 10, qty: 2 }], discount: 0.9, logs: [] })

// derive：读式派生（惰性 + 依赖跟踪）
const derived = derive({
  subtotal: (get) => get(state).items.reduce((a, i) => a + i.price * i.qty, 0),
  total: (get) => get(derived).subtotal * get(state).discount,   // 派生可依赖派生
})
// 组件里 useSnapshot(derived)——与订阅原始 proxy 机制一致

// watch：命令式副作用（同步到远端）
const unsub = watch((get) => {
  const snap = get(state)
  // 相等性短路：防自触发
  if (snap.logs.at(-1)?.subtotal === derived.subtotal) return
  syncToWorker({ type: 'recalc', subtotal: derived.subtotal })
})

// 坑示例：watch 里写被观察 store（无短路 → 死循环）
// BAD: watch((get) => { state.version++ })            // 改完又触发 watch
// GOOD: watch((get) => { if (needRecalc(get(state))) state.version++ })

// 组件内使用：必须退订
function Logger() {
  useEffect(() => {
    const stop = watch((get) => console.log('changed', get(state).items.length))
    return stop
  }, [])
  return null
}
```
