---
title: [ENG-217] CI 流水线的分层（快慢道/门禁分级）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-217：CI 分层怎么设计？
**答**：
- 三层流水线：PR 快道（< 10min：lint/typecheck/单元测试/affected 构建）→ 合入门禁（全量测试/集成测试）→ 定时深水（安全扫描/E2E 全量/性能基线）——按反馈价值排序。
- affected 驱动：所有层基于变更影响面裁剪（SCN/ENG-203），无变更不跑。
- 失败优先：并行任务 fail-fast 策略可选（调试期全跑拿到完整报告 vs 门禁期快速失败）。
- 资源分级：PR 快道用高并发小机器，深水用大机器——CI 成本与时长平衡。
- 追问钩子：为什么 E2E 放定时层不放 PR 门禁——E2E 慢且 flaky，放门禁会让 10 分钟快道失效；PR 层用受影响的集成测试保证核心链路，E2E 全量每日兜底。

```yaml
# 三层流水线
pr:
  - lint, typecheck (affected)
  - unit tests (affected)
  - build (affected)            # 目标 < 10min
merge-gate:
  - full unit + integration
  - e2e (affected core-journeys)
nightly:
  - security scan + sbom
  - full e2e + perf baseline    # 深水层
```
