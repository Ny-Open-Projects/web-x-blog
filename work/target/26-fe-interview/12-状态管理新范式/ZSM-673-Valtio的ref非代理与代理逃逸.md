---
title: [ZSM-673] Valtio 的 ref 与代理逃逸：哪些对象不该被 proxy 化
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-673：Valtio 的 ref 与代理逃逸：哪些对象不该被 proxy 化

**答**：
- `ref(obj)` 把对象标记为「不代理」：ref 内的对象按引用直接存取，不做跟踪/快照。该用的场景：1) **DOM 元素/Canvas 上下文**这类不可克隆、不可代理的对象；2) 三个库/三方实例（地图 SDK、编辑器实例）——proxy 化会破坏其内部 this 绑定；3) 大型二进制/频繁可变的高频数据（shader uniforms）——跟踪成本大于收益。
- 「代理逃逸」bug：把 proxy 状态对象直接塞给**期望普通对象的 API**（第三方库、JSON.stringify 意外触发 get 拦截、structuredClone 递归触发代理）——库内部存了 proxy 引用，后续状态变更库拿着的是「活的」proxy（行为诡异）或快照（数据陈旧），取决于 API 何时读。解法：跨界传 `snapshot(state)` 或原始 plain object。
- 判定清单（放不进 proxy 的对象）：class 实例带私有字段（#field Proxy 可见性问题）、WeakMap 不可枚举依赖、循环引用、不可克隆（Blob/File）、原型链方法依赖 this 的（Date/RegExp 的方法）。
- 追问钩子：ref 之外的通用守则——「状态库里只放数据形状的 plain object + 明确 ref 的实例」，任何 class 实例状态库存 id、实例存 ref/context，避免代理层与类逻辑冲突。

```javascript
import { proxy, ref, useSnapshot, snapshot } from 'valtio'

const state = proxy({
  name: 'demo',
  canvas: ref(document.createElement('canvas')),   // 不代理：2D 上下文安全
  editor: ref(editorInstance),                     // 三方实例按引用
  items: [{ id: 1 }],                              // 数据形状正常代理
})

state.canvas.getContext('2d')     // 直接访问，无拦截开销

// 代理逃逸的三个典型场景
// 1) structuredClone(proxy) —— 触发递归 get，可能爆炸或拷出快照
//    ✓ const clone = structuredClone(snapshot(state))
// 2) 第三方 API 存 proxy 引用
//    chart.update(proxyState)        // ✗ 库持有活的 proxy
//    chart.update(snapshot(proxyState))   // ✓ 传冻结快照
// 3) JSON.stringify 循环引用报错
//    ✓ JSON.stringify(snapshot(state))

// 判定清单
function shouldRef(obj) {
  if (obj instanceof HTMLElement || obj instanceof CanvasRenderingContext2D) return true
  if (obj instanceof Date || obj instanceof RegExp) return true      // 方法依赖内部槽位
  if (obj.constructor?.name.startsWith('THREE')) return true         // 3D 实例
  return false
}
```
