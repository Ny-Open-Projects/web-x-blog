---
title: [TST-678] 自然语言测试步骤转成 Playwright 代码怎么实现？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-678：自然语言测试步骤转成 Playwright 代码怎么实现？

**答**：
- 结论：用「意图槽位填充」而非直接生成代码——解析出动作/目标/断言三个槽位，再套模板。
- 模板保证输出确定、可 lint；模型只负责槽位识别，降低幻觉。
- 生成后跑一次冒烟验证可执行性，失败转人工修正。
- 追问钩子：用户写「点那个按钮」，模型怎么确定是哪个按钮？

```javascript
const TEMPLATES = {
  click: (t) => `await page.getByRole('button',{name:'${t}'}).click();`,
  fill: (t, v) => `await page.getByLabel('${t}').fill('${v}');`,
  expect: (t) => `await expect(page.getByText('${t}')).toBeVisible();`,
};
function nlpToCode(step) {
  const m = step.match(/点击「(.+)」|输入「(.+)」到「(.+)」|断言「(.+)」可见/);
  if (!m) return '// 无法解析，需人工';
  if (m[1]) return TEMPLATES.click(m[1]);
  if (m[2]) return TEMPLATES.fill(m[3], m[2]);
  return TEMPLATES.expect(m[4]);
}
console.log(nlpToCode('点击「提交」'));
```
