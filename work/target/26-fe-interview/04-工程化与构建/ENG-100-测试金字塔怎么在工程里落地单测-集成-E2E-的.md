---
title: [ENG-100] 测试金字塔怎么在工程里落地？单测、集成、E2E 的比例与门禁怎么定？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-100：测试金字塔怎么在工程里落地？单测、集成、E2E 的比例与门禁怎么定？
**答**：
- 比例参考 70/20/10：单元测试打底、少量集成测试、极少量关键路径 E2E，越往上越慢越脆。
- 门禁分层：PR 卡口只挂单测与类型检查（秒级~分钟级）；E2E 放在合入 main 后异步跑，不阻塞开发者。
- 集成测试（组件级/模块级）补单测与 E2E 之间的断层，用 Vitest + Testing Library + MSW 承载。
- 反模式：金字塔倒置（E2E 占大头）导致流水线慢、flaky 噪音大、失败定位难。

```yaml
# CI 分层执行：PR 只跑单测，E2E 在 main 上异步跑
jobs:
  unit:
    if: github.event_name == 'pull_request' || github.ref == 'refs/heads/main'
    steps:
      - run: pnpm vitest run --coverage

  e2e:
    if: github.ref == 'refs/heads/main'   # 只在主干跑，不阻塞 PR
    needs: unit
    steps:
      - run: pnpm playwright install --with-deps
      - run: pnpm playwright test
```
