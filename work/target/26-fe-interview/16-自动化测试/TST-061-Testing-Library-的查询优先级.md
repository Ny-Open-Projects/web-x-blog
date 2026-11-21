---
title: [TST-061] Testing Library 的查询优先级是什么？为什么这样排？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-061：Testing Library 的查询优先级是什么？为什么这样排？
**答**：
- 官方优先级：① getByRole（含 accessible name）→ ② getByLabelText / getByPlaceholderText → ③ getByText → ④ getByDisplayValue → ⑤ getByAltText / getByTitle → ⑥ getByTestId（最后兜底）。
- 排序逻辑：越靠前越接近「用户如何感知元素」（无障碍语义），测试越贴近真实交互，且天然顺带做了可访问性检查（缺 role/label 一步就暴露）。
- test垫底原因：data-testid 是纯实现细节，用户不可感知；但动态文本、重复 role + 相似文案时它是必要兜底（如列表第 N 项）。
- getByRole 附加能力：`{ name }` 匹配 accessible name、`{ hidden: false }` 排除 aria-hidden、还能检查元素是否可交互（hidden 元素查不到）。
- 追问钩子：优先级不是教条——按钮用 role、输入用 label、列表项用 testid（带稳定 id）是常见合理组合。

```jsx
// 按优先级写查询
render(<OrderForm />);

// ① role + accessible name：最推荐
screen.getByRole('button', { name: /提交订单/i });
screen.getByRole('textbox', { name: '收货地址' });   // <label>收货地址<input/></label>

// ② label：表单控件次选
screen.getByLabelText('手机号');

// ③ text：静态文案
screen.getByText('运费 ¥10');

// ⑥ testid：动态内容兜底
screen.getByTestId(`order-row-${order.id}`);   // 行内动态 id，role/text 都不稳定时
```
