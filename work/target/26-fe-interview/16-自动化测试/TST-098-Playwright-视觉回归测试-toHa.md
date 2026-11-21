---
title: [TST-098] Playwright 的视觉回归测试怎么做？截图对比怎么防误报？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-098：Playwright 的视觉回归测试怎么做？截图对比怎么防误报？
**答**：
- 基本用法：`expect(page).toHaveScreenshot()` / `expect(locator).toHaveScreenshot()`，首次运行生成 baseline 快照存 `*-snapshots/` 目录，之后运行做像素 diff，不一致即失败；`--update-snapshots` 更新基线，CI 上用 HTML 报告看 diff 图（红框高亮差异）。
- 防误报三板斧：① `maxDiffPixelRatio` / `threshold` 放宽像素级敏感度；② `mask: [locator]` 遮住动态区域（头像、时间戳、轮播图、广告位）；③ `animations: 'disabled'` + `caret: 'hide'` 固定动画与光标——动画中途截图是视觉回归误报第一大来源。
- 环境一致性：跨平台字体渲染差异会导致基线不可比，用 Docker 镜像跑（官方 `mcr.microsoft.com/playwright`），或者 `snapshotPathTemplate` 按平台分目录；CI 与本地必须同环境。
- 最佳实践：只截组件/区域不截整页（缩小 diff 面）；基线变更必须进 code review（截图文件本身也是代码）；配合 Storybook 每个组件状态截一张。
- 追问钩子：什么时候值得做视觉回归？——设计系统组件库、营销页、强视觉业务；普通后台 CRUD 页性价比低，改用结构断言。

```javascript
test('视觉回归：卡片组件截图对比', async ({ page }) => {
  await page.goto('/design/goods-card');
  await page.getByTestId('card-normal').waitFor(); // 等渲染稳定

  await expect(page.getByTestId('card-normal')).toHaveScreenshot('goods-card.png', {
    animations: 'disabled',            // 冻结 CSS 动画
    caret: 'hide',                     // 隐藏输入光标
    maxDiffPixelRatio: 0.02,           // 允许 2% 像素差异
    mask: [page.getByTestId('avatar'), page.getByTestId('price-flash')], // 遮动态区
  });
});
```
