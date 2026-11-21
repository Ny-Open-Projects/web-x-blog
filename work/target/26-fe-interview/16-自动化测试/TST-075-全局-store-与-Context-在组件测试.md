---
title: [TST-075] 组件依赖全局状态（Redux/Zustand/Context）时怎么测？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-075：组件依赖全局状态（Redux/Zustand/Context）时怎么测？
**答**：
- 三种注入方式：① 真实 Provider 包裹（render(<Provider store={makeStore()}>…)）——集成最真，注意每用例新建 store 实例防串；② 定制 render 工具（renderWithProviders）统一包裹 router+store+theme，工程标配；③ mock hook——`vi.mock('zustand 库路径')` 或直接 mock 业务 store 模块的 useXxx 返回固定值，适合只测组件展示分支。
- Zustand 特殊性：store 是模块级单例，测试里 `useStore.setState({ ... })` 直接灌状态、`useStore.getState().reset()` 清理——比 mock 更简单。
- 取舍：测「组件在给定状态下的渲染」用真 Provider/mocked hook 都行；测「交互触发 action」用真 store + spy action。
- 追问钩子：Context 的自定义 hook 消费者测试用「测试专用 Provider」注入测试值，而不是 mock 模块。

```jsx
// 测试工具：renderWithProviders（统一包裹全局依赖）
import { render } from '@testing-library/react';
import { Provider } from 'react-redux';
import { makeStore } from './store';

export function renderWithProviders(ui, { preloadedState } = {}) {
  const store = makeStore(preloadedState);      // 每次新建实例
  const utils = render(<Provider store={store}>{ui}</Provider>);
  return { store, ...utils };
}

// Zustand：直接 setState 灌值
import { useCartStore } from './cartStore';
beforeEach(() => useCartStore.setState({ items: [], total: 0 }));  // 清理防串

test('购物车非空显示结算按钮', () => {
  useCartStore.setState({ items: [{ id: 'p1' }], total: 100 });
  render(<CartSummary />);
  expect(screen.getByRole('button', { name: '去结算' })).toBeInTheDocument();
});
```
