---
title: [TST-400] 自动化测试深水区总览（面试收束答法）。
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-400：自动化测试深水区总览（面试收束答法）。
**答**：
- 扩展六域：分布式执行（分片/隔离/聚合）、视觉 AI（分层判定）、组件库体系（a11y/多主题）、微前端（隔离与契约）、SSR（水合/流式/双端）、数据工厂与契约（结构保证）。
- 贯穿主线：确定性（消除随机性）、可归因（失败分环境/产品/测试）、可演进（根因库/资产老化）。
- 关键判断：测试体系的上限 = 环境与数据的确定性下限。
- 收束答法：先讲体系分层，再讲深水专项，落到度量与演进。

```javascript
const tstDeep = {
  domains: ['distributed', 'visual-AI', 'component-lib', 'micro-fe', 'ssr', 'factory+contract'],
  threads: ['determinism', 'attributability', 'evolvability'],
  law: '测试上限 = 环境与数据的确定性下限',
};
r
```
