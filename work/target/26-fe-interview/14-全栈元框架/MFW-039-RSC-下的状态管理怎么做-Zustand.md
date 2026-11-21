---
title: [MFW-039] RSC 架构下状态管理怎么做？Zustand/Redux 还能用吗？
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-039：RSC 架构下状态管理怎么做？Zustand/Redux 还能用吗？
**答**：
- 先分类：**服务端数据**（列表/详情）尽量不进客户端 store——直接在 Server Component 取、RSC Payload 直达；只有**客户端交互状态**（表单草稿、UI 开关、乐观更新缓存）才用 store。
- Zustand 完全可用：Provider 标 `'use client'`，包在 layout 里（导航不卸载），所有消费组件自然也在 client 图中。
- Redux/TanStack Query 同理可用，但都要在 client 边界内；TanStack Query 与 RSC 的分工见「SSR 脱水复水」专题卡。
- 反模式：把服务端拿到的数据一股脑灌进 Zustand 当「初始状态」——数据已经通过 RSC Payload 传输，重复灌一遍只会增大 bundle 与复杂度。
- 组合模式：**RSC 管只读数据，Server Action 变更后 revalidate；client store 只管跨组件的 UI 协作**。

```jsx
// app/store.ts —— 全局 UI 状态：client 边界内
'use client';
import { create } from 'zustand';

export const useUI = create((set) => ({
  sidebarOpen: false,
  toggleSidebar: () => set((s) => ({ sidebarOpen: !s.sidebarOpen })),
}));
```

```jsx
// app/layout.tsx —— 数据不进 store：Server 直取
import Sidebar from './sidebar'; // 'use client' 组件

export default async function Layout({ children }) {
  const nav = await getNavTree();          // 服务端数据走 RSC Payload
  return (
    <div>
      <Sidebar nav={nav} />                 {/* UI 状态用 Zustand，数据靠 props */}
      {children}
    </div>
  );
}
```
