---
title: [FRP-152] 并发模式下受控输入为什么不会"回跳"？revert 机制是怎么回事？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-152：并发模式下受控输入为什么不会"回跳"？revert 机制是怎么回事？

**答**：
- 风险场景：输入触发低优更新（如过渡中的搜索列表渲染），低优 render 慢——如果浏览器把"旧 state 对应的 value"写回 input，用户会看到自己刚打的字消失。
- React 的保障一：**连续离散事件**（keydown/输入类）触发的更新被强制为 sync lane，同步 render + commit，输入即时上屏。
- 保障二是 **revert 机制**：commit 前检查 DOM input 的当前值与 fiber 里 state 是否一致；不一致说明存在"被打断的渲染留下的 DOM 状态"，React 把 DOM 值**恢复**成用户视角的最新值，并对该 input 用 sync lane 立即重渲。
- 源码入口：`restoreStateIfNeeded / restoreImpl`——遍历记录的"需要恢复的 DOM 引用"，逐个 revert 后清空队列。

```javascript
// 简化实现，帮助理解受控输入的 revert 机制
// React 内部记录"可能需要恢复"的 DOM
let needsStateRestore = false;
const restoreTargets = [];

function markRestoreTarget(inputEl, expectedValue) {
  restoreTargets.push({ el: inputEl, value: expectedValue });
  needsStateRestore = true;
}

function restoreStateIfNeeded() {
  if (!needsStateRestore) return;
  needsStateRestore = false;
  for (const { el, value } of restoreTargets) {
    if (el.value !== value) {
      // DOM 值与最新 state 不一致：把 DOM 拨回用户真正输入的值
      el.value = value;                       // revert！
      // 并对该输入的 state 用 sync lane 强制重渲，让 fiber 与 DOM 重新一致
      syncRenderFromDOMValue(el, value);
    }
  }
  restoreTargets.length = 0;
}

// 挂接点：每次 commit 完成后 / 被打断的渲染恢复前调用
function commitRoot() {
  // ... 提交 DOM 变更 ...
  restoreStateIfNeeded();                     // 关键调用
}

// —— 场景演示 ——
// <input value={query} onChange={e => { setQuery(v); startTransition(() => setResults(v)) }} />
// 1. 用户输入 'abc'：setQuery 同步上屏（离散事件 sync lane），input.value = 'abc'
// 2. 过渡渲染 results 很慢，期间用户继续输入 'abcd'：
//    又一次 sync render，fiber.query = 'abcd'
// 3. 过渡 render 被打断/恢复时：检查 input DOM 值 —— 'abcd'
//    若某个中间状态曾把 'abc' 写回 DOM -> revert 成 'abcd'
// 用户视角：无论并发多忙，输入框永远显示自己刚打的内容，永不回跳
```

## 追问（补充）

**追问**：

1. 把 onChange 里的 setQuery 也放进 startTransition 会怎样？ → 输入更新被降为过渡优先级，不再 sync 上屏，受控值会滞后于按键，体感就是"打字卡顿"。正确做法是只把派生列表的更新放进 transition，输入本身保持 sync lane。
2. React 19 里 revert 的实现有变化吗？ → 有调整。19 在 commit 前发现 DOM value 与最新 state 不一致时直接安排一次同步重渲来对齐，精简了 18 里那套 restore 队列的部分分支，但"输入永不回跳"的结论不变。
3. 非受控输入有回跳问题吗？ → 没有。非受控时 DOM 是唯一真相源，React 不往 value 里写值，也就不存在把旧 state 写回去的可能；代价是无法在渲染期格式化或拦截输入。
