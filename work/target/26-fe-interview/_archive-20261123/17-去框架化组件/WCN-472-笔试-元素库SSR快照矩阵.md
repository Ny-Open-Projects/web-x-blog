---
title: [WCN-472] 笔试：实现 SSR 快照矩阵（元素 × props 场景 × 主题）。
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-472：笔试：实现 SSR 快照矩阵（元素 × props 场景 × 主题）。
**题目**：生成矩阵用例：每元素 × 场景集（空/典型/极值/错误态）× 主题（light/dark）→ renderDSD 快照；断言「主题间 diff 只在颜色类 token」。

```javascript
const SCENES = { empty: {}, typical: { sku: 'A1', title: '商品' },
  extreme: { title: 'x'.repeat(500) }, error: { bad: true } };
function ssrMatrix(tags, themes = ['light', 'dark']) {
  return tags.flatMap(t => Object.keys(SCENES).flatMap(s =>
    themes.map(th => ({ case: `${t}-${s}-${th}`,
      run: () => renderDSD({ ...SCENES[s], theme: th }) }))));
}
// 断言：light/dark diff 中非颜色字段为空

```

**评分点**：
- 矩阵生成（笛卡尔积）。
- 场景集标准化（四态）。
- 主题 diff 语义（只允许 token 值差异）。
- 快照命名规范（tag-scene-theme）。
