---
title: [MFM-454→MFM→MFW-454] 笔试：手写上线检查机器人（八问自动应答）
date: 2026-11-20
 categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-454：MFM→454：上线八问机器人
**答**：实现 `preMergeBot(prDiff, answers)`——合并前自动回答八问（数据来自管线而非口述）：①影响路由（蓝图闭包）②缓存策略变化（fetch 选项 diff）③新外部依赖（审计卡）④回滚方案（双版本指针在？）⑤性能预算（快照 vs 表）⑥安全头/CSP 违规 ⑦实验键入矩阵否 ⑧数据出口新字段（payload 审计）——每问附证据链（命令+输出摘要），无数据=「未知」标红（不允许口 say yes）。

```javascript
export async function eightQuestions (pr) {
  const bp = await blueprintOf (pr.base, pr.head)
  return [
    { q: '影响路由', a: bp.routes, v: 'blueprint-diff' },
    { q: '回滚', a: dualVersionReady (pr.routes) ? 'pointer-ready' : 'MISSING', v: 'rt-check' },
    { q: '预算', a: perfSnap vs (table), v: 'perf-snap' },
    { q: '出口', a: payloadAudit (pr).newFields, v: 'flight-audit' },
    ...// 每问 { answer, evidence: cmd+output, unknownOk: false }
  ].map((r) => ({ ...r, status: r.evidence ? 'data' : 'UNKNOWN' }))   // 无数据即红
}
// 评语义：任一 UNKNOWN 或 FAIL → block merge（口说无凭）
```
**评分点**：
- 数据源回答（管线取证——不靠开发者记忆自报）
- UNKNOWN=红（「没查」比「否」更危险——显式化）
- 八问覆盖（路由/缓存/依赖/回滚/性能/安全/实验/出口——发布风险全景）
- 证据链可复核（命令+输出——审计不是截图）
