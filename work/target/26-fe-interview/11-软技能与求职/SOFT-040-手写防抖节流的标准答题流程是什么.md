---
title: [SOFT-040] 手写防抖节流的标准答题流程是什么？
date: 2026-11-17
categories: [软技能]
tags: [前端面试, 笔试题, 22]
type: 笔试题
---

## SOFT-040：手写防抖节流的标准答题流程是什么？

**答**：
- 这是前端最高频手写题，标准流程：先辨析概念差异 → 确认需求场景 → 手写实现 → 补进阶点 → 自测。
- 概念辨析一句话讲透：防抖是"停止触发 n 毫秒后才执行"（最后一次说了算），节流是"n 毫秒内最多执行一次"（第一次说了算）。
- 先写基础版拿稳分，再主动补进阶点（立即执行、取消、返回值）——由浅入深展示完整度。
- 写完口头跑场景：搜索框用防抖、滚动加载用节流，场景对应是理解证明。

```text
防抖节流答题流程

1. 辨析："防抖 debounce：事件停止触发 n ms 后执行，适合搜索框
   输入联想；节流 throttle：n ms 内最多执行一次，适合
   scroll/resize 这类高频事件。"
2. 确认："需要我实现哪个？需要支持立即执行首次触发吗？"

3. 基础版防抖：
   function debounce(fn, delay) {
     let timer = null
     return function (...args) {
       clearTimeout(timer)
       timer = setTimeout(() => fn.apply(this, args), delay)
     }
   }

4. 进阶点（主动补）：
   - 立即执行版：首次触发立刻执行，后续静默期内的触发重置定时器
   - 取消能力：返回对象上挂 cancel 方法，clearTimeout 并置空
   - 组件卸载清理：Vue 的 onUnmounted / React 的 useEffect cleanup
5. 自测："模拟连续输入：每 100ms 触发一次、共 5 次、delay 500ms——
   前面 4 次都被 clearTimeout 重置，停止输入 500ms 后执行 1 次。"

【追问预案】
"防抖和节流结合？"→ 答过渡思路：延迟窗口内收集、窗口边界执行。
```
