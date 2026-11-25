---
title: [ARC-131] 质量门禁体系（MR 卡口）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-131：质量门禁体系（MR 卡口）如何设计？
**答**：
- 门禁分级：阻塞级（lint/type 错误、受影响测试失败、覆盖率增量不达标、安全扫描高危）必须过；建议级（复杂度、命名、包体积趋势）只展示不挡路——全阻塞会让开发效率崩塌并催生豁免滥用。
- 性能预算也是门禁：包体积 diff 超 5% 阻塞，bundle 分析报告随 MR 评论输出。
- 豁免机制显式化：豁免必须带理由与期限，豁免记录进月报，超期未还的自动升级到 tech lead——没有审计的豁免最终会变成长期绿灯。
- 反馈速度是采纳率关键：门禁总时长预算 10 分钟内，慢的检查移到合并后异步跑（如全量 E2E）。

```yaml
# MR 质量门禁配置（合并机器人消费）
merge_gates:
  blocking:                          # 阻塞合并
    - lint:            { rule: error=0 }
    - type_check:      { rule: error=0 }
    - affected_tests:  { rule: fail=0, tool: vitest-related }
    - coverage_gate:   { mode: incremental, changed_files_lines: ">= 80%" }
    - bundle_budget:   { js_diff: "<= +5%", lcp_budget: "<= +100ms" }
    - security_scan:   { sev: [critical, high], rule: count=0 }
    - api_contract:    { rule: "OpenAPI diff 无 breaking change（breaking 需后端 owner approve）" }
  advisory:                          # 仅评论提示
    - complexity:      { warn: "> 15" }
    - code_smells:     { warn: "> 10" }
    - doc_update:      { warn: "改了公共 API 但没更新文档" }
  exemption:
    flow: 提交豁免申请 → 说明理由 + 期限 → tech lead approve
    audit: 月报统计豁免数量与超期项，超期自动升级
  latency_budget: "< 10min"          # 门禁总时长，超了就优化或异步化
```

---

## 十五、可观测性与 DevEx 架构（ARC-132 ~ ARC-138）
