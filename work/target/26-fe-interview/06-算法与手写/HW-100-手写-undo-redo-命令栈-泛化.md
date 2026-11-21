---
title: [HW-100] 手写可泛化的 undo/redo 命令栈——命令对象接口、合并连续操作、容量上限
date: 2026-11-19
categories: [手写代码]
tags: [前端面试, 笔试题, 24]
type: 笔试题
---

**答**：命令模式 undo/redo：每个操作封装 {execute, undo}；连续同类操作（如连续打字）合并为一个命令（coalesce 窗口内）；栈容量上限丢最旧；redo 指针语义（新命令入栈清空 redo 分支）。与 ALG-199（画板场景）的差异是通用接口化。

```javascript
class CommandStack {
  constructor({ max = 100, coalesceMs = 500 } = {}) {
    Object.assign(this, { max, coalesceMs, done: [], undone: [] });
  }
  execute(cmd) {
    cmd.execute();
    const last = this.done.at(-1);
    // 合并：同类型命令且间隔 < coalesceMs（连续打字合成一条，undo 一次退整段）
    if (last && cmd.mergeWith && cmd.mergeWith(last)) {
      this.done[this.done.length - 1] = cmd;   // 合并替换
    } else {
      this.done.push(cmd);
      this.undone = [];                        // 新命令清空 redo 分支
      if (this.done.length > this.max) this.done.shift();
    }
  }
  undo() {
    const cmd = this.done.pop();
    if (!cmd) return false;
    cmd.undo();
    this.undone.push(cmd);
    return true;
  }
  redo() {
    const cmd = this.undone.pop();
    if (!cmd) return false;
    cmd.execute();
    this.done.push(cmd);
    return true;
  }
}
// 用法：文本编辑器
const stack = new CommandStack({ coalesceMs: 800 });
let text = '';
function typeCmd(ch, at) {
  return {
    execute: () => { text = text.slice(0, at) + ch + text.slice(at); },
    undo: () => { text = text.replace(ch, ''); },
    mergeWith: (last) => last.type === 'type' && Date.now() - last.at < 800,
    type: 'type', at: Date.now(), ch,
  };
}
stack.execute(typeCmd('h', 0)); stack.execute(typeCmd('i', 1));
stack.undo();          // 一次撤销 "hi" 两步（已合并）
```

**评分点**：
- 命令接口（execute/undo）与双栈语义正确；redo 分支在新命令入栈时清空。
- 合并窗口（连续同类操作一条 undo），mergeWith 协议清晰。
- 容量上限丢最旧；undo/redo 返回值供 UI 禁用态。
- 能对比快照法（内存大）与命令法（实现复杂）的取舍。
