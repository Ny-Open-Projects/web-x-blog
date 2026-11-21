---
title: [WCN-118] WCN 的可访问性如何跨框架保证？a11y 审计自动化与影子树的可访问性怎么测？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 跨框架复用]
type: 面试题
---

## WCN-118：WCN 的可访问性如何跨框架保证？影子树的 a11y 怎么测？

**答**：
- 语义内聚原则：role/aria 状态属于组件（影子树内），文案属于使用方（slot/attribute 传入）；组件用 ElementInternals 设默认 role，允许宿主覆盖。
- 影子树的 a11y 难点：axe-core 等工具对 open shadow 支持良好（`axe.run({ includeShadows: true })`）；closed shadow 审计需测试钩子。
- 自动化：Playwright + @axe-core/playwright，全组件矩阵扫描（键盘遍历顺序、对比度、aria 属性完整性）；CI 门禁零 critical。
- 键盘测试：Tab 顺序跨影子边界（delegatesFocus 影响）、Escape 关闭、方向键导航——用 page.keyboard 系列断言 document.activeElement。
- 屏幕阅读器验证：shadow 边界对 SR 透明（可访问性树不隔离），但 aria-labelledby 跨边界 id 引用无效——引用节点必须同在影子树内。

```javascript
// Playwright + axe 审计示例
import AxeBuilder from '@axe-core/playwright';

test('x-dialog 无 a11y critical 违规', async ({ page }) => {
  await page.goto('/docs/dialog');
  await page.keyboard.press('Tab');           // 焦点进入组件
  const results = await new AxeBuilder({ page })
    .include('x-dialog')                      // 审计范围限定组件
    .withRules(['aria-roles', 'color-contrast', 'keyboard'])
    .analyze();
  expect(results.violations.filter((v) => v.impact === 'critical')).toEqual([]);
});
// 键盘遍历断言
await page.keyboard.press('Escape');
await expect(page.locator('x-dialog')).not.toHaveAttribute('open');
```
