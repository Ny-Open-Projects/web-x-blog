---
title: [H5-178] axe-core 如何集成到开发流与 CI？
date: 2026-11-17
categories: [HTML5]
tags: [前端面试, 面试题, 02]
type: 面试题
---

## H5-178：axe-core 如何集成到开发流与 CI？
**答**：
- 运行时：`axe.run(document)` 返回 violations 数组，每条带 rule id/impact/WCAG 标签/失败节点选择器/修复文档链接。
- CI：Playwright + `@axe-core/playwright` 对每个页面扫描，`wcag2a/2aa` 级别 + serious/critical 失败阻断合入。
- 局部扫描：`include('.modal')`/`exclude()` 缩小范围降噪；已知误报 `disableRules` 白名单但要写明理由。
- 边界：规则覆盖约 30~40%（静态可判定项），焦点管理/读屏体验仍需人工（H5-176）。

```javascript
// CI 集成：Playwright + axe-core，构建失败 = 有严重无障碍违规
// npm i -D @playwright/test @axe-core/playwright
const { test, expect } = require('@playwright/test');
const AxeBuilder = require('@axe-core/playwright').default;

test('首页无严重无障碍问题', async ({ page }) => {
  await page.goto('https://example.com');
  const results = await new AxeBuilder({ page })
    .withTags(['wcag2a', 'wcag2aa', 'wcag21a', 'wcag21aa'])  // 按合规等级过滤
    // .disableRules(['color-contrast'])  // 已知误报白名单，需注明理由
    .analyze();

  const blocking = results.violations.filter(
    (v) => v.impact === 'critical' || v.impact === 'serious');
  // 每条违规自带：规则 id、影响级别、WCAG 标签、失败节点选择器、修复文档
  expect(blocking, JSON.stringify(blocking.map((v) => ({
    id: v.id, impact: v.impact, nodes: v.nodes.map((n) => n.target),
  })), null, 2)).toEqual([]);
});

// 开发期快捷用法：控制台引入 axe 即扫
async function quickAudit() {
  const axe = (await import('https://cdn.skypack.dev/axe-core')).default;
  const r = await axe.run(document, { resultTypes: ['violations'] });
  for (const v of r.violations) {
    console.warn(`[${v.impact}] ${v.help} -> ${v.nodes[0].target}`);
  }
}
// 工程要点：
// 1) 规则覆盖约 30~40%（静态可判定项），焦点管理/读屏体验必须人工走查
// 2) 局部组件扫描 AxeBuilder.include('.modal')，避免整页噪音
// 3) 分级处理：critical/serious 阻断合入，moderate 开 issue 跟踪
```

## 三十、综合案例
