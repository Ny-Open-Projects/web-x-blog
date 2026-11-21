---
title: [R19-076] Zustand 大型项目如何组织？slice 模式是什么？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-076：Zustand 大型项目如何组织？slice 模式是什么？
**答**：
- 单一巨型 store 会变成"上帝对象"，按业务域拆成 user/cart/order 等 slice，每个 slice 一个文件、独立 StateCreator。
- 合并时用展开运算组合，类型上 store 类型 = 各 slice 类型的交叉。
- 组件订阅必须用 selector 精确到字段，zustand 默认浅比较，selector 返回新对象要用 useShallow。
- 跨 slice 调用通过 get 拿到整个 store，天然支持 slice 间协作。

```typescript
// store/userSlice.ts —— 按业务域拆 slice，最后合并
import type { StateCreator } from 'zustand';

interface User { id: string; name: string }

export interface UserSlice {
  users: User[];
  addUser: (user: User) => void;
}

type AppStore = UserSlice & CartSlice;   // 合并后的全局类型

export const createUserSlice: StateCreator<AppStore, [], [], UserSlice> = (set, get) => ({
  users: [],
  addUser: (user) => set(state => ({ users: [...state.users, user] })),
});

// store/cartSlice.ts 同理导出 createCartSlice，可通过 get() 调用 userSlice 的方法

// store/index.ts —— 合并
import { create } from 'zustand';

export const useAppStore = create<AppStore>()((...a) => ({
  ...createUserSlice(...a),
  ...createCartSlice(...a),
}));

// 组件中用 selector 订阅，避免整树重渲染
// const users = useAppStore(s => s.users);
// const addUser = useAppStore(s => s.addUser);
```
