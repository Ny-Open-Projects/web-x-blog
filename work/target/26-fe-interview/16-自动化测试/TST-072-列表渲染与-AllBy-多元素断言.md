---
title: [TST-072] 列表类组件怎么测？AllBy 与列表项定位的坑
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-072：列表类组件怎么测？AllBy 与列表项定位的坑
**答**：
- 数量断言：`getAllByRole('listitem')` / `getAllByTestId` 的 length 校验；语义化列表用 ul/li 的 role 天然成立，div 拼的「列表」建议加 role="list"/listitem 或干脆断言 testid 数量。
- 定位单项：「在第 N 项内操作」的正确姿势——先 getAllBy 拿到数组按 index 取，再用 `within(item)` 缩小查询范围；不要 `list.children[n]` 直接戳 DOM（脆弱）。
- 同名文案重复：多条商品同名时 getByText 直接 multiple elements 报错——用 within(item) 或给行加稳定 testid（`row-${id}`）。
- 空态/加载态：列表为空断言 queryByText('暂无数据')；分页加载用 findBy 等新一批出现。

```jsx
import { render, screen, within } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { describe, it, expect, vi } from 'vitest';

const products = [
  { id: 'p1', name: '键盘', price: 399 },
  { id: 'p2', name: '键盘（青轴）', price: 499 },   // 故意同名前缀
];

describe('ProductList', () => {
  it('渲染全部条目并可对指定行加购', async () => {
    const user = userEvent.setup();
    const onAdd = vi.fn();
    render(<ProductList products={products} onAdd={onAdd} />);

    expect(screen.getAllByRole('listitem')).toHaveLength(2);

    // 定位第二行，在其内部找按钮 —— within 是关键
    const secondRow = screen.getAllByRole('listitem')[1];
    await user.click(within(secondRow).getByRole('button', { name: /加入购物车/ }));
    expect(onAdd).toHaveBeenCalledWith('p2');
  });

  it('空列表显示空态', () => {
    render(<ProductList products={[]} onAdd={vi.fn()} />);
    expect(screen.getByText('暂无商品')).toBeInTheDocument();
    expect(screen.queryByRole('listitem')).toBeNull();
  });
});
```
