---
title: [ZSM-266] 录制用户动作流重放做回归测试可行吗
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-266：录制用户动作流重放做回归测试可行吗

**答**:
- 可行但有坑：录制层录真实用户操作（点击/输入/网络响应），回放时要么真跑浏览器（Playwright）要么纯状态层重放（快但只验证逻辑不验证 UI）
- 两个失败模式：环境漂移（回放时接口返回变了/文案变了）→ 录制网络响应做 mock 锁环境；动态数据（时间/id）→ 录制时做参数化占位
- 工程建议：录制回放当「候选测试生成器」——录一次自动转成 Playwright 脚本，人工修补选择器后进回归集，而不是直接把录制当测试跑
- 断言生成：录制时同步记录关键节点状态快照，回放后对比——自动生成断言，降低写用例成本

```javascript
// 录制 → 脚本（示意）
record({ url: '/cart', actions: [
  { type: 'click', selector: '.add-btn' },
  { type: 'fill', selector: '#qty', value: '2' },
  { type: 'assert', snapshot: { cartCount: 2 } },
]})
// 导出 Playwright
test('cart-flow', async ({ page }) => {
  await page.goto('/cart'); await page.click('.add-btn');
  await page.fill('#qty', '2'); await expect(page.locator('.count')).toHaveText('2')
})
```
