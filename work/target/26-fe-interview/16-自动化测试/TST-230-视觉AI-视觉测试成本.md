---
title: [TST-230] 视觉回归的存储与算力成本如何控制？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-230：视觉回归的存储与算力成本如何控制？
**答**：
- 基线压缩：PNG → 有损但视觉无损（pngquant），基线库可减 60%+。
- 只对变更组件重测（受影响子集），而非全量基线重放。
- 基线去重：同组件多视口差异小于阈值时合并断言。
- 冷热分层：热基线（本周更新过）本地缓存，冷基线按需拉取。

```javascript
# 基线压缩（视觉无损）
pngquant --quality=80-98 --ext .png --force __screenshots__/*.png
# CI 中只重测受影响组件
npx playwright test --grep @scope:cart
r
```
