---
title: [ZSM-581] 笔试：手写主线程-Worker 状态镜像器（增量 patch 协议）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-581：手写主线程-Worker 状态镜像器（增量 patch 协议）
**答**：实现 `createMirror(workerUrl, initial)`：1) 主线程 `commit(op, args)`：发操作给 worker，worker 求值后**只回变更路径 patch**（`{ path, value }[]`），主线程 applyPatch 更新本地镜像；2) reqId 配对 + 过期结果丢弃；3) `pending` 计数暴露在途请求数；4) `onSync(fn)` 通知镜像更新；5) worker 侧提供 `snapshot(state)`：对比新旧状态生成扁平路径 patch（一层对象数组展开为 `a.b` 路径）。附用例验证 patch 生成与过期丢弃。

```javascript
// worker 侧工具：状态 diff → 扁平路径 patch
function snapshot(prev, next, path = '', out = []) {
  if (Object.is(prev, next)) return out
  if (isObj(prev) && isObj(next)) {
    const keys = new Set([...Object.keys(prev), ...Object.keys(next)])
    for (const k of keys) {
      if (!(k in next)) out.push({ path: path ? `${path}.${k}` : k, value: undefined })
      else snapshot(prev[k], next[k], path ? `${path}.${k}` : k, out)
    }
    return out
  }
  out.push({ path, value: next })   // 叶子差异整体替换
  return out
}
function isObj(v) { return v && typeof v === 'object' }

// worker 主逻辑
let state = null
let latestReqId = 0
self.onmessage = (e) => {
  const { type, op, args, reqId } = e.data
  if (type === 'init') { state = e.data.state; return }
  if (type !== 'commit') return
  latestReqId = reqId
  const next = compute(op, args, state)
  const patch = snapshot(state, next)
  state = next
  self.postMessage({ type: 'patch', reqId, patch })
}
function compute(op, args, state) {
  if (op === 'inc') return { ...state, count: state.count + (args.n ?? 1) }
  if (op === 'setUser') return { ...state, user: { ...state.user, name: args.name } }
  return state
}

// 主线程：镜像器
function createMirror(workerUrl, initial) {
  const w = new Worker(workerUrl)
  let state = { ...initial }
  const listeners = new Set()
  let pending = 0
  let latest = 0

  w.onmessage = (e) => {
    const { reqId, patch } = e.data
    pending--
    if (reqId !== latest) return        // 过期结果丢弃（新请求已发出）
    for (const { path, value } of patch) applyPath(state, path, value)
    listeners.forEach((fn) => fn(state))
  }

  function applyPath(obj, path, value) {
    const ks = path.split('.')
    let cur = obj
    ks.slice(0, -1).forEach((k) => (cur[k] = cur[k] ?? {}))
    cur[ks.at(-1)] = value
  }

  return {
    commit(op, args) {
      pending++
      latest = ++latest
      w.postMessage({ type: 'commit', op, args, reqId: latest })
    },
    getState: () => state,
    get pending() { return pending },
    onSync(fn) { listeners.add(fn); return () => listeners.delete(fn) },
  }
}

// 用例（主线程视角模拟）
const mirror = createMirror('worker.js', { count: 0, user: { name: 'a' } })
// worker 内 compute('inc', {n: 5}) 生成 patch:
// [{ path: 'count', value: 5 }]
const patch1 = snapshot({ count: 0, user: { name: 'a' } }, { count: 5, user: { name: 'a' } })
console.log(patch1)                       // [{ path: 'count', value: 5 }]
const patch2 = snapshot(patch1[0].value && { count: 5, user: { name: 'a' } }, { count: 5, user: { name: 'b' } })
console.log(patch2)                       // [{ path: 'user.name', value: 'b' }]：嵌套路径
```
**评分点**：
- 增量 patch 生成（叶子替换粒度，数组/嵌套路径正确）
- reqId 配对与过期结果丢弃（快速连击防旧覆盖新）
- 镜像 applyPatch 的中间节点补建（cur[k] ??= {}）
- pending 在途计数可观测
