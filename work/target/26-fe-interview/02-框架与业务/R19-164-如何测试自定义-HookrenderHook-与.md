---
title: [R19-164] 如何测试自定义 Hook？renderHook 与自定义 render 有什么用法？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-164：如何测试自定义 Hook？renderHook 与自定义 render 有什么用法？
**答**：
- `renderHook`（RTL 内置）把 hook 挂进一个测试宿主组件，返回 result.current 读取最新返回值；重渲染用 `rerender(newProps)`。
- act 约束同样适用：触发 hook 内部状态变化的操作（调用 result.current 的函数、触发 effect）都要包 act。
- 项目级推荐自定义 `render`/`renderHook`：内置 Provider 组装（Router/Query/Theme/Store），测试代码不再关心依赖注入。
- hook 依赖外部模块（如 useLocation）时用 wrapper 传入 MemoryRouter 或 vi.mock 提供受控实现。

```tsx
// use-pagination.test.tsx —— hooks 测试 + 自定义 renderHook
import { renderHook, act } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import { useState } from 'react';

// 被测 hook：分页 + 越界钳制
function usePaginationImpl(total: number, pageSize = 10) {
  const [page, setPage] = useState(1);
  const pages = Math.max(1, Math.ceil(total / pageSize));
  const go = (p: number) => setPage(Math.min(Math.max(1, p), pages));
  return { page, go, pages };
}

describe('usePagination', () => {
  it('go 越界时被钳制在合法范围', () => {
    const { result, rerender } = renderHook(
      ({ total }) => usePaginationImpl(total),   // hook 挂进测试宿主
      { initialProps: { total: 45 } },
    );
    expect(result.current.page).toBe(1);
    expect(result.current.pages).toBe(5);

    act(() => result.current.go(99));            // 状态更新必须包 act
    expect(result.current.page).toBe(5);         // 钳制到最后一页

    act(() => result.current.go(0));
    expect(result.current.page).toBe(1);

    rerender({ total: 15 });                     // props 变化重渲染：pages 收缩
    expect(result.current.pages).toBe(2);
  });
});

// test-utils.tsx —— 项目级自定义 render：Provider 一次组装
import { render, renderHook, type RenderOptions } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';

function createTestQueryClient() {
  return new QueryClient({
    defaultOptions: { queries: { retry: false, gcTime: 0 } },
  });
}

export function renderWithProviders(
  ui: React.ReactElement,
  { route = '/', ...options }: RenderOptions & { route?: string } = {},
) {
  const qc = createTestQueryClient();
  const Wrapper = ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={qc}>
      <MemoryRouter initialEntries={[route]}>
        {children}
      </MemoryRouter>
    </QueryClientProvider>
  );
  return { ...render(ui, { wrapper: Wrapper, ...options }), queryClient: qc };
}

export function renderHookWithProviders(hook: () => unknown, options = {}) {
  const qc = createTestQueryClient();
  const Wrapper = ({ children }: { children: React.ReactNode }) => (
    <QueryClientProvider client={qc}>{children}</QueryClientProvider>
  );
  return renderHook(hook, { wrapper: Wrapper, ...options });
}
```
