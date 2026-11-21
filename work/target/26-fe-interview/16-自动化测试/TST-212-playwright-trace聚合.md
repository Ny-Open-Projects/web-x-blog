---
title: [TST-212] trace（执行轨迹）在分布式下的存储与查看实践？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-212：trace（执行轨迹）在分布式下的存储与查看实践？
**答**：
- trace: 'retain-on-failure' 只留失败轨迹，控制存储量。
- trace 文件随 artifact 上传，用 trace viewer 本地打开（npx playwright show-trace）。
- trace 命名含 shard/worker/用例 id，避免覆盖与难定位。
- 聚合平台（如 ReportPortal/自建）把 trace 链接到报告条目，一键回放。

```javascript
export default defineConfig({
  use: { trace: 'retain-on-failure', video: 'retain-on-failure',
         screenshot: 'only-on-failure' },
});
// artifact 命名：trace-{shard}-{worker}-{testId}.zip
r
```
