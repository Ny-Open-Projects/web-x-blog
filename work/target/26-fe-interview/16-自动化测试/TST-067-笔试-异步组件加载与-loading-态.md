---
title: [TST-067] 笔试：为异步加载的商品列表组件写完整测试（loading/成功/失败）
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-067：笔试：为异步加载的商品列表组件写完整测试（loading/成功/失败）
**答**：
- 需求：`<ProductList />` 挂载时请求接口：loading 骨架屏 → 成功渲染列表 → 失败显示重试按钮（点击重新请求）。三个状态都要测。
- 要点：成功态用 findBy（异步出现）；失败态 mockRejectedValue；重试点击后再次 await findBy 验证第二次请求；loading 态断言骨架存在（mock 永不 resolve 或用 delay）。
- 边界：每次用例 mockReset 防串；断言列表项数量与首项内容（不只是「渲染了」）。

```jsx
import { render, screen } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi, beforeEach } from 'vitest';
import { api } from './api';
import ProductList from './ProductList';

vi.mock('./api', () => ({ api: { fetchProducts: vi.fn() } }));

describe('ProductList 三态', () => {
  beforeEach(() => vi.mocked(api.fetchProducts).mockReset());

  it('loading 态显示骨架屏', () => {
    vi.mocked(api.fetchProducts).mockReturnValue(new Promise(() => {}));
    render(<ProductList />);
    expect(screen.getByTestId('skeleton')).toBeInTheDocument();
  });

  it('成功态渲染商品列表', async () => {
    vi.mocked(api.fetchProducts).mockResolvedValue([
      { id: 1, name: '键盘', price: 399 },
      { id: 2, name: '鼠标', price: 199 },
    ]);
    render(<ProductList />);
    expect(await screen.findByText('键盘')).toBeInTheDocument();
    expect(screen.getByText('¥399.00')).toBeInTheDocument();
    expect(screen.getAllByRole('listitem')).toHaveLength(2);   // 数量断言
  });

  it('失败态显示错误与重试，点击后重新请求成功', async () => {
    vi.mocked(api.fetchProducts)
      .mockRejectedValueOnce(new Error('network'))
      .mockResolvedValueOnce([{ id: 1, name: '键盘', price: 399 }]);
    render(<ProductList />);

    expect(await screen.findByText('加载失败')).toBeInTheDocument();
    await userEvent.click(screen.getByRole('button', { name: '重试' }));
    expect(await screen.findByText('键盘')).toBeInTheDocument();
    expect(api.fetchProducts).toHaveBeenCalledTimes(2);        // 两次请求
  });
});
```
**评分点**：
- 三态全覆盖（loading/成功/失败），失败含重试闭环。
- findBy 处理异步、getAllByRole 断言数量。
- mockRejectedValueOnce + mockResolvedValueOnce 链式编排两次请求。
- beforeEach mockReset 防用例间污染。
