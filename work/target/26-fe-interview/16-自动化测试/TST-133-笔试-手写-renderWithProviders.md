---
title: [TST-133] 笔试：手写 renderWithProviders（Router/Store/Theme 统一包裹）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-133：笔试：手写 renderWithProviders（Router/Store/Theme 统一包裹）
**答**：
- 需求：实现 `renderWithProviders(ui, options)`——把测试里重复的 Provider 包裹（Router、Redux/Zustand store、Theme、I18n、MSW）收敛成一个 helper：支持传路由初始路径、注入专属 store、覆盖主题，返回 RTL 的查询工具 + 附加工具（navigate 助手）。
- 设计要点：① options 全部可选、有合理默认（内存路由、空 store）；② 返回值透传 RTL render 的结果并额外暴露 `store`（断言状态）与 `history`（断言跳转）；③ 不在 helper 里藏 beforeEach——数据 mock（MSW handlers）由用例显式声明，保持可读。
- 反模式警告：helper 里不要偷偷塞全局 mock/定时器，否则用例行为不可预测；helper 应该只是「结构收敛」不是「行为魔法」。

```jsx
// test-utils.tsx
import { render } from '@testing-library/react';
import { createMemoryRouter, RouterProvider } from 'react-router-dom';
import { Provider } from 'react-redux';
import { configureStore } from '@reduxjs/toolkit';
import { ThemeProvider } from '@/theme';
import rootReducer from '@/store';

export function renderWithProviders(ui, {
  route = '/',
  routes = [],                       // 额外路由配置（详情页等）
  preloadedState,
  theme = 'light',
} = {}) {
  const store = configureStore({ reducer: rootReducer, preloadedState });
  const router = createMemoryRouter(
    [{ path: '*', element: ui }, ...routes],
    { initialEntries: [route] },
  );

  const utils = render(
    <Provider store={store}>
      <ThemeProvider value={theme}>
        <RouterProvider router={router} />
      </ThemeProvider>
    </Provider>,
  );

  return {
    ...utils,
    store,                             // 断言状态：store.getState()
    router,                            // 断言跳转：router.state.location.pathname
    rerenderWith: (newUi) =>           // 支持带同样 provider 的重渲染
      utils.rerender(
        <Provider store={store}><ThemeProvider value={theme}><RouterProvider router={router} /></ThemeProvider></Provider>
      ),
  };
}

// ---- 用例 ----
test('未登录跳转登录页', () => {
  const { router, store } = renderWithProviders(<Profile />, {
    route: '/profile',
    preloadedState: { auth: { user: null } },
  });
  expect(router.state.location.pathname).toBe('/login');
  expect(store.getState().auth.user).toBeNull();
});
```

**评分点**：
1. options 可选且默认合理，不强制每个用例传全参。
2. 返回 store/router 供状态与跳转断言（不只是渲染）。
3. helper 不藏全局副作用 mock（结构收敛而非行为魔法）。
4. 支持 preloadedState 精确构造初始状态（避免层层 dispatch）。
