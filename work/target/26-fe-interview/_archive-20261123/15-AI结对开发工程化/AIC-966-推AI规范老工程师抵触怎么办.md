---
title: [AIC-966] 在商品列表团队推广 AI 规范，几位资深工程师很抵触「被规则束缚」，你怎么推进？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-966：在商品列表团队推广 AI 规范，几位资深工程师很抵触「被规则束缚」，你怎么推进？
**答**：
- 先理解抵触的合理内核：资深工程师的担心常是「规则拖慢我」「规则不适合我的场景」——结论：先听再改，别上来就压。
- 让他们成为「规则的制定者」而非「被管对象」：邀请资深工程师参与规则评审，把他们的经验写进规范（他们的隐性知识被沉淀，反而有 ownership）。
- 用数据说话：展示规范降低了多少返工/事故，并允许「有理由的豁免」——规则的例外通道让专家保留判断空间，减少被束缚感。
- 追问钩子：能说出「推广的本质是改变人的行为，核心是让早期采纳者受益、让反对者参与决策，而非靠行政命令强推」的候选人懂组织变革。

```typescript
// 规范共建：让资深工程师参与 + 有理由的豁免
const adoption = {
  inviteReviewers:['资深A','资深B'], // 参与制定 → ownership
  exemptions: [ // 有理由的豁免，保留专家判断
    { rule:'PRICE-INT', who:'资深A', reason:'对接遗留系统必须浮点', expires:'2026-12-01' },
  ],
};
function applyRule(rule, person, now) {
  const ex = adoption.exemptions.find(e=>e.rule===rule && e.who===person && e.expires>now);
  return ex ? { enforce:false, reason:ex.reason } : { enforce:true };
}
console.log(applyRule('PRICE-INT','资深A','2026-11-23')); // 豁免生效
```
