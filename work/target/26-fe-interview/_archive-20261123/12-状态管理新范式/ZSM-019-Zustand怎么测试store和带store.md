---
title: [ZSM-019] Zustand 的 store 和组件怎么测试？reset 状态要注意什么？
date: 2026-11-18
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-019：Zustand 的 store 和组件怎么测试？reset 状态要注意什么？
**答**：
- store 测试不依赖 React：直接 `getState()` / `setState()` / 调 action 断言，最稳；中间件行为（persist/devtools）可在 node 环境验证（mock storage）。
- 组件测试用 `renderHook` + `act` 触发 action，或 RTL 渲染组件后断言 UI；测试间必须 reset，否则状态泄漏产生偶发失败。
- reset 要保留函数字段：`setState(initialState, true)` 用 replace 会把 actions 也删掉，正确做法是只重置数据切片或提前保存初始数据快照。
- vi.mock/jest.mock 可以整 store 替换，但优先测真 store + reset，mock 太多说明 store 与副作用耦合过深。

```javascript
const initialData = { count: 0 }
const useCounter = create(set => ({ ...initialData, inc: () => set(s => ({ count: s.count + 1 })) }))

afterEach(() => {
  // 只重置数据，保留 inc 等函数
  useCounter.setState(initialData)
})

test('inc', () => {
  const { result } = renderHook(() => useCounter(s => s.count))
  act(() => useCounter.getState().inc())
  expect(result.current).toBe(1)
})
```
