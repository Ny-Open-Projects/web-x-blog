---
title: [WCN-154] 去框架化组件的 CI 流水线设计：从提交到 CDN 发布要过哪些闸口？
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 面试题, 选型与工程落地]
type: 面试题
---

## WCN-154：去框架化组件的 CI 流水线设计：从提交到 CDN 发布要过哪些闸口？

**答**：
- 闸口一（提交级）：类型检查 + lint（tag 前缀/事件命名规范）+ 单测（Vitest，逻辑与事件语义）。
- 闸口二（PR 级）：构建产物 + 体积预算 + manifest diff（breaking 检测）+ 双宿主冒烟（React/Vue demo）+ a11y（axe 零 critical）+ 视觉回归（主题矩阵截图）。
- 闸口三（合入级）：changesets 版本号 + changelog（manifest 变化必须说明）+ E2E（Playwright 跨宿主一致性）。
- 闸口四（发布级）：CDN staged 上传 → SRI 校验 → importmap 试切 → 金丝雀观察（错误率/加载耗时看板）→ 全量；失败自动回滚 importmap。
- 效率配套：Turborepo 远程缓存、受影响包检测（--filter=...[origin/main]）、并行测试分片。

```yaml
# .github/workflows/release.yml 关键步骤（简化）
jobs:
  gate:
    steps:
      - run: pnpm turbo build test --filter=...[origin/main]
      - run: pnpm run check:size-budget        # 体积预算
      - run: pnpm run check:manifest-diff      # breaking 检测
      - run: pnpm run test:e2e:all-hosts       # React/Vue/native 宿主一致性
  release:
    needs: gate
    steps:
      - run: pnpm changeset publish && pnpm run cdn:staged
      - run: pnpm run canary:observe --duration=30m   # 看板观察，异常自动回滚
```
