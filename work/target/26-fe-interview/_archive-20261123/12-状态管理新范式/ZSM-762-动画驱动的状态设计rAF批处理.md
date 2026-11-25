---
title: [ZSM-762] 动画驱动的状态设计：rAF 批处理与帧预算内的状态更新
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-762：动画驱动的状态设计：rAF 批处理与帧预算内的状态更新

**答**：
- 动画状态（进度/插值值）的正确架构：**原始信号不进 store，rAF 循环里计算插值 → 直接写 DOM（transient）**；只有「里程碑」（动画开始/结束/阶段切换）才进 store 触发 React 渲染。每帧预算 16ms（8ms 余量），状态更新的序列化+diff 开销在动画路径上全部免除。
- rAF 批处理：多个动画源（滚动+手势+动画库）都写 DOM 时统一进一个 rAF 循环——「每帧一次 layout 写入」，避免 layout thrashing（读-写交错强制回流）。模式：`collect reads → compute → write`（先批量读后批量写）。
- React 侧的受控消费：动画结束后 store 更新最终值（如 `position: {x: 300, y: 200}`），刷新时恢复语义一致；动画中途刷新页面丢中间帧是可接受的（动画态本来就不该持久化）。
- 派生动画状态（如进度条百分比）用 CSS 变量传递：`el.style.setProperty('--progress', p)`——CSS calc/transition 在合成器线程消费，不进 React。
- 追问钩子：FLIP 技术的状态含义——「先记录旧位置（读）→ 状态变更（React 渲染新布局）→ transform 回旧位置 → rAF 下一帧过渡到新位置」——React 状态驱动布局 + 手写 transform 补间，是「状态库与动画协作」的标准解。

```javascript
// rAF 批处理动画循环（读写分离）
class AnimationLoop {
  #pendingWrites = []
  #reads = []

  read(el, prop) { this.#reads.push({ el, prop }) }       // 声明读
  write(el, apply) { this.#pendingWrites.push({ el, apply }) }   // 声明写

  start() {
    const tick = () => {
      // 1) 批量读（一次 layout）
      const values = this.#reads.map(({ el, prop }) => el.getBoundingClientRect()[prop])
      // 2) 批量写（一次 layout）
      this.#pendingWrites.forEach(({ el, apply }, i) => apply(el, values[i]))
      this.#reads = []
      this.#pendingWrites = []
      requestAnimationFrame(tick)
    }
    requestAnimationFrame(tick)
  }
}

// 手势动画：信号不进 store
const loop = new AnimationLoop()
function onDrag(e) {
  // 高频：直接写 transform（合成器线程，不触发 React）
  loop.write(boxRef.current, (el) => {
    el.style.transform = `translate3d(${e.clientX}px, ${e.clientY}px, 0)`
    el.style.setProperty('--progress', e.clientX / window.innerWidth)   // CSS 变量：合成器消费
  })
}
// 里程碑：进 store
function onDragEnd(e) {
  useDrag.getState().settle({ x: e.clientX, y: e.clientY })   // 最终值进 store（一次渲染）
}

// FLIP：React 状态驱动布局 + 手写补间
function flip(oldRect, el) {
  const newRect = el.getBoundingClientRect()
  const dx = oldRect.left - newRect.left
  const dy = oldRect.top - newRect.top
  el.style.transform = `translate(${dx}px, ${dy}px)`
  requestAnimationFrame(() => {
    el.style.transition = 'transform 200ms'
    el.style.transform = ''                       // 过渡到新位置
  })
}
```
