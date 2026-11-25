---
title: [TST-261] SSR 水合（hydration）测试的核心断言是什么？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-261：SSR 水合（hydration）测试的核心断言是什么？
**答**：
- 服务端 HTML 与客户端首帧渲染的结构一致——mismatch 会触发整树重渲染（性能）与闪烁。
- 典型 mismatch 源：时间戳/随机数/浏览器分支（window 判断）在服务端与客户端值不同。
- 测试方法：renderToString 输出与挂载后 DOM 关键节点对比；开发模式下捕获 hydration warning。
- 动态内容规范化：服务端与客户端都用「稳定值」（uid 由服务端下发而非客户端生成）。

```javascript
test('无 hydration mismatch', () => {
  const server = renderToString(<Clock />);
  const el = document.createElement('div');
  el.innerHTML = server;
  const { container } = hydrate(<Clock />, el);      // 开发模式警告会被 React 抛出
  expect(container.innerHTML).toBe(server);           // 结构一致
});
r
```
