---
title: [V3-435] 笔试：手写迷你 EffectScope（嵌套 + detached）
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 笔试题, 06]
type: 笔试题
---

## V3-435：笔试：手写迷你 EffectScope（嵌套 + detached）
**题**：实现 `effectScope(detached)`：run(fn) 内创建的子 scope/effect 自动挂到当前 scope；stop() 递归停止所有子级（detached 的子 scope 不受影响）；嵌套 run 时内层正确挂靠；重复 stop 幂等。

```javascript
let activeScope = null
function effectScope(detached = false) {
  const scope = { children: [], disposables: [], active: true, detached }
  scope.run = (fn) => {
    const prev = activeScope
    if (prev && !detached) prev.children.push(scope)
    activeScope = scope
    try { return fn(scope) } finally { activeScope = prev }
  }
  scope.stop = () => {
    if (!scope.active) return // 幂等
    scope.active = false
    scope.disposables.forEach(d => d())   // 停 effect/watch
    scope.children.forEach(c => { if (!c.detached) c.stop() })
    scope.children = []
  }
  // register 供 watch/effect 内部调用
  scope._register = (dispose) => scope.disposables.push(dispose)
  return scope
}
// watch 内部：activeScope?._register(() => unwatch())
```
**评分点**：
- activeScope 栈式切换（run 内保存/恢复 prev）。
- 递归 stop + detached 豁免。
- stop 幂等（active 标志）。
- _register 收集清理函数（模拟 effect/watch 的注册入口）。
__zcode_status=$?
if [ "$__zcode_status" -eq 0 ]; then pwd -P > '/var/folders/0s/4tf1lwpd7817z10jldln1r4c0000h8/T/zcode-a8aaaf99-5e0a-4ac4-9328-9eca0f3226fb-cwd'; fi
exit "$__zcode_status"
