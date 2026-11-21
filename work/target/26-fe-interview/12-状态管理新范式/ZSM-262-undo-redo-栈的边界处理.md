---
title: [ZSM-262] 手写 undo/redo 栈要处理哪些边界
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-262：手写 undo/redo 栈要处理哪些边界

**答**:
- 新动作清空 redo 栈（分叉丢弃）；栈容量上限（如 50 步）FIFO 淘汰防止内存膨胀
- 合并窗口：连续输入同一表单字段只记一步（100ms~500ms 内同字段合并），否则打一个字就是一步撤销
- 异步操作不可撤销：网络请求结果落地要么标记「不可回退」，要么记录反向 patch（如删除则存回原文）
- 状态分域：全应用一个栈会撤销到无关模块，按编辑域（画布/表单/文档）独立栈

```javascript
function createHistory(limit = 50, mergeMs = 300) {
  let past = [], future = [], lastTime = 0, lastKey = ''
  return {
    push(state, key) {
      const now = Date.now()
      const merge = key === lastKey && now - lastTime < mergeMs   // 合并窗口
      if (!merge) { past = [...past.slice(-(limit - 1)), state]; future = [] }
      lastTime = now; lastKey = key
    },
    undo(current) { if (!past.length) return current; future.push(current); return past.pop() },
    redo(current) { if (!future.length) return current; past.push(current); return future.pop() },
  }
}
```
