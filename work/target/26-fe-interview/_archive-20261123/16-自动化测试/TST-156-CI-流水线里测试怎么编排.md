---
title: [TST-156] CI 流水线里测试怎么编排？各层测试在什么时机跑？
date: 2026-11-17
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-156：CI 流水线里测试怎么编排？各层测试在什么时机跑？
**答**：
- 分层编排原则：越快的越靠前、越容易挂的越靠后。PR 阶段：lint/typecheck → 单测（分钟内）→ 增量覆盖率门禁 → 构建产物检查；合并后（每夜/每次部署前）：组件测试全集 → E2E 冒烟；每日定时：E2E 全集 + 视觉回归 + 变异测试 + Lighthouse。
- PR 门禁只放「必过且快」的：单测 + 类型 + 冒烟 E2E（5 分钟内），全集不进 PR 否则反馈周期毁掉开发体验。失败反馈要闭环：PR 评论 + 群告警 + 失败截图/trace 链接。
- 缓存与加速：node_modules/Playwright 浏览器二进制缓存、vitest 并行 worker、E2E 分片、受影响测试选择器（改哪跑哪，见 TST-126）。
- flaky 处置通道：PR 里挂了先重试一次（retries），重试仍挂才阻断；每日任务里统计重试率产出 flaky 榜单，隔离修复。
- 追问钩子：怎么处理「合并后才发现 E2E 挂」？——主干保护：E2E 冒烟也进 merge queue（合入前跑），或主干挂了禁止部署直到修复。

```yaml
# .github/workflows/ci.yml 关键编排
jobs:
  unit:          # PR 必过：单测 + 覆盖率增量门禁（~2min）
    steps: [checkout, cache-node-modules, { run: 'npm ci' },
            { run: 'npm run test:unit -- --coverage' },
            { run: 'node scripts/diff-coverage.mjs' }]
  e2e-smoke:     # PR 必过：冒烟链路，2 分片（~5min）
    needs: unit
    strategy: { matrix: { shard: [1, 2] } }
    steps: [{ run: 'npx playwright test --grep @smoke --shard=${{ matrix.shard }}/2' }]
  e2e-full:      # 每夜：全集 + 视觉回归 + flaky 报告
    if: github.event_name == 'schedule'
    steps: [{ run: 'npx playwright test' },
            { run: 'node scripts/flaky-report.mjs' }]
```
