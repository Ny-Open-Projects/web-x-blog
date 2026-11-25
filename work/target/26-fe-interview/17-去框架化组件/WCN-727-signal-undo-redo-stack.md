---
title: [WCN-727] 笔试：手写 signal 驱动的 undo/redo 事务栈
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-727：笔试：手写 signal 驱动的 undo/redo 事务栈

**答**：
- 需求：实现 `createHistory(initial)`，返回 `{ valueOf(), set(next), undo(), redo(), canUndo(), canRedo() }`。每次 set 记录 {prev,next} 到 past；undo 回退并把记录移到 future；redo 反向；连续相同值不记录；栈深度上限 50。
- 要点：用闭包维护 past/future 数组；set 时 prev===next 直接忽略；undo/redo 时维护两个栈；边界：栈空时 no-op。

```javascript
function createHistory(initial) {
  let value = initial, past = [], future = [];
  const LIMIT = 50;
  return {
    valueOf() { return value; },
    set(next) {
      if (Object.is(next, value)) return;           // 相同值不记录
      past.push({ prev: value, next });
      if (past.length > LIMIT) past.shift();        // 限制深度
      value = next; future = [];
    },
    undo() {
      if (!past.length) return;                     // 栈空 no-op
      const rec = past.pop();
      value = rec.prev; future.push(rec);
    },
    redo() {
      if (!future.length) return;
      const rec = future.pop();
      value = rec.next; past.push(rec);
    },
    canUndo() { return past.length > 0; },
    canRedo() { return future.length > 0; },
  };
}
const h = createHistory('A');
h.set('B'); h.set('C'); h.undo();
console.log(h.valueOf(), h.canRedo());   // B true
```

**评分点**：
- undo/redo 正确维护 past/future 双栈。
- 相同值（Object.is）不记录，避免历史噪声。
- 栈深度上限防止内存膨胀。
- 栈空操作 no-op，具备边界防御。
