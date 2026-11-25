---
title: [R19-387] Context 性能深水：传播机制与 bailout 击穿
date: 2026-11-21
categories: [React19]
tags: [前端面试, 面试题, 性能]
type: 面试题
---

## R19-387：Context 性能深水：传播机制与 bailout 击穿

**答**：
- 传播机制：Provider value 变化 → 其子树的 beginWork 强制重新渲染（bailout 失效）——context 变更是少数「击穿 memo」的力量（老 value/new value Object.is 比较）
- 击穿范围：整棵 Provider 子树（即使组件没消费 context）——这是 Context 滥用导致全页重渲的根源；消费组件才「读 value」，未消费的组件只是被「重执行」（React 靠子组件自己的 bailout 二次收口）
- 优化三板斧：value 拆分（多个小 Context 而不是一个大对象）、Provider 下沉（包裹真正消费的子树）、value 引用稳定（useMemo/拆 props）
- didPropagate 检查优化：React 对未消费的组件做 fast path——dependencies 位图（React 18+）记录「该组件依赖哪些 context」，无关 context 变化可继续 bailout
- 与状态库的对比：状态库（selector 级订阅）天然解决粒度问题——全局高频状态（主题除外）不建议裸 Context

```jsx
// 反模式: 大对象 value 全页传播
<UserCtx.Provider value={{ user, perms, prefs, ... }}>   // 任一字段变全子树重跑
// 正解: 拆分 + 稳定
<PermCtx.Provider value={perms}>   {/* useMemo 稳定 */}
  <PrefsCtx.Provider value={prefs}> ... </PrefsCtx.Provider>
</PermCtx.Provider>
```
