---
title: [R19-161] 手写一个 jotai mini：原子状态与派生原子如何实现？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-161：手写一个 jotai mini：原子状态与派生原子如何实现？
**答**：
- atom 就是"带 key 的状态单元"：`{ init, read, write }`；primitive atom 的 read 是 `get => get(self)`，derived atom 的 read 可以依赖其他 atom。
- 派生实现：read 函数里 `get(otherAtom)` 时登记依赖，被依赖 atom 更新时通知依赖它的 atom 一起失效。
- 写入：write(get, set, update)，`set` 既可写 primitive 也可触发 derived 的重算。
- 与 zustand 的差异一句话：atom 是**图**（任意组合派生），store 是**树**（整体 state 切片）。

```javascript
// jotai-mini.js —— 手写原子状态 + 派生
import { useSyncExternalStore } from 'react';

const atomRegistry = new Map();     // atom -> { value, listeners, deps }

function getNode(atom) {
  if (!atomRegistry.has(atom)) {
    atomRegistry.set(atom, {
      value: undefined,
      initialized: false,
      listeners: new Set(),
      dependents: new Set(),        // 依赖本 atom 的其他 atom（用于级联失效）
    });
  }
  return atomRegistry.get(atom);
}

export function atom(read, write) {
  if (typeof read === 'function') {
    return { read, write };                        // derived atom
  }
  const a = {
    init: read,
    read: get => get(a),                           // primitive：读自己
    write: (get, set, update) =>
      set(a, typeof update === 'function' ? update(get(a)) : update),
  };
  return a;
}

function readAtom(atom) {
  const node = getNode(atom);
  const get = (dep) => {
    if (dep === atom) {                            // 读自己：返回缓存
      if (!node.initialized) {
        node.value = atom.init;
        node.initialized = true;
      }
      return node.value;
    }
    getNode(dep).dependents.add(atom);             // 读别人：登记依赖关系
    return readAtom(dep);
  };
  return atom.read(get);
}

export function useAtomValue(atom) {
  const node = getNode(atom);
  return useSyncExternalStore(
    cb => { node.listeners.add(cb); return () => node.listeners.delete(cb); },
    () => {                                        // 快照：派生链实时求值
      const v = readAtom(atom);
      return typeof v === 'object' ? v : v;        // 值类型天然稳定
    },
    () => node.initialized ? node.value : atom.init,
  );
}

export function useSetAtom(atom) {
  return (update) => {
    const get = (dep) => readAtom(dep);
    const set = (target, value) => {
      const n = getNode(target);
      n.value = value;
      n.initialized = true;
      n.listeners.forEach(l => l());               // 通知订阅组件
      // 级联：让依赖它的 derived atom 的订阅者也刷新
      n.dependents.forEach(d => get(d) && getNode(d).listeners.forEach(l => l()));
    };
    atom.write(get, set, update);
  };
}

// ---- 使用 ----
// const countAtom = atom(0);
// const doubleAtom = atom(get => get(countAtom) * 2);   // 派生
// const [count] = useAtomValue(countAtom);
// const [double] = useAtomValue(doubleAtom);            // count 变 -> double 自动重算
// const setCount = useSetAtom(countAtom);
```
