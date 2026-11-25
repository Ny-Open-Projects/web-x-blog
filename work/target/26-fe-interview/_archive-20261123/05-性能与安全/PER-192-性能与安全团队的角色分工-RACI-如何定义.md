---
title: [PER-192] 性能与安全团队的角色分工（RACI）如何定义？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-192：性能与安全团队的角色分工（RACI）如何定义？

**答**：
- RACI 四角色：**R 执行、A 拍板（每行有且只有一个）、C 被咨询、I 被知会**；A 缺位的事故复盘直接定为流程缺陷。
- 典型分工：预算定义平台组拍板业务组执行；漏洞修复安全组拍板业务组执行；应急响应是业务组与安全组共同 R、EM 拍板；合规法务 A。
- 冲突高发区在"性能 vs 安全"（如 CSP 与内联脚本、缓存与过期策略），裁决权明确给安全侧，性能用技术手段补（nonce、分版本缓存）。
- RACI 要贴在值班手册与 CR 模板里，出事时不用现场争论谁负责。

```yaml
# 性能与安全 RACI：R 执行 A 拍板 C 被咨询 I 被知会
raci_matrix:
  性能预算定义:
    platform: A
    biz_front: R
    product: C
    qa: I
  性能修复执行:
    platform: C
    biz_front: R
    em: A
    qa: I
  安全漏洞修复:
    sec_platform: A
    biz_front: R
    qa: C
    ops: I
  安全应急响应:
    sec_platform: R
    biz_front: R
    em_leader: A
    ops: C
    pr_legal: I
  合规与隐私:
    sec_platform: C
    legal: A
    biz_front: R
    data_team: C
  rule: "每行有且只有一个 A；A 缺位的事故复盘定为流程缺陷"
```
