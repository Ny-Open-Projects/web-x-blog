---
title: [ZSM-656] Valtio 对 Map/Set 的 proxy 处理：为什么需要原生方法重写
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-656：Valtio 对 Map/Set 的 proxy 处理：为什么需要原生方法重写

**答**：
- 普通 Proxy 拦不住 Map/Set：`map.set(k, v)` / `set.add(v)` 调用的是**原型链上的方法**，方法内部通过内部槽位（[[MapData]]）操作数据，不走 get/set 拦截器——代理形同虚设，修改不会触发版本 bump 和通知。
- Valtio 的解法：在 proxy 的 get 拦截器里对 Map/Set 特判，**返回重新绑定 this 的包装方法**——`map.set` 被替换为「先记录修改 → 调用原生方法 → bump 版本 → 通知」的合成函数；`get/has/forEach/keys` 等读方法同样包装以注册依赖。
- 使用注意：1) proxy(map) 后 `size` 是 getter 要特殊处理（get 拦截返回绑定值）；2) **嵌套的 Map 内值**再取出来仍是 proxy（get 时递归代理）；3) 序列化（JSON）Map 会变成 `{}`——持久化前要转换。
- 替代方案对比：Valtio 支持 Map/Set、immer 需要 `enableMapSet()`、zustand 里直接用普通对象 + Set 建模（ZSM-526）更简单——Map 状态的选型上「真的需要 Map 语义（O(1) has/delete）」才用 proxy 库，否则对象字典更省心。
- 追问钩子：Proxy + Map 的兼容问题是「Proxy 库」性能与实现复杂度的缩影——这也是 valtio 源码里 proxyHandler 比想象中长的原因。

```javascript
import { proxy, useSnapshot } from 'valtio'

const state = proxy({
  userMap: new Map([['u1', { name: 'a' }]]),
  selected: new Set(['u1']),
})

// set：Valtio 包装后触发通知
state.userMap.set('u2', { name: 'b' })       // 内部：原生 set + version bump + notify
state.selected.add('u2')
state.userMap.delete('u1')                    // O(1) 删除同样生效

// 读：快照语义
function UserList() {
  const snap = useSnapshot(state)             // Map 在快照里可读
  return [...snap.userMap.entries()].map(([id, u]) => <div key={id}>{u.name}</div>)
}

// 陷阱：JSON 序列化 Map 失败
console.log(JSON.stringify({ m: state.userMap }))   // {"m":{}} —— Map 丢失
// 持久化要转换
const serializable = { userMap: Object.fromEntries(state.userMap) }

// 手写示意：proxy get 拦截里包装 Map 方法（简化）
function proxyMap(target) {
  return new Proxy(target, {
    get(t, k) {
      if (k === 'set') return (key, val) => { t.set(key, val); bump(); notify() }
      if (k === 'delete') return (key) => { const r = t.delete(key); bump(); notify(); return r }
      if (k === 'get') return (key) => t.get(key)
      if (k === 'size') return t.size
      const v = Reflect.get(t, k)
      return typeof v === 'function' ? v.bind(t) : v
    },
  })
}
```
