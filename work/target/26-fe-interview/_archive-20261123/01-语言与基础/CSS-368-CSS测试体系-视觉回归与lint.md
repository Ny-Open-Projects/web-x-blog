---
title: [CSS-368] CSS 测试体系：视觉回归、lint 与规则测试
date: 2026-11-21
categories: [CSS]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## CSS-368：CSS 测试体系：视觉回归、lint 与规则测试

**答**：
- 视觉回归（核心）：Playwright 截图对比（全页 + 组件快照）+ 差异高亮报告；关键在「稳定化」——动画冻结（CSS injection 停 animation）、字体/时区固定、内容 mock、容差阈值
- stylelint 静态检查：禁用模式（!important 滥用/深嵌套/物理方向属性混用/硬编码色值不入 token）、命名规范（BEM 语法）——lint 进 CI 门禁
- 组件规则测试：Storybook + interaction test（hover 后截图断言）、@media/主题变量矩阵测试（light/dark × 断点出快照矩阵）
- 基线管理：基线图入库（随 PR 更新走 review——图 diff 就是设计变更评审）；大规模重构用「页面级像素 diff 报告」人工抽验
- 真机抽样：自动截图是单环境，关键页面每版本真机走查（字体渲染差异自动测不出来）

```js
// playwright 视觉回归
test('card dark mode', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'dark', reducedMotion: 'reduce' });
  await page.addStyleTag({ content: '*,*::before{animation:none!important;transition:none!important}' });
  await page.goto('/components/card');
  expect(await page.screenshot({ clip })).toMatchSnapshot('card-dark.png', { maxDiffPixelRatio: 0.01 });
});
```
