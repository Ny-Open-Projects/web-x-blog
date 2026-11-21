---
title: [ZSM-059] 哪些状态不适合放进 Jotai atom？举出四类反例及替代方案
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-059：哪些状态不适合放进 Jotai atom？举出四类反例及替代方案
**答**：
- 服务端数据（列表、详情）：atom 异步无缓存策略、无失效协作，放 TanStack Query/SWR。
- 高频帧数据（鼠标、拖拽坐标、动画进度）：进 atom 会触发渲染风暴，用 ref + subscribe 瞬时更新。
- 本组件私有的输入框中间态：useState 足够，上 atom 反而增加全局命名与释放负担。
- 大型不可序列化对象（DOM 节点、编辑器实例、worker 句柄）：atom 值会被 devtools 序列化、调试面板拖慢，用 useRef/module 变量 + atom 只存句柄 id。
- 判据一句话：atom 适合「需要跨组件响应且更新频率可控」的数据。

```javascript
// 反例修正
const editorAtom = atom(null)                 // 差：塞实例
const editorIdRef = useRef('editor-1')        // 好：ref 持有
const activeEditorAtom = atom('editor-1')     // atom 只存可序列化 id

const cursorAtom = atom({ x: 0, y: 0 })       // 差：高频
// 好：onMouseMove 里直接 ref.style.transform，不入 atom
```
