---
title: [WCN-297] 元素库的 CI 流水线（比普通库多了什么）？
date: 2026-11-20
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-297：元素库的 CI 流水线（比普通库多了什么）？
**答**：
- 多浏览器矩阵测试（行为/视觉/a11y 三类）+ DSD SSR 渲染验证（node 环境）。
- bundle 审计：单元素 chunk 大小上限 + 共享依赖盘点。
- token 消费审计：shadow 内裸值扫描（硬编码颜色/间距）。
- 文档构建：demo 测试全绿才发版（文档=测试）。

```javascript
# 元素库 CI 关键 job
jobs:
  matrix: [chromium, webkit, firefox]   # 行为+视觉+a11y
  ssr: node render-dsd-snapshot        # DSD 快照
  audit: token-bare-value-scan         # 裸值扫描
  docs: build-docs-and-test-demos      # demo 即测试
r
```
