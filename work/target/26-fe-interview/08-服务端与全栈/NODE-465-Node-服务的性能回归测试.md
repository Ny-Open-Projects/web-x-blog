---
title: [NODE-465] Node 服务的性能回归测试（接口耗时基线）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-465：性能回归测试
**答**:
- 定位：CI 中跑"代表性请求集合"的耗时基线对比（P50/P95），新 MR 性能劣化 > 阈值即预警——把"上线后才发现变慢"提前到合并前。
- 测试形态：微基准（纯函数级：序列化/算法——vitest bench，快）、接口基准（起本地 app + stub 下游，压固定 QPS 测延迟分布）、全链路基准（夜间压测环境跑，NODE-373，慢但真实）。
- 基线管理：主道基线（每日更新——排除环境噪音：多轮取中位数）、MR 对比基线（同机同配置）、噪音控制（CPU pinning/预热/数据量固定 NODE-463）。
- 阈值与归因：劣化 > 20% 预警 → 归因辅助（对比 flame 图/SQL 计划 diff——定位到改动点）；资源指标同步采集（内存/CPU/事件循环延迟——延迟没变但内存翻倍也是回归）。
- 产出闭环：性能回归报告附 MR（与功能测试同级看待），关键接口（支付）劣化直接阻断。
```javascript
// vitest bench 微基准
bench('serialize order', () => { JSON.stringify(bigOrder); }, { time: 1000, iterations: 100 });
// CI: bench 结果 vs main 基线 → delta > 20% → warning（core 路径 → fail）
```
