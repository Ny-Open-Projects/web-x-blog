---
title: [ZSM-502] persist 中间件的 createJSONStorage 存储层是怎么设计的
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-502：persist 中间件的 createJSONStorage 存储层是怎么设计的

**答**：
- `createJSONStorage` 返回一个「同步读、异步写、双 getJSON/ setJSON」的 StateStorage 适配器，persist 只依赖这个接口，不关心底层是 localStorage、IndexedDB 还是 AsyncStorage。
- 接口约定四方法：`getItem/setItem/removeItem`，且 `setItem` 允许返回 Promise——RN 环境 AsyncStorage 全异步也能无痛接入。
- JSON 序列化层和存储层是分离的：`createJSONStorage(() => localStorage)` 负责字符串↔对象转换，自定义存储只需给字符串级 API，不用自己 JSON.stringify。
- 若 `getItem` 返回 Promise，persist 的 `hydrate` 变异步，`onRehydrateStorage` 回调在完成时触发；没配 storage 时返回 undefined，persist 静默跳过。
- 追问钩子：getItem 抛异常时 persist 会 warn 并视为「无持久化数据」，走 partialize 默认值初始化，不会让应用白屏。

```javascript
// persist 内部存储调用骨架
const storage = options.storage ?? createJSONStorage(() => localStorage)
// StateStorage 接口：
// interface StateStorage {
//   getItem: (name: string) => string | null | Promise<string | null>
//   setItem: (name: string, value: string) => void | Promise<void>
//   removeItem: (name: string) => void | Promise<void>
// }

// hydrate 流程（简化）
async function hydrate() {
  try {
    const str = await storage.getItem(options.name)   // 可能同步可能异步
    if (!str) return                                  // 首次无数据
    const stored = JSON.parse(str)                    // { state, version }
    const migrated = options.version !== stored.version
      ? await options.migrate?.(stored.state, stored.version)
      : stored.state
    set(merged)                                       // merge 默认浅合并：持久值覆盖初始值
  } catch (e) {
    console.warn(`[persist] hydrate failed for '${options.name}'`, e)
    // 不 throw：持久层损坏不应阻塞首屏
  }
}
```
