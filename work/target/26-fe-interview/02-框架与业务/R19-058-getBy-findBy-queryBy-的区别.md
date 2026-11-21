---
title: [R19-058] getBy、findBy、queryBy 的区别？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-058：getBy、findBy、queryBy 的区别？
**答**：
- getBy：同步查找，找不到立即抛错，用于断言当前一定存在的元素。
- findBy：返回 Promise，默认一秒内轮询等待元素出现，适合异步渲染的内容。
- queryBy：找不到返回 null 而不抛错，专门用于断言"元素不存在"。
- 复数形式 getAllBy/findAllBy/queryAllBy 语义相同，返回数组。

```jsx
test('三种查询的使用场景', async () => {
  render(<Profile userId="1" />);

  // 同步确定存在
  expect(screen.getByRole('heading', { name: '个人主页' })).toBeInTheDocument();

  // 异步数据，等待出现
  await screen.findByText('异步加载的用户名');

  // 断言不存在：只有 queryBy 不抛错
  expect(screen.queryByText('不该出现的文案')).toBeNull();
});
```
