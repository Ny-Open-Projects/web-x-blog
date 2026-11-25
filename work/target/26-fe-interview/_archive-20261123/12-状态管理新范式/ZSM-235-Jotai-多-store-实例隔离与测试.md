---
title: [ZSM-235] Jotai 不用 Provider 时全局 store 怎么隔离测试
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-235：Jotai 不用 Provider 时全局 store 怎么隔离测试

**答**：
- 无 Provider 模式用模块级默认 store，测试间状态会串——用 `createStore()` + `<Provider store={testStore}>` 每个测试新建，天然隔离
- store 句柄可脱离 React 直接读写：`store.get/set/sub(atom)`，适合测试断言与模拟事件源
- SSR/多租户隔离同理：每请求创建 store 传入 Provider，避免用户间数据串（与 queryClient 每请求新建同构）
- 混合模式：默认全局 store + 关键域用命名 store，代码上通过 Provider 树区分，减少全局单例的心智负担

```javascript
import { createStore, Provider } from 'jotai'

test('cart adds item', () => {
  const store = createStore()               // 每测试新建
  render(<Provider store={store}><Cart /></Provider>)
  act(() => store.set(itemsAtom, [{ id: 1 }]))
  expect(store.get(countAtom)).toBe(1)
})
```
