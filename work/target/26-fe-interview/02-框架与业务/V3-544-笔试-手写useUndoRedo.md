---
title: [V3-544] 笔试：手写 useUndoRedo（快照栈 + 合并策略）
date: 2026-11-21
categories: [Vue3]
tags: [前端面试, 笔试题, 架构]
type: 笔试题
---

## V3-544：笔试：手写 useUndoRedo

**答**：实现 `useUndoRedo(sourceRef, { capacity = 50, mergeMs = 500 })`：① undo/redo 栈（快照 + 指针）；② 连续变更合并：mergeMs 内的变更视为一次（输入场景不产生海量快照）；③ undo/redo 返回 bool（栈耗尽返回 false）；④ canUndo/canRedo 响应式；⑤ capacity 上限丢最旧。写出实现。

```javascript
export function useUndoRedo(source, { capacity = 50, mergeMs = 500 } = {}) {
  const undoStack = [], redoStack = [];
  const pointer = ref(-1);
  let lastPushAt = 0;

  function snapshot() {
    const now = Date.now();
    const current = JSON.parse(JSON.stringify(toValue(source)));   // 深快照
    if (now - lastPushAt < mergeMs && undoStack.length) {
      undoStack[undoStack.length - 1] = current;      // 合并: 替换栈顶
    } else {
      undoStack.push(current);
      if (undoStack.length > capacity) undoStack.shift();
      pointer.value = undoStack.length - 1;
    }
    lastPushAt = now;
    redoStack.length = 0;                              // 新快照清空 redo
  }
  const canUndo = computed(() => pointer.value > 0);
  const canRedo = computed(() => pointer.value < undoStack.length - 1);

  function undo() {
    if (!canUndo.value) return false;
    // 把当前态存入 redo
    redoStack.push(JSON.parse(JSON.stringify(toValue(source))));
    pointer.value--;
    source.value = JSON.parse(JSON.stringify(undoStack[pointer.value]));
    return true;
  }
  function redo() {
    if (!canRedo.value) return false;
    undoStack.push(JSON.parse(JSON.stringify(toValue(source))));
    pointer.value++;
    source.value = JSON.parse(JSON.stringify(redoStack.pop()));
    return true;
  }
  // 自动快照: 变更即记录(深 watch 或显式调用)
  watch(source, snapshot, { deep: true });
  return { undo, redo, canUndo, canRedo, snapshot };
}
```

**评分点**：
- 双栈 + 指针模型（undo 时当前态进 redo）
- mergeMs 合并策略（输入场景防快照爆炸）
- 深快照序列化隔离（防引用共享导致的栈污染）
- capacity 上限与 canUndo/canRedo 边界
