---
title: [V3-367] 嵌套 Suspense 的 resolve 顺序如何验证？
date: 2026-11-19
categories: [Vue3]
tags: [前端面试, 面试题, 06]
type: 面试题
---

## V3-367：嵌套 Suspense 的 resolve 顺序如何验证？
**答**：
- 规则：内层边界 resolve 不代表外层 resolve；外层等所有**直接**异步依赖，内层边界的内容在外层渲染后才开始处理。
- 验证手段：在各异步依赖里打日志（start/resolve 时间戳），或用测试断言 fallback 的出现顺序。
- 常见误解：「内层数据完成得早，外层就能提前完成」——错，外层只看自己的异步依赖集合。
- 时序可视化：DevTools Performance 面板过滤组件渲染事件，或自己封装 `<SuspenseDebug>` 边界组件在 onPending/onResolve 打点。
- 工程价值：解释「为什么骨架屏比预期久」——通常是外层依赖里混入了慢接口，按依赖清单拆分层。
