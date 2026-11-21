---
title: [TST-189] BDD 与 Given/When/Then：怎么把验收标准变成可执行测试？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-189：BDD 与 Given/When/Then：怎么把验收标准变成可执行测试？
**答**：
- BDD 的核心不是工具而是「用行为描述对齐三方」：产品写 Given（前置）/When（动作）/Then（结果）格式的验收标准，开发把 AC 直接翻译成测试骨架，测试即需求文档——评审时三方看的是同一份东西。
- 落地两级：轻量级（推荐）——在测试命名与结构里用 GWT 语义（describe = Feature，it = Scenario，beforeEach = Given，操作 = When，断言 = Then），不引入额外框架；重量级——Cucumber/Gherkin（.feature 文件 + step 定义），适合 QA 主导编写场景的大团队，前端一般用不上全套。
- GWT 写法规范：一个 Scenario 只验证一条业务规则（复数规则 = 拆分）；Then 断言用户可感知的结果而非实现；数据在 Given 里显式给出（不给「默认数据」暗坑）。
- 价值与陷阱：价值是 AC 可执行化 + 沟通成本下降；陷阱是 Gherkin 的 step 定义层维护成本（业务词到代码的翻译层）——团队小就别上，describe/it 已经足够表达。
- 追问钩子：产品改需求后测试怎么办？——AC 变更 = 测试变更 = PR 里可见，需求变更第一次就变成可追溯的行为变更，这正是 BDD 的防漂移价值。

```javascript
// AC（产品文档）：
// Given 用户购物车里有 2 件商品
// When 用户移除其中 1 件
// Then 合计金额更新且商品数显示 1

describe('Feature: 购物车结算金额', () => {
  const setup = () => renderWithProviders(<CartPage />, {
    preloadedState: { cart: { items: [makeItem(100), makeItem(200)] } }, // Given
  });

  it('Scenario: 移除商品后金额与件数同步更新', async () => {
    const utils = setup();
    await userEvent.click(utils.getByTestId('remove-item-1'));            // When
    expect(utils.getByText('共 1 件')).toBeInTheDocument();               // Then
    expect(utils.getByText('合计 ¥200.00')).toBeInTheDocument();
  });
});
```
