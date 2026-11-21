---
title: [RBL-297] Rspack 懒编译（lazyCompilation）实践与边界
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-297：Rspack 懒编译实践与边界

**答**:
- 原理：dev 下不预编译全部模块，动态 import 的模块在「首次请求」时才触发编译——巨型应用（几千页面）冷启动从分钟级到秒级
- 配置：`experiments.lazyCompilation: true` 或细粒度（仅对动态 import 生效）；访问延迟转移到首次导航（首屏快、点击路由慢一点）
- 边界：不适合做「全量预检查」的场景（类型检查要另跑）；缓存预热策略配合（idle 时后台预编译高频路由，平衡首屏与导航）
- 判定：冷启动 > 60s 且路由访问集中度低（用户散点访问）→ 懒编译收益最大

```javascript
experiments: {
  lazyCompilation: {
    entries: false,          // 入口仍全量
    imports: true,           // 动态 import 懒编译
  },
}
// 配套：idle 后台预热高频路由（行为统计驱动）
```
