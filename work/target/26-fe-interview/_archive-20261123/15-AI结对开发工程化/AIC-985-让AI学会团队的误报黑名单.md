---
title: [AIC-985] 如何把团队积累的「误报黑名单」喂给 AI Review，让它别再犯同样的误报？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-985：如何把团队积累的「误报黑名单」喂给 AI Review，让它别再犯同样的误报？
**答**：
- 误报黑名单要「可执行」而非文档：把每条误报转成 AI 可理解的结构化样例——「这种代码模式是合法的，因为 X」，作为 few-shot 示例或规则例外注入评审 prompt/上下文。
- 分层注入：全局黑名单进系统提示（所有评审都遵守），模块级黑名单按评审文件动态加载（如测试文件的 any 豁免）——结论：注入要与评审上下文相关，别全塞。
- 要防「黑名单过拟合」：样例太多会占用上下文并可能让 AI 对类似但真有问题的代码也放行；定期清理过时样例，用回归样例验证 AI 仍抓得住真问题。
- 追问钩子：能提出「黑名单要带『反例的反例』——即合法模式的边界在哪，避免 AI 学到过度宽松的判断」的候选人理解 Few-shot 的双刃剑。

```typescript
// 误报黑名单作为结构化 few-shot 样例注入
const blacklist = [
  { pattern:'测试文件中的 any', example:'const data: any = mock()', reason:'mock无类型定义', scope:'test' },
];
function buildReviewContext(file, blacklist) {
  const scoped = blacklist.filter(b=> b.scope==='global' ||
    (b.scope==='test' && /\.(test|spec)\./.test(file)));
  return {
    rules: scoped.map(b=>`合法模式: ${b.example} (${b.reason})`),
    note:'以上是本团队确认的合法写法，不要误报',
  };
}
console.log(buildReviewContext('foo.test.ts', blacklist).rules);
```
