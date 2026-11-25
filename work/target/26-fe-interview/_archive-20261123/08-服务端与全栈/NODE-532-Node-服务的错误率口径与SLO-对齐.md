---
title: [NODE-532] Node 服务的错误率口径（业务错与系统错的 SLI 设计）如何对齐？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-532：错误率口径与 SLI
**答**:
- 口径问题：HTTP 500 ≠ 系统故障（业务校验失败也可能是 500 实现不规范）——SLI 必须按"错误分类学"（NODE-516）定义：系统错误率 = 系统错误数 / 总请求（业务错剔除），而不是 5xx 率。
- 口径实现：错误分类标签进指标（error_class: biz/sys/deps——响应中间件统一打标 NODE-516/372）、口径文档化（SLI 定义注册表：公式/分类规则/边界 case——争议场景裁定记录）。
- 边界 case 裁定：第三方超时算谁的（deps 类——上游问题但影响我 SLA：SLI 里计入但归因到 deps——双维度呈现）、降级成功算成功吗（降级 = 功能受损——单独 degraded 类不混入成功也不算失败，独立指标 ARC-447）。
- 一致性：SLI 口径与告警/看板/复盘口径统一（同一分类函数——防"看板 0.1% 告警说 1%"）。
- 演进：分类规则变更走评审（影响 SLI 历史——口径断点标注 NODE-531/ARC-614 同思想）。
```javascript
// 错误分类打标（响应统一出口）
function classify(e) {
  if (e instanceof AppError && e.biz) return 'biz';              // 业务错
  if (e.dep) return 'deps';                                      // 依赖错
  return 'sys';                                                  // 系统错
}
// SLI: sysRate = sys / total；degraded 单列：degradeCount / total
```
