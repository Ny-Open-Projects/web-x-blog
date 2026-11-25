---
title: [XP-339] 跨端 CI：多端构建与测试流水线
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-339：跨端 CI：多端构建与测试流水线

**答**：
- 流水线：lint -> 单测 -> 多端构建（web/rn/mini 并行）-> 视觉回归 -> 包体门禁 -> 灰度发布。
- 加速：缓存依赖/构建产物、并行端构建、增量构建（变更文件触发）。
- 时长目标：全流水线 < 15 分钟（超过则并行/缓存优化）。

```javascript
// CI 编排
async function ciPipeline(changed) {
  const stages = [
    { name: 'lint', run: lint, when: () => true },
    { name: 'test', run: unitTest, when: () => true },
    { name: 'build-web', run: buildWeb, when: () => changed.some(isWeb) },
    { name: 'build-rn', run: buildRN, when: () => changed.some(isRN) },
    { name: 'visual', run: visualRegression, when: () => true },
    { name: 'budget', run: bundleGate, when: () => true },
  ];
  const active = stages.filter(s => s.when());
  return Promise.all(active.map(s => s.run()));      // 并行执行
}
```
