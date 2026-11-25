---
title: [ZSM-504] Jotai 的 atom 内部结构与依赖图是怎么维护的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-504：Jotai 的 atom 内部结构与依赖图是怎么维护的

**答**：
- 每个 atom 在 store 里对应一个 atomState： `{ d: 依赖 atom 的 Map（含版本号）, p: promise, v: 当前值 }`。读 atom 时递归沿 `d` 收集上游。
- 依赖是**读取时动态收集**的：`atom.read(get)` 里每次调用 `get(other)` 都记录 `atom → other` 依赖边。同一个 atom 本次读用到了哪些上游，取决于 read 函数实际执行路径（条件派生自动按需依赖）。
- store 维护 `mounted` 集合：组件挂载订阅后才把 atom 标记 mounted，上游未挂载的依赖通过「向下游传播」激活。
- 更新传播：set 一个 atom 后，store 遍历其依赖图下游，逐个使依赖版本失效并重算；派生 atom 有 promise 缓存，依赖没变就不重算。
- 追问钩子：条件分支派生（`read` 里 if 选择不同上游）每次重算会重建依赖边，这就是「动态依赖图」——比 Redux 静态 selector 链灵活，但重算成本不可静态分析。

```javascript
// 简化的 read 与依赖收集
function readAtomState(store, atom) {
  const atomState = getAtomState(atom)
  const deps = new Map() // 本次读取收集到的依赖
  const get = (dep) => {
    deps.set(dep, getVersion(dep))   // 记边 + 版本号
    return readAtomState(store, dep).v
  }
  const value = atom.read(get)       // 用户 read 函数，可能走不同分支
  atomState.d = deps                 // 整体替换：本轮没用到的边被剪掉
  atomState.v = value
  return atomState
}

// 例：条件派生
const modeAtom = atom('a')
const dataAtom = atom((get) =>
  get(modeAtom) === 'a' ? get(atomA) : get(atomB)
)
// mode 为 'a' 时依赖图只有 mode+atomA，atomB 更新不会触发重算
```
