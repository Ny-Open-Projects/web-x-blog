---
title: [ZSM-359] 热更新（HMR）时 store 状态为什么会被重置怎么保
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-359：热更新（HMR）时 store 状态为什么会被重置，怎么保

**答**:
- 原因：store 模块被 HMR 替换后重新执行 `create()`，新实例替换旧引用；订阅在旧实例上的组件拿到的是「新 store + 旧数据」或直接重置
- 保存方案：模块级缓存（import.meta.hot.data）保存旧状态，重建时用 `create(() => saved ?? initial)` 恢复；或 store 挂到 window 单例（HMR 不清 window）
- 验收面：HMR 只影响开发体验，但「每次热更状态归零」会拖慢调试（反复造数据），值得花 10 行代码解决
- persist 的意外红利：开了 persist 的 store HMR 后从 storage 复水，状态自然保留——但要注意开发数据与真实数据的隔离（环境前缀）

```javascript
// Vite HMR 状态保留
if (import.meta.hot) {
  import.meta.hot.accept((mod) => {
    import.meta.hot.data.state = useStore.getState()    // 存旧状态
    mod.rehydrate(import.meta.hot.data.state)           // 新模块恢复
  })
}
// 简易替代：window 单例
const store = (window.__store ??= create(() => ({ count: 0 })))
```
