---
title: [ZSM-703] Storybook 里的状态调试：args、decorators 与 MSW 分层
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-703：Storybook 里的状态调试：args、decorators 与 MSW 分层

**答**：
- Storybook 的状态注入三层：1) **props/args**（纯受控组件的输入）；2) **decorators**（包裹 Provider——StoreDecorator 预置 zustand 状态、QueryClientDecorator 注入 mock client）；3) **MSW handlers**（拦截网络层，给 TanStack Query/RTK Query 供给确定性数据）。分层原则：数据来自网络就 mock 网络层（不要绕过 Query 直接 setState，否则测的不是真实数据流）。
- 状态组合的参数化：`states` arg 工厂——一个组件 story 覆盖「loading/error/empty/partial」四态，每态由 decorator 里的 store patch + MSW 场景共同决定；`play` 函数还能模拟交互后的状态（点击后断言 + 截图）。
- 调试收益：组件在隔离环境中「任意状态可直达」——复现「空数据+长标题溢出」这种线上边角态不需要真造数据，十秒定位；配合 ZSM-702 的视觉回归把 Storybook 当截图源。
- msw-storybook-addon 的场景切换：`mswLoader` + story 参数 `msw: { handlers: cartHandlers }`——同一组件不同 story 挂不同 handler（成功/慢响应/500）。
- 追问钩子：Storybook 状态与真实 app 的一致性风险——decorator 预置的状态可能与真实初始化路径不同（漏了 hydrate/权限注入），保持「状态构造代码与 app 共享同一模块」（fixture 从 store 模块导出，不要 story 里手写）。

```javascript
// decorators 分层示例
import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
import { setupServer } from 'msw/node'
import { useStore } from '../store'

const queryClient = new QueryClient({
  defaultOptions: { queries: { retry: false } },
})

const StoreDecorator = (Story, { parameters }) => {
  // 预置状态（fixture 共享自 store 模块，不手写）
  if (parameters.store) {
    useStore.setState(parameters.store)
  }
  return <Story />
}

const QueryDecorator = (Story) => (
  <QueryClientProvider client={queryClient}>
    <Story />
  </QueryClientProvider>
)

// CartList.stories.tsx
const meta = {
  title: 'Cart/CartList',
  decorators: [StoreDecorator, QueryDecorator],
}
export default meta

export const Empty = {
  parameters: {
    store: { items: [] },
    msw: { handlers: [emptyCartHandler] },
  },
}

export const Loading = {
  parameters: {
    msw: { handlers: [delayedHandler(3000)] },   // 慢响应 → 组件走 loading 态
  },
}

export const Error = {
  parameters: {
    msw: { handlers: [errorHandler] },           // 500 → error 态
  },
}

// play 函数：交互后状态断言
Empty.play = async ({ canvasElement }) => {
  const canvas = within(canvasElement)
  expect(canvas.getByText('购物车是空的')).toBeInTheDocument()
}
```
