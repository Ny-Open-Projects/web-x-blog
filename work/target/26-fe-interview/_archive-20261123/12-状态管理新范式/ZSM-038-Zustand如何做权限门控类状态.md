---
title: [ZSM-038] 用 Zustand 做全局权限/主题这类低频高影响状态，设计上有什么讲究？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-038：用 Zustand 做全局权限/主题这类低频高影响状态，设计上有什么讲究？
**答**：
- 低频高影响（权限、主题、用户信息）适合单独 store：变更少、读取多，selector 按 key 拆开，避免无关组件被牵连。
- 权限要区分「数据」与「判定」：store 存权限集（数组/Set），判定逻辑做成纯函数 `can(code)`，组件订阅 `can` 的结果而不是整个权限数组。
- 主题切换要注意 CSS 变量与 class 的原子切换，store 只存一个 theme 字段，别存几十个颜色值。
- 持久化 + 水合竞态：主题闪变用内联脚本提前设 class，store 水合后再对齐，避免 FOUC。

```javascript
const usePerms = create(set => ({
  codes: [],
  setCodes: codes => set({ codes: [...new Set(codes)] }), // 去重稳定
}))
// 纯函数判定：订阅返回布尔值，粒度最细
export const useCan = code => usePerms(s => s.codes.includes(code))
// 组件：const editable = useCan('doc:edit')   ← 权限集其他变化不触发
```
