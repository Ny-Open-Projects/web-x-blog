---
title: [ZSM-056] 笔试：手写 Jotai 的 selectAtom（切片 + 缓存比较）
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 笔试题, ZSM]
type: 笔试题
---

## ZSM-056：手写 Jotai 的 selectAtom（切片 + 缓存比较）

**答**：
- 实现 `selectAtom(atom, selector, equalityFn = Object.is)`：返回一个只读派生 atom。
- 关键行为：源 atom 变化时执行 selector，结果与上次相等（equalityFn）就**保持旧引用**，订阅者不重渲染。
- selector 对同一输入应只跑一次并缓存。

```javascript
export function selectAtom(atom, selector, equalityFn = Object.is) {
  let cache = { has: false, input: undefined, output: undefined }
  const read = get => {
    const input = get(atom)               // 源值
    if (cache.has && cache.input === input) return cache.output
    const output = selector(input)
    if (!cache.has || !equalityFn(cache.output, output)) {
      cache = { has: true, input, output } // 结果变化才更新缓存引用
    } else {
      cache = { ...cache, input }          // 结果相等：保留旧 output 引用
    }
    return cache.output
  }
  return atom(read) // 只读派生
}

const listAtom = atom([{ id: 1, on: true }, { id: 2, on: false }])
const activeAtom = selectAtom(
  listAtom,
  l => l.filter(i => i.on),
  shallowEqual, // 浅比较数组
)
```

**评分点**：
- 双层缓存：input 引用相等直接短路；output 相等保留旧引用，防止新数组触发渲染。
- equalityFn 参数化，默认 Object.is。
- 返回的是合法只读 atom，可继续参与派生链。
- 说出与 Zustand useShallow 的对应关系：都在「新引用」问题上做缓存。
