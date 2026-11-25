---
title: [OPT-187] 性能门禁如何从"人工审查"演进到"CI 自动阻塞"？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-187：性能门禁如何从"人工审查"演进到"CI 自动阻塞"？

**答**：
- 三阶段演进：①人工阶段——性能评审表 + 代码 review 关注点（能跑但靠自觉）；②半自动——CI 出报告不阻塞（size-limit 超限只评论），团队适应期；③全自动——超预算阻塞合并，RUM 线上劣化自动告警回滚。
- 演进节奏建议：半自动运行 ≥ 1 个月、误报率 < 10% 后再收紧为阻塞，避免门禁一开始就招抵制被绕过（加 skip 标签之类的后门）。
- 门禁项分层：确定性强的用硬卡口（bundle 超预算、Lighthouse 低于分）；波动大的用软卡口（lab LCP ±10% 带宽噪音，只警告）。
- 逃生通道：预算豁免走临时申请（登记恢复时间），禁止无痕跳过。

```yaml
# 一一对应：门禁演进三阶段的 CI 配置切换
stages:
  stage1_manual:
    mechanism: 性能评审表 + review 关注点
    config: null                          # 无 CI，仅文档

  stage2_report_only:                     # 半自动：只报告不阻塞（≥1个月适应期）
    lighthouse-ci:
      assertions:
        categories:performance: [warn, { minScore: 0.9 }]
    size-limit:
      action: comment                     # 超限只在 PR 评论
      failure: false
    exit_to_stage3: { false_positive_rate: "<10%", soak_weeks: 4 }

  stage3_blocking:                        # 全自动：超预算阻塞合并
    size-limit:
      action: fail                        # 硬卡口：确定性指标
      limits: { total_js_gzip: 300KB, css_gzip: 60KB, image_total: 500KB }
    lighthouse-ci:
      assertions:
        categories:performance: [error, { minScore: 0.9 }]   # 3 次中位
      action: fail
    lab_metrics:
      action: warn                        # 软卡口：波动大的只警告
      tolerance: ±10%
    waiver:                               # 逃生通道：登记式豁免
      file: PERF_WAIVERS.yml
      require: [reason, owner, expire_date]  # expire 后自动恢复阻塞
```
