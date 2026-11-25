---
title: [TST-237] 视觉测试在测试金字塔中的位置与投入比例建议？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-237：视觉测试在测试金字塔中的位置与投入比例建议？
**答**：
- 底层：样式 token/设计系统单测（快、稳定）——覆盖 80% 样式一致性。
- 中层：组件级视觉 diff（Storybook）——组件外观回归主防线。
- 顶层：整页快照 + AI 布局检测——低频兜底。
- 投入比例参考：底层 50% / 组件 35% / 整页 15%，比例失调（整页为主）是维护泥潭的开始。

```javascript
const pyramid = {
  bottom: 'token 单测（jest 断言 token 映射）50%',
  middle: 'Storybook 视觉 diff 35%',
  top: '整页快照 + AI 布局检测 15%',
};
r
```
