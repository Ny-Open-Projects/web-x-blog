---
title: [OPS-180] 发版 checklist 怎么工具化？哪些环节保留人工？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-180：发版 checklist 怎么工具化？哪些环节保留人工？
**答**：
- 人肉清单改为四道卡口：CI 全绿、产物体积与 sourcemap 检查、预发自动化冒烟、发布后自动验证（版本号/刷新状态/错误率基线）。
- 卡口放在流水线必经之路，不满足就阻断——机器不遗忘，遵守率从 60% 到 100%。
- 保留人工的两项：产品验收（灰度数据辅助判断）、回滚决策（平台给建议，人拍板，OPS-139）。
- checklist 内容本身版本化维护：新增检查项走 PR 评审，防止清单无限膨胀。
- 效果度量：发版耗时下降、checklist 漏项导致的事故数下降。

```yaml
# 发版 checklist 工具化：CI/发布平台卡口替代人肉
automated_gates:
  gate_1_ci:
    check: 单测 + lint + 构建 + 安全扫描全绿（OPS-150 安全项内嵌）
    block: 红则禁止生成发布单
  gate_2_artifact:
    check: bundle 体积变化 < 10%，sourcemap 已归档（OPS-077/157）
    block: 超阈值需 owner 二次确认
  gate_3_staging:
    check: 预发自动化冒烟 20 条通过
    block: 失败阻断晋级生产
  gate_4_post_deploy:
    check: 入口版本号校验 + CDN 刷新完成（OPS-117）+ 错误率 10 分钟基线对比
    block: 异常自动冻结后续放量并通知值班
human_only:
  - 产品验收（灰度数据辅助）
  - 回滚决策（平台建议 + 人拍板，OPS-139）
effect: checklist 遵守率 60% → 100%，单次发版耗时 -40%
```
