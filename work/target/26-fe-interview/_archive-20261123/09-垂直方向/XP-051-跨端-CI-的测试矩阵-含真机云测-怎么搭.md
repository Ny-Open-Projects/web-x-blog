---
title: [XP-051] 跨端 CI 的测试矩阵（含真机云测）怎么搭？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-051：跨端 CI 的测试矩阵（含真机云测）怎么搭？
**答**：
- 测试金字塔按端组合：**单元测试**（core/hooks 全端跑同一份 jest）→ **契约测试**（adapter 各端实现跑同一用例矩阵）→ **E2E**（H5 Playwright、小程序 automator、RN Detox/Maestro）→ **真机云测**（Testin/Firebase Test Lab/自建设备农场，覆盖机型碎片化）。
- 矩阵维度：端 × OS 版本 × 机型档位（旗舰/中端/低端）× 网络（弱网模拟），高频组合进流水线，长尾组合夜间跑。
- 质量门禁：核心链路 E2E 通过率 100%、崩溃率阈值、启动时长基线对比；不达标禁止发布。
- 设备管理：云测接入 CI（API 提交任务+轮询报告），失败自动归档录屏/日志，联动告警。

```yaml
# .github/workflows/cross-test.yml —— 测试矩阵 + 真机云测接入
jobs:
  unit:
    runs-on: ubuntu-latest
    steps:
      - run: pnpm turbo run test --filter=packages/core --filter=packages/hooks   # 全端共用
  contract:
    strategy:
      matrix: { adapter: [h5, weapp, rn] }
    runs-on: ubuntu-latest
    steps:
      - run: pnpm --filter @app/adapter-${{ matrix.adapter }} test:contract       # 同一用例矩阵
  e2e:
    strategy:
      matrix:
        include:
          - { suite: h5,    run: playwright test }
          - { suite: weapp, run: miniprogram-automator scripts/e2e-weapp.js }
          - { suite: rn,    run: maestro test .maestro/ }                      # RN UI 测试
    runs-on: ubuntu-latest
    steps: [ uses: actions/checkout@v4, run: ${{ matrix.run }} ]
  cloud-devices:                # 真机云测：夜间全量，发布前跑核心机型
    if: github.event_name == 'schedule'
    runs-on: ubuntu-latest
    steps:
      - run: node scripts/cloudtest-submit.js --devices=flagship,mid,lowend --os="iOS17,iOS15,Android13,Android11"
      - run: node scripts/cloudtest-wait.js --timeout=1800
      - run: node scripts/cloudtest-gate.js --crash<0.1 --pass>99.5             # 门禁
```
