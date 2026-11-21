---
title: [V3-398] 笔试：手写弹窗队列与 z-index 管理器
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-398：笔试：手写弹窗队列与 z-index 管理器
**题**：实现全局弹窗管理器：`open(options)` 返回 Promise（resolve 用户点击结果）；维护栈保证后开的弹窗 z-index 更高；同一 key 的弹窗去重（已存在则返回现有 promise）；关闭时自动出栈并恢复底层弹窗可交互。

```javascript
const stack = []
let baseZ = 2000
const uniqueMap = new Map()
function open(options) {
  const { key, component, props } = options
  if (key && uniqueMap.has(key)) return uniqueMap.get(key) // 去重
  const promise = new Promise(resolve => {
    const item = { id: Symbol(), resolve, zIndex: ++baseZ, ...options }
    stack.push(item)
    const close = (result) => {
      const i = stack.indexOf(item)
      if (i > -1) stack.splice(i, 1)
      uniqueMap.delete(key)
      resolve(result) // 底层弹窗自动重新可交互（顶层 zIndex 由栈顶决定）
    }
    item.close = close
    mountDialog(item) // 挂载弹窗组件，传入 zIndex 与 close
  })
  if (key) uniqueMap.set(key, promise)
  return promise
}
function closeTop(result) { stack.at(-1)?.close(result) }
```
**评分点**：
- Promise 化 open/close 闭环。
- 栈结构 + 递增 zIndex（或栈顶动态计算）。
- key 去重返回同一 promise。
- 关闭时 resolve 结果并出栈，不泄漏。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-28c596e9-fd96-482c-8c9c-f9c7884725a9-cwd'; fi
exit "$__zcode_status"
