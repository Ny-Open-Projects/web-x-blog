---
title: [TST-215] 分布式失败后如何高效重跑（只重跑失败分片的失败用例）？
date: 2026-11-20
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-215：分布式失败后如何高效重跑（只重跑失败分片的失败用例）？
**答**：
- Playwright 的 --last-failed 会话级记录，CI 中可用 --grep @failed 标签方案更稳。
- 重跑前先确认失败原因：环境类（服务挂了）重跑无意义，先修环境。
- 重跑结果不覆盖原报告而是合并（保留原始失败证据）。
- 反复重跑成功的用例进入 flaky 名单治理，不能靠重跑掩盖。

```javascript
# 标记失败 → 重跑
npx playwright test --grep @failed --shard=2/4
# 或使用 blob 合并时保留两次运行对比
r
```
