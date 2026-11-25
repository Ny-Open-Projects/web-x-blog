---
title: [FRP-356] 跨框架的 E2E 与视觉回归矩阵
date: 2026-11-21
categories: [框架原理]
tags: [前端面试, 面试题, 测试]
type: 面试题
---

## FRP-356：跨框架的 E2E 与视觉回归矩阵

**答**：
- 矩阵维度：框架壳（React/Vue）× 主题（light/dark）× 视口（三断点）× 状态（空/加载/错误/正常）——矩阵爆炸治理：核心路径全矩阵，长尾抽样
- 选择器策略：跨框架 E2E 用「语义选择器」（data-testid/role）——不依赖框架 class（scoped hash 不同）
- 视觉回归的基线管理：按「框架 × 主题 × 视口」三维目录——基线更新走 PR review（截图 diff 即设计变更）
- 行为断言的一致性：跨框架同一交互的断言脚本复用（Playwright page object 抽象）——「写一次测两框架」的前提是接口一致
- CI 组织：壳层测试并行跑（React 任务/Vue 任务）——矩阵的执行时间控制

```javascript
// 跨框架 Page Object (接口一致)
class CartPage {
  constructor(page) { this.page = page; }
  addItem(sku) { return this.page.getByTestId(`add-${sku}`).click(); }
  async assertTotal(n) { await expect(this.page.getByTestId('total')).toHaveText(`¥${n}`); }
}
// 两个框架的应用共用同一 PO — 行为断言写一次
// 视觉基线: cart/{react,vue}/{light,dark}/{sm,md,lg}.png
```
