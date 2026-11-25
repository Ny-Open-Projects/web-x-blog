---
title: [VIZ-316] 手写 WebGL→WebGPU 渐进迁移方案（笔试）
date: 2026-11-21
categories: [数据可视化]
tags: [前端面试, 笔试题, 25]
type: 笔试题
---

## VIZ-316：手写 WebGL→WebGPU 渐进迁移方案（笔试）

**答**：
- 题目：存量 WebGL 图表库渐进迁移 WebGPU——迁移评估清单 + 适配层 + 灰度路径。
- 思路：评估：着色器数量（WGSL 重写工作量）、特性依赖（transform feedback 等 WebGPU 缺失项）、兼容率；适配层：IRenderer 双后端（VIZ-261）；灰度：flag + 双跑（VIZ-260）。
- 评分点：评估维度；适配层复用；灰度与回退。

```javascript
const migrationPlan = {
  assess: {
    shaders: 'WGSL 重写工作量（语法差异：attribute→@builtin，uniform→uniform struct）',
    missingFeatures: ['transform feedback → compute pass 替代', 'textureLod 差异'],
    compatRate: 'WebGPU 支持率（2026 约 85%）→ 必须保留 WebGL 后端',
  },
  adapter: 'IRenderer 双后端（ALG/VIZ-261）——业务零感知切换',
  rollout: [
    '阶段 1：内部白名单 flag 试跑',
    '阶段 2：双跑对比（VIZ-260）通过后 5% 灰度',
    '阶段 3：性能劣化/渲染错误哨兵（HW-846）自动回退',
    '阶段 4：兼容率达标后 WebGL 转维护模式',
  ],
  rollback: 'flag 关闭即回 WebGL——引擎选择运行时判断（VIZ-207）',
};
```
