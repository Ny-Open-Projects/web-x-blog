---
title: [AIC-237] AI 喜欢生成大快照测试，快照膨胀后无人敢看，如何治理？
date: 2026-11-20
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-237：AI 喜欢生成大快照测试，快照膨胀后无人敢看，如何治理？
**答**：
- 禁止大对象整树快照：要求断言关键节点（角色、文案、状态类名）。
- 必须用快照时限制规模（< 50 行）且须人工评审首版快照。
- 快照更新要有语义：CI 中快照 diff 需要关联说明，禁止无脑 -u。
- 用语义化断言库（testing-library 的 getByRole）替代 DOM 快照。

```javascript
// 反例
expect(container.innerHTML).toMatchSnapshot(); // 整树快照，diff 无法人审
// 正例
expect(screen.getByRole('button', { name: '提交订单' })).toBeEnabled();
expect(screen.getByTestId('price')).toHaveTextContent('¥129.00');
r
```
