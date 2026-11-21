---
title: [XP-106] 跨端 UI 一致性测试怎么做？多端视觉回归矩阵如何搭建？
date: 2026-11-17
categories: [跨端]
tags: [前端面试, 面试题, 27]
type: 面试题
---

## XP-106：跨端 UI 一致性测试怎么做？多端视觉回归矩阵如何搭建？
**答**：
- 目标分层：**组件级**（设计系统还原度）与**页面级**（关键链路截图），一致性验收标准来自 Design Token（尺寸/色板/字体梯度），Token 不一致先修 Token 再谈截图。
- 多端截图采集：Web/H5 用 Playwright 截图；RN 用 iOS/Android 模拟器截图（detox/maclib）；Flutter 用 `goldenFileTest`（无需模拟器）；小程序走真机截图自动化。**基线图统一按组件名+状态命名入库**。
- 对比与阈值：像素 diff（pixelmatch）+ 感知 diff（SSIM）双指标，容忍阈值按组件分级（文本组件 5%、图形组件 1%）；字体渲染差异（平台 hinting）在阈值或渲染层归一化处理。
- CI 矩阵：PR 触发多端多机型矩阵（与 XP-136 CI 体系复用），diff 报告生成 HTML 页挂 PR comment；基线更新需设计/平台双审。
- 治理节奏：核心组件库每次发版跑全量矩阵，业务页面按改动面跑增量；新增截图即"快照冻结"，变更必须显式接受（与 XP-072 兼容性测试衔接）。

```yaml
# .github/workflows/visual-regression.yml —— 多端视觉回归矩阵
name: visual-regression
on: [pull_request]
jobs:
  matrix:
    strategy:
      fail-fast: false
      matrix:
        include:
          - { target: web,        os: ubuntu-latest,  cmd: "npx playwright test --update-snapshots=false" }
          - { target: rn-ios,     os: macos-14,       cmd: "detox build && detox test -c ios.sim.release" }
          - { target: rn-android, os: ubuntu-latest,  cmd: "detox build && detox test -c android.emu.release" }
          - { target: flutter,    os: ubuntu-latest,  cmd: "flutter test --update-goldens=false test/goldens" }
          - { target: miniprogram,os: ubuntu-latest,  cmd: "miniprogram-automator screenshot-suite" }
    runs-on: ${{ matrix.os }}
    steps:
      - uses: actions/checkout@v4
      - run: ${{ matrix.cmd }}
      - uses: actions/upload-artifact@v4         # 采集图统一命名 组件名_状态_端_机型
        with: { name: shots-${{ matrix.target }}, path: screenshots/ }
  compare:                                        # 产物齐全后统一 diff
    needs: matrix
    runs-on: ubuntu-latest
    steps:
      - uses: actions/download-artifact@v4
      - run: node tools/visual-diff.js --threshold-web 5 --threshold-graphic 1
        # pixelmatch + SSIM 双指标；diff 报告 HTML 作为 PR comment，基线更新需双审
```
