---
title: [PER-008] Lighthouse 的评分维度有哪些？如何在 CI 中集成 Lighthouse 做性能回归？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-008：Lighthouse 的评分维度有哪些？如何在 CI 中集成 Lighthouse 做性能回归？

**答**：
- 四大评分维度：Performance、Accessibility、Best Practices、SEO，Performance 下由 FCP/LCP/TBT/CLS/Speed Index 等加权得出。
- 本地用 `npx lighthouse` 出报告，`--preset=desktop` 模拟桌面环境（默认是移动端）。
- CI 集成用官方 `@lhci/cli`：构建后启动服务，`lhci autorun` 收集并对指标做断言，低于阈值直接失败。
- 注意实验室数据（Lighthouse）与真实用户数据（RUM/ web-vitals 上报）要分开看，优化决策以 RUM 为准。

```bash
# 本地生成完整报告：性能、可访问性、最佳实践、SEO 四大评分
npx lighthouse https://example.com --preset=desktop --view

# 只输出 JSON，供监控平台二次加工
npx lighthouse https://example.com --output=json --output-path=./report.json

# CI 集成 Lighthouse CI：对构建产物做回归检测
npm i -D @lhci/cli
npx lhci autorun --collect.url=http://localhost:3000
```

## 二、资源加载优化
