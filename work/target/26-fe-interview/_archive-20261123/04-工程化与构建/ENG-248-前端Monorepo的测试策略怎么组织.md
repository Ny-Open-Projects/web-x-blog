---
title: [ENG-248] Monorepo 的测试策略怎么组织（金字塔在千包仓库的落地）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-248：Monorepo 测试策略怎么组织？
**答**：
- 按包分层：ui 组件包（组件测试+可访问性）、utils 纯逻辑（单测为主）、feature 包（集成测试）、apps（E2E 关键旅程）——测试类型跟随包职责。
- affected 运行：改 A 包只跑 A 及其消费方的测试（SCN-ENG-203），全量留给 nightly。
- 测试基建共享：测试工具库（render helper/mock 工厂/fixture）作为独立包，杜绝每个包自造轮子。
- 覆盖率策略：包级覆盖率目标（核心包 80%、工具包 95%），monorepo 汇总报表按 owner 分发。
- 追问钩子：为什么「测试工具库共享」在 monorepo 特别重要——N 个包各自造 mock/render 辅助，升级测试框架要改 N 处且行为不一致；工具库单源让测试行为全仓一致，框架升级一次 PR。

```javascript
// turbo test 受影响运行
turbo run test --filter=...[origin/main]
// 共享测试工具包
import { renderWithTheme } from '@org/test-utils';   // 单源 helper
// 覆盖率按 owner 分发
coverageReport.byOwner();  // -> ui-team: 82% ✅, feature-team: 71% ⚠️
```
