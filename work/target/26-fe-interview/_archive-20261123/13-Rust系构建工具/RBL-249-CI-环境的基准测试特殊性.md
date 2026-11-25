---
title: [RBL-249] CI 环境跑基准测试有什么特殊性
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-249：CI 环境跑基准测试有什么特殊性

**答**:
- CI 机器虚拟化：CPU 计时与磁盘 IO 噪声大（共享宿主），绝对值不可信——CI 适合跑「相对对比」（同 runner 上 A/B 同时跑）与回归检测（趋势），不适合发布绝对性能数字
- 噪声控制：同 PR 内 A/B 交替跑、选独占 runner（自托管/专用机型）、warm-up 轮丢弃
- 回归检测策略：不设绝对阈值，用「相对基线百分比」（P95 超过基线 +15% 阻断），基线定期重校准（防基线腐化）
- 报告分层：CI 报趋势（周维度趋势图），本地标准机报绝对值——两种数据源不要混用

```yaml
# GitHub Actions 基准 job
benchmark:
  runs-on: [self-hosted, perf-dedicated]    # 独占 runner
  steps:
    - run: ./bench.sh --ab-alternate --n 10 --base main
    - run: ./check-regression.sh --threshold 15%   # 相对基线
```
