---
title: [OPT-119] Core Web Vitals 从"全红"到"全绿"的推进路线图怎么排？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-119：Core Web Vitals 从"全红"到"全绿"的推进路线图怎么排？

**答**：
- 排序原则：**先测量后优化**（没有分维度基线全是瞎打）、按"对总分拖累 × 修复成本"排优先级、每步只动一个变量并验证 RUM。
- 标准六阶段：基线体检（CrUX+RUM+Lab 三源对齐）→ LCP 治理（资源/直出）→ CLS 治理（占位/尺寸锁定，通常最容易全绿）→ INP 治理（长任务切片/第三方瘦身，最难）→ 回归卡口（CI+预算）→ 持续运营（看板+告警）。
- 阶段验收都用同一口径：**CrUX/RUM 的 P75 达标**（LCP<2.5s、INP<200ms、CLS<0.1），Lab 数据只做过程参考。
- 常见坑：只顾 LCP 把 CLS 治恶化（异步插内容没占位）；用均值汇报掩盖 P75 未达标。

```yaml
# 一一对应：CWV 全绿路线图（可落地的里程碑 + 验收 YAML，进仓库当 checklist）
# cwv-roadmap.yaml —— 每阶段有 owner/动作/验收口径
milestones:
  - phase: 1-基线体检            # 第 1 周
    actions:
      - 拉 CrUX P75 与 RUM 分维度数据，定位最差指标与最差人群（机型x网络）
      - Lighthouse CI 建立实验室基线，锁定当前版本号
    exit_criteria: { output: 三源数据报告，明确主攻指标 } # 例：LCP 4.2s INP 380ms CLS 0.32

  - phase: 2-CLS治理             # 第 2 周（成本最低，先摘果子）
    actions:
      - 全图片补 width/height 或 aspect-ratio
      - 动态插入区块预占位；字体 fallback 度量对齐（见 OPT-072）
    exit_criteria: { rum_p75_cls: "<0.1" }

  - phase: 3-LCP治理             # 第 3-4 周
    actions:
      - LCP 元素标 fetchpriority=high，非关键资源压 low（见 OPT-050）
      - 首屏接口 SSR/直出 + HTML 边缘缓存（见 OPT-118）
      - 文本资源全量 Brotli + 强缓存 hash（见 OPT-052）
    exit_criteria: { rum_p75_lcp: "<2.5s" }

  - phase: 4-INP治理             # 第 5-6 周（最难，长任务+第三方）
    actions:
      - 长任务切片改造（见 OPT-057），INP 回溯归因到具体交互
      - 第三方脚本 facade 化/延后（见 OPT-018），交互路径同步脚本清零
      - 输入回调瘦身，重计算进 Worker（见 OPT-102 决策树）
    exit_criteria: { rum_p75_inp: "<200ms" }

  - phase: 5-回归卡口            # 持续
    actions:
      - Lighthouse CI + size-limit 进流水线（见 OPT-040）
      - RUM 告警阈值：P75 劣化 10% 自动告警
    exit_criteria: { ci: lighthouse-score-min-90 }

  - phase: 6-持续运营            # 永远
    actions:
      - 月度性能周报（CrUX 趋势 + Top 劣化页面）
      - 新功能上线前性能评审（预算申请制）
    exit_criteria: { output: 指标连续两季度达标 }
```
