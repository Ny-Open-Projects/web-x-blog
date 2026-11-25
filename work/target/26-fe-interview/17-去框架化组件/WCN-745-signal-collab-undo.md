---
title: [WCN-745] 基于 Signals 实现协同编辑的本地乐观更新与撤销栈怎么配合？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-745：基于 Signals 实现协同编辑的本地乐观更新与撤销栈怎么配合？

**答**：
- 结论：本地操作先立即写入本地 signal（乐观更新）并入 undo 栈，再发送给服务端；收到远端确认后校正版本号；收到远端操作则用 CRDT/OT 合并到本地。
- 撤销只撤销「本地已确认操作」，且要广播给其他端；用「操作 ID + 版本」去重，避免自己收到自己的回声重复应用。
- 追问钩子：本地撤销与远端同时操作冲突了怎么办？考察 CRDT 的交换律/幂等与冲突消解策略。

```javascript
const local = signal({ text: '' });
const undoStack = [];
function applyLocal(op) {
  undoStack.push(op);                       // 入撤销栈
  local.value = applyOp(local.value, op);   // 乐观更新
  broadcast({ ...op, origin: 'local' });
}
function applyRemote(op) {
  if (op.origin === 'local') return;         // 忽略自己的回声
  local.value = applyOp(local.value, op);    // 合并远端
}
function undo() {
  const op = undoStack.pop();
  if (!op) return;
  local.value = applyOp(local.value, invert(op));
  broadcast({ ...invert(op), origin: 'local' });
}
function applyOp(s, op) { return { text: s.text + (op.insert || '') }; }
function invert(op) { return { insert: '', delete: op.insert }; }
console.log(typeof applyLocal, typeof applyRemote, typeof undo);
```
