---
title: [XP-370] 跨端 app 内嵌 H5 与原生的职责划分
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-370：跨端 app 内嵌 H5 与原生的职责划分

**答**：
- 原则：性能敏感（列表滚动/动画）原生，内容展示/快速迭代 H5。
- 判定：页面性能预算（滚动帧率）达不到 H5 标准时下沉原生。
- 桥能力：H5 页面需要的原生能力（支付/分享/定位）统一 bridge 白名单。

```javascript
// 职责判定
function pageTech(page) {
  const score = page.animComplexity * 2 + page.listSize / 100
    - page.iterationSpeed;
  return score > 3 ? { tech: 'native', note: '性能敏感下沉原生' }
    : { tech: 'h5', note: '迭代速度优先' };
}
```
