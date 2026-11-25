---
title: [R19-077] Zustand 的 persist、devtools、immer 中间件如何组合？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-077：Zustand 的 persist、devtools、immer 中间件如何组合？
**答**：
- 中间件按洋葱模型嵌套：`devtools(persist(immer(...)))`，devtools 放最外层让 Redux DevTools 看到最终状态。
- persist 默认整个 state 存 localStorage，必须用 partialize 剔除函数，只持久化数据。
- immer 让"深嵌套不可变更新"写成直接赋值，reducer 可读性大幅提升。
- 持久化结构升级靠 version + migrate，老用户数据平滑迁移。

```typescript
import { create } from 'zustand';
import { persist, devtools, createJSONStorage } from 'zustand/middleware';
import { immer } from 'zustand/middleware/immer';

type SettingsStore = {
  theme: 'light' | 'dark';
  language: string;
  toggleTheme: () => void;
  setLanguage: (lang: string) => void;
};

export const useSettingsStore = create<SettingsStore>()(
  devtools(                                  // 最外层：Redux DevTools 可见
    persist(
      immer((set) => ({
        theme: 'light',
        language: 'zh-CN',
        toggleTheme: () => set(s => {        // immer：直接改 draft
          s.theme = s.theme === 'light' ? 'dark' : 'light';
        }),
        setLanguage: (lang) => set(s => { s.language = lang; }),
      })),
      {
        name: 'app-settings',                          // localStorage key
        storage: createJSONStorage(() => localStorage),
        partialize: s => ({ theme: s.theme, language: s.language }),  // 只持久化数据
        version: 1,                                    // 结构变更时靠 migrate 迁移
      },
    ),
  ),
);
```
