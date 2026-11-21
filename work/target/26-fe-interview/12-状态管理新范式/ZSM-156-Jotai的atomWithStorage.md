---
title: [ZSM-156] Jotai 的 atomWithStorage 怎么做持久化和跨标签同步？和 Zustand persist 的差异是什么？
date: 2026-11-19
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-156：Jotai 的 atomWithStorage 怎么做持久化和跨标签同步？和 Zustand persist 的差异是什么？
**答**：
- atomWithStorage：atom 声明即持久化——读时从 localStorage 反序列化（JSON 默认），写时同步写回，且内置监听 storage 事件做跨标签页同步，一行搞定 Zustand persist + 跨 tab 的组合功能。
- 与 Zustand persist 的差异：persist 是「事后快照整个 store 再挑字段」，atomWithStorage 是「按 atom 粒度各自存取」，天然避免整包序列化；但多 atom 之间没有事务一致性（Zustand 一次 set 是原子的）。
- 定制点：createJSONStorage 换存储介质（sessionStorage/IndexedDB/自实现 AsyncStorage），自定义 stringify/parse 支持 Map/Date 等非 JSON 类型；`unstable_shouldOnBeforeMount` 控制首挂载是否用本地值覆盖默认值。
- 坑：SSR 端 localStorage 不存在，默认在客户端挂载后才读取，首帧与服务端渲染不一致会触发 hydration 警告，需要 suppress 或门控。

```javascript
import { atomWithStorage, createJSONStorage } from 'jotai/utils'

// 单 atom 持久化 + 跨标签同步
export const themeAtom = atomWithStorage('app-theme', 'dark')
export const sidebarAtom = atomWithStorage('sidebar-collapsed', false, {
  ...createJSONStorage(() => sessionStorage),   // 换介质
  unstable_getOnInit: true,                     // 初始渲染即读存储，减少闪变
})

// 跨标签：B 标签改主题，A 标签 storage 事件自动更新（内置）
function ThemeToggle() {
  const [theme, setTheme] = useAtom(themeAtom)
  return <button onClick={() => setTheme(t => t === 'dark' ? 'light' : 'dark')}>
    {theme}
  </button>
}
```
