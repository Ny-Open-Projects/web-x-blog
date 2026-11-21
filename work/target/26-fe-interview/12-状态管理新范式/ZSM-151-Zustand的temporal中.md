---
title: [ZSM-151] Zustand 怎么做撤销/重做（undo/redo）？temporal 中间件的核心数据结构是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-151：Zustand 怎么做撤销/重做（undo/redo）？temporal 中间件的核心数据结构是什么？
**答**：
- 用 zundo 的 temporal 中间件：包住 create 后自动把每次 set 前的状态压入 pastStates 栈，undo 弹栈写回、redo 从 futureStates 取回——核心就是双栈 + 指针。
- 性能关键：`partialize` 只跟踪需要撤销的切片（画布节点而非整个 store），`limit` 限制栈深防内存爆炸；高频操作（拖拽）要先 `temporal.pause()` 结束再 resume，避免一帧一条记录。
- 语义细节：undo 应该恢复的是「快照」而非补丁，所以状态对象要不可变更新；异步 action 里 setState 多次会产生多条历史，需在入口 pause。
- 适用边界：画布/文档编辑器这类「用户显式操作流」值得 undo；表单类用受控草稿更自然，别滥用。

```javascript
import { temporal } from 'zundo'

const useCanvasStore = create(temporal(
  (set) => ({
    nodes: [],
    addNode: (n) => set((s) => ({ nodes: [...s.nodes, n] })),   // 不可变更新
  }),
  {
    limit: 50,                                    // 栈深上限
    partialize: (s) => ({ nodes: s.nodes }),      // 只跟踪画布数据
    handleSet: (handleSet) =>
      throttle(handleSet, 300)                    // 高频 set 合并历史
  }
))

function Toolbar() {
  const { undo, redo, clear } = useCanvasStore.temporal.getState()
  const nodes = useCanvasStore(s => s.nodes)
  return <>
    <NodeCanvas nodes={nodes}/>
    <button onClick={() => undo()}>撤销</button>
    <button onClick={() => redo()}>重做</button>
  </>
}
```
