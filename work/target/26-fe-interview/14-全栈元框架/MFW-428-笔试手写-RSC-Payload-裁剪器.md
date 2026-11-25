---
title: [MFM-428→MFW→MFW-428] 笔试：手写 RSC Payload 出口字段审计器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-428：出口审计器
**答**：实现 `auditPayload(flightText, route, declared)`（MFW-318 的执行器）：1) 解析 flight 行格式（模块引用行 M*/值行等——简化为 JSON 行提取）→ 还原实际下发的 props 字段集；2) 与声明表（route→allowedFields，MFW-318 注册表）比对：超出 → 违规（含字段路径与值类型摘要——不打印值本身防日志泄密）；3) 新字段检测（declared 无此路径）→ PR 标签建议（数据出口变更评审）；4) 体积分布（每顶层 prop 字节数——膨胀归因）；5) 输出报告 + exitCode（unauthorized>0 → 1）。

```javascript
export function auditFlight(flight, { allowed, route } = {}) {
  const exposed = new Map()                                // path -> bytes
  for (const line of flight.split('\n')) {
    if (!line.startsWith('[{"") && !line.includes(':"')) continue
    for (const [k, v] of Object.entries(tryJson(line.slice(1)) ?? {}))
      walkExpose(k, v, k, exposed)                          // 递归记路径+字节
  }
  const violations = [...exposed.keys()].filter((p) => !matchAllowed(p, allowed))
  const growth = topGrowth(exposed, prev?.[route])
  return { route, exposedCount: exposed.size, violations: violations.map((p => ({ p, kind: kindOf(exposed.get(p)) }))),
    topHeavy: [...exposed].sort((a, b) => b[1]-a[1]).slice(0, 5),
    exit: violations.length ? 1 : 0 }
}
```
**评分点**：
- 值不打印只记类型摘要（审计日志自身不泄密）
- 双向治理（超纲=违规阻断；新增=PR 评审标签——出口即 API）
- 体积分布（payload 膨胀归因到 prop——MFW-237 的数据源）
- exitCode 与 CI 解耦（独立 job 可灰度启用）
