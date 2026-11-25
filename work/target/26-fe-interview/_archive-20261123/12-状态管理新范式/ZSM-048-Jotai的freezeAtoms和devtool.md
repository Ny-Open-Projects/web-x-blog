---
title: [ZSM-048] Jotai 开发期工具有哪些（devtools、freeze）？怎么定位「谁改了这个 atom」？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-048：Jotai 开发期工具有哪些（devtools、freeze）？怎么定位「谁改了这个 atom」？
**答**：
- jotai-devtools 提供树状 atom 状态面板、动作历史、时间旅行；`useAtomDebug`/DevTools 组件挂进树即可。
- freezeAtom/atomWithFreeze：开发期把 atom 冻结（Object.freeze），任何「直接改引用内字段」的非法突变立刻抛错，抓住不可变性违规。
- 定位写入来源：包一层 write-only 调试 atom 拦截 set，打印调用栈；或临时 `freeze` 后在 DevTools 断点看 mutation 报错栈。
- 生产建议 tree-shake 掉 devtools 与 freeze，避免 Proxy/Object.freeze 开销。

```javascript
import { freezeAtom } from 'jotai/utils'
import { DevTools } from 'jotai-devtools'

const listAtom = freezeAtom(atom([{ id: 1 }]))
// listAtom[0].id = 2 → TypeError: Cannot assign to read only property

function App() {
  return (<>
    <DevTools /> {/* 开发期面板：树 + 时间线 */}
    <Page />
  </>)
}
```
