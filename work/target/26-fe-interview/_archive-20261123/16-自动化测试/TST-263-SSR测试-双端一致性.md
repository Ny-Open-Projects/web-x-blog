---
title: [TST-263] 「同构代码」双端行为一致性的测试策略？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-263：「同构代码」双端行为一致性的测试策略？
**答**：
- 核心组件双端渲染对比：node 环境 renderToString vs jsdom render，关键内容一致。
- 环境分支集中化：isServer 判断封装到唯一 util，测试保证每个分支路径都被双端用例覆盖。
- 数据获取双端一致：服务端 prefetch 与客户端 fallback fetch 的数据结构一致（schema 校验）。
- 平台 API 包装层：safeStorage/safeLocation 在服务端返回 no-op 而非抛错。

```javascript
test('双端渲染一致', () => {
  const html = renderToString(<ProductCard sku="A1" />);
  const { getByTestId } = render(<ProductCard sku="A1" />);
  expect(getByTestId('price').textContent).toContain(extractPrice(html));
});
r
```
