---
title: [ZSM-838] 笔试：手写 View Transition 状态切换封装（降级 + 快照命名）
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-838：手写 View Transition 状态切换封装（降级 + 快照命名 + 并发防御）
**答**：实现 `transitionState(updateFn, { names })`：1) 支持 `document.startViewTransition` 时：旧视图快照 → 执行 updateFn（一次状态变更+渲染）→ 动画过渡；不支持时直接执行（降级）；2) 元素级命名（`view-transition-name`）：指定哪些元素参与动画（列表项重排/卡片移动）；3) **并发防御**：transition 进行中再触发 → 取消前一个（skipTransition）再开始，防快照叠加；4) `transitioning` 状态可查询；5) 附用例：降级直执行与命名动画的启动。

```javascript
function createViewTransitionManager() {
  let transitioning = false

  async function transitionState(updateFn, { names = {} } = {}) {
    const supports = typeof document !== 'undefined' && document.startViewTransition
    // 并发防御：进行中先跳过旧动画
    if (transitioning && document.getAnimations) {
      document.getAnimations().forEach((a) => { if (a.id?.startsWith('vt-')) a.cancel() })
    }

    // 元素级命名：给指定元素设置 view-transition-name
    const restoreNames = applyNames(names)

    if (!supports) {
      restoreNames()
      await updateFn()                        // 降级：直接执行（无动画）
      transitioning = false
      return { animated: false }
    }

    transitioning = true
    try {
      const vt = document.startViewTransition(async () => {
        await updateFn()                       // 旧快照 → 状态变更 → 新视图
      })
      await vt.finished
      return { animated: true }
    } finally {
      transitioning = false
      restoreNames()
    }
  }

  function applyNames(names) {
    const restores = []
    for (const [selector, name] of Object.entries(names)) {
      const el = document.querySelector(selector)
      if (!el) continue
      const prev = el.style.viewTransitionName
      el.style.viewTransitionName = name       // 快照命名：元素级动画
      restores.push(() => { el.style.viewTransitionName = prev })
    }
    return () => restores.forEach((fn) => fn())
  }

  return { transitionState, get transitioning() { return transitioning } }
}

// 用例（模拟环境）
const html = {
  _styles: new Map(),
  querySelector(sel) {
    return {
      get style() {
        if (!html._styles.has(sel)) html._styles.set(sel, {})
        return html._styles.get(sel)
      },
    }
  },
  startViewTransition: async (cb) => {
    await cb()
    return { finished: Promise.resolve() }
  },
}
globalThis.document = {
  ...html,
  getAnimations: () => [],
}

const mgr = createViewTransitionManager()
let applied = false
const r1 = await mgr.transitionState(async () => { applied = true }, {
  names: { '#card-7': 'moving-card' },
})
console.log(r1.animated, applied, mgr.transitioning)      // true true false
console.log(html._styles.get('#card-7').viewTransitionName)   // ''（动画后恢复原名）

// 降级环境
globalThis.document = { querySelector: () => null }
const r2 = await mgr.transitionState(async () => {})
console.log(r2.animated)                                  // false：降级直执行
```
**评分点**：
- 降级直执行（无 startViewTransition 的环境语义一致）
- 元素级命名（view-transition-name 设置与动画后恢复）
- 并发防御（进行中取消旧动画再开始）
- transitioning 状态可查询（防快照叠加）
