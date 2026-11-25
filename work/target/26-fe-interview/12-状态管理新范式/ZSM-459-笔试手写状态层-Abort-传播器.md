---
title: [ZSM-459] 笔试：手写 Abort 传播器（级联取消 + 清理回调）
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-459：手写 Abort 传播器
**答**：实现 `createAbortScope(parent?)`：1) `scope.run(fn)`：fn 收到 scope 的 signal；2) 父 scope abort 时所有子 scope 级联 abort（监听父 signal）；3) `scope.onAbort(fn)` 注册清理回调（abort 时逆序执行，LIFO）；4) `dispose()`：abort + 清空回调 + 从父级解绑（防泄漏）；5) abort 后 run 直接 reject（AbortError）不再执行 fn；6) signal.reason 传播（子 scope 的 abort 原因继承父级）。

```javascript
export class AbortScope {
  constructor(parent) {
    this.ac = new AbortController()
    this.callbacks = []
    this.children = new Set()
    if (parent) {
      this.parent = parent
      parent.children.add(this)
      this._parentUn = parent.ac.signal.addEventListener('abort', () => {
        if (!this.ac.signal.aborted) this.ac.abort(parent.ac.signal.reason)   // 级联 + reason 继承
      })
    }
  }

  get signal() { return this.ac.signal }

  run(fn) {
    if (this.ac.signal.aborted) return Promise.reject(new DOMException('aborted', 'AbortError'))
    return new Promise((resolve, reject) => {
      const onAbort = () => reject(new DOMException('aborted', 'AbortError'))
      this.ac.signal.addEventListener('abort', onAbort, { once: true })
      Promise.resolve(fn(this.ac.signal)).then(resolve, reject)
        .finally(() => this.ac.signal.removeEventListener('abort', onAbort))
    })
  }

  onAbort(fn) {
    if (this.ac.signal.aborted) { fn(); return () => {} }       // 已 abort 立即执行
    this.callbacks.push(fn)
    return () => { const i = this.callbacks.indexOf(fn); if (i >= 0) this.callbacks.splice(i, 1) }
  }

  abort(reason) {
    if (this.ac.signal.aborted) return
    this.ac.abort(reason)
    const fns = [...this.callbacks].reverse()                   // LIFO
    this.callbacks.length = 0
    fns.forEach((fn) => { try { fn(reason) } catch (e) { report('abort_cb_error', e) } })
  }

  dispose() {
    this.abort('disposed')
    this._parentUn?.()                                          // 父级解绑
    this.parent?.children.delete(this)
  }
}
```
**评分点**：
- 级联取消（监听父 signal 转发 abort）+ reason 继承
- onAbort LIFO 逆序执行（资源依赖顺序正确）+ 已 abort 时立即执行语义
- dispose 三件事：abort + 父级解绑 + 回调清空（防泄漏完整）
- abort 后 run 快速 reject（不再发起新工作）
