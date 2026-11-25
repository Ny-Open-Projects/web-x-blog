---
title: [XP-072] 跨端 UI 还原度保障与兼容性测试策略？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-072：跨端 UI 还原度保障与兼容性测试策略？
**答**：
- 还原度量化：**多端截图 diff**——设计稿标注导出 token，组件库每组件建截图基线（H5/RN/小程序三端 × 亮暗色 × 关键断言尺寸），CI 跑视觉回归（pixelmatch/自研，阈值如 0.5% 差异告警）。
- 布局断言：不只像素，还要**关键几何断言**（元素位置/尺寸/层级），对截图噪声（字体渲染差异）更鲁棒。
- 兼容性测试策略：机型矩阵（旗舰/中端/低端 × OS 版本，XP-051 云测执行）、内核矩阵（X5/系统 WebView/各厂商）、暗色模式/大字号/RTL/横竖屏组合。
- 流程机制：视觉走查自动化前置（CI 拦截）+ 发布前人工抽查少量高频页 + 线上"还原度反馈"入口（设计师一键报差）。
- 度量：还原度得分 = 截图通过率 + 几何断言通过率，按组件/页面聚合进看板（XP-069 同构）。

```yaml
# .github/workflows/visual-regression.yml —— 多端截图基线与几何断言
jobs:
  snapshot:
    strategy:
      matrix:
        end: [h5, weapp, rn]
    runs-on: ubuntu-latest
    steps:
      - run: pnpm install --frozen-lockfile
      - run: pnpm turbo run storybook:build --filter=@app/ui          # 组件库 stories
      - run: pnpm --filter @app/ui-${{ matrix.end }} screenshot       # 截图：三端统一用例集
      - run: node scripts/geometry-assert.mjs --end=${{ matrix.end }} # 几何断言：位置/尺寸/层级
      - run: node scripts/pixel-diff.mjs --threshold=0.005            # 与基线 diff，>0.5% 差异 fail
      - uses: actions/upload-artifact@v4
        with: { name: diff-${{ matrix.end }}, path: .diffs/ }         # 失败图归档，PR 评论可视化
  compatibility:                # 兼容矩阵：夜间 + 发布前
    strategy:
      matrix:
        device: [ { model: pixel8, os: android14, tier: flagship },
                  { model: redmi9,  os: android10, tier: lowend },
                  { model: iphone11, os: ios16, tier: mid } ]
    runs-on: ubuntu-latest
    steps:
      - run: node scripts/cloudtest-visual.js --device=${{ toJson(matrix.device) }}
      - run: node scripts/darkmode-fontscale-check.js   # 暗色/大字号/RTL 组合断言
```
