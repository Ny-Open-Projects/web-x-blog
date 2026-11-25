---
title: [ZSM-517] Jotai 的 atomFamily 是怎么管理参数化 atom 的缓存的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-517：Jotai 的 atomFamily 是怎么管理参数化 atom 的缓存的

**答**：
- `atomFamily(paramCreator, atomCreator)` 本质是 `Map<param, Atom>` 工厂：同一参数返回同一 atom 实例，不同参数各自独立状态——列表场景「每行一个 atom」的标准方案。
- 缓存策略可配：`atomFamily(createAtom, areEqual)` 第二个参数是相等性函数（默认 `Object.is`），用结构化比较（如 id 相等）可避免对象参数导致的重复创建。
- 生命周期问题：Map 只增不减，长列表/路由切换会泄漏。jotai 提供 `atomFamily` 的 `remove(param)`（新版还有 `setShouldRemove(fn)` 按时间/引用清理），组件卸载时配合 `useEffect` 清理对应 atom。
- 与「atom 里存 Map」对比：atomFamily 的粒度是 atom 级，订阅、Suspense、依赖图都按 atom 隔离；存 Map 的话整个列表共享一个 atom，一行更新全员重算。
- 追问钩子：参数对象每次渲染都是新引用会击穿缓存，正确姿势是传原始 id 而非对象；或在 family 内做 LRU。

```javascript
import { atom, useAtomValue, useSetAtom } from 'jotai'
import { atomFamily } from 'jotai/utils'

// 每个商品一行独立 atom（价格/选中态互不干扰）
const itemFamily = atomFamily(
  (id) => atom({ id, qty: 0, selected: false }),
  (a, b) => a === b        // 结构化相等：id 相等即复用
)

function CartRow({ id }) {
  const item = useAtomValue(itemFamily(id))
  const setItem = useSetAtom(itemFamily(id))
  useEffect(() => () => {
    // 卸载清理：防 Map 无限增长
    itemFamily.remove(id)
  }, [id])
  return (
    <button onClick={() => setItem((it) => ({ ...it, qty: it.qty + 1 }))}>
      {item.id} × {item.qty}
    </button>
  )
}

// 反例对比：整列表一个 atom
// const listAtom = atom(new Map())  // 任一行更新 → 订阅整表的组件全部重算
```
