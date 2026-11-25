---
title: [MFW-604] route segment config 的审计：静态/动态声明的漂移检测
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-604：route segment config 审计

**答**:
- segment config 的声明面：dynamic/revalidate/fetchCache/runtime/ppr——「声明的意图」vs「实际行为」（隐式动态化：深层组件读 cookies——声明 force-static 但被动态 API 打脸——编译告警或静默降级 RBL-510 陷阱）。
- 审计的矩阵：声明 vs 实际（构建输出的路由类型 RBL-561）——「声明 force-static 实际 dynamic」= 语义矛盾（构建警告）；「未声明 + 实际 dynamic」= 隐式动态（提示显式化）；「声明 dynamic + 实际 static」= 浪费（每请求渲染但本可缓存——成本白付）。
- 漂移的 CI 检测：build manifest 的路由类型与「声明的 config」diff——「上次构建 vs 本次构建」的动态化漂移（升级/新组件引入的隐式动态化：路由画像对比 RBL-576）。
- 追问钩子：为什么「隐式动态化」的检测比「显式错误」更值得审计？——显式错误（force-static + cookies 冲突）编译即报；隐式动态（无声明 + 深层 cookies）静默发生（成本爆炸：每请求渲染 RBL-934 预算崩）——「静默成本变化」与静默错误同级危险（RBL-956 清单的成本版）；审计的目的：让「成本画像的变化」与「代码变更」关联（PR 引入动态化的归因）。

```typescript
// 审计：声明 vs 实际
interface RouteAudit {
  route: string;
  declared: 'static' | 'dynamic' | 'force-static' | 'isr' | undefined;
  actual: 'static' | 'dynamic' | 'isr';                  // 构建输出
}
function auditRoutes(audits: RouteAudit[]) {
  return audits.flatMap(a => {
    const findings = [];
    if (a.declared === 'force-static' && a.actual === 'dynamic')
      findings.push({ route: a.route, issue: 'contradiction', detail: '声明 force-static 但实际动态——动态 API 覆盖声明' });
    if (a.declared === undefined && a.actual === 'dynamic')
      findings.push({ route: a.route, issue: 'implicit-dynamic', detail: '隐式动态化——建议显式声明 dynamic 或 revalidate' });
    if (a.declared === 'dynamic' && a.actual === 'static')
      findings.push({ route: a.route, issue: 'wasted-dynamic', detail: '声明 dynamic 但实际静态——每请求渲染白付' });
    return findings;
  });
}
// 漂移检测：上次构建 vs 本次
function driftCheck(lastBuild, thisBuild) {
  return thisBuild.filter(t => {
    const prev = lastBuild.find(l => l.route === t.route);
    return prev && prev.actual !== t.actual;             // 类型翻转：static→dynamic
  }).map(t => ({ route: t.route, from: lastBuild.find(l => l.route === t.route).actual, to: t.actual }));
}
```
