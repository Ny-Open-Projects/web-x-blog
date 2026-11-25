---
title: [TST-879] 收官：未来 3 年 AI 会如何重塑测试工程，你如何保持竞争力？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-879：收官：未来 3 年 AI 会如何重塑测试工程，你如何保持竞争力？
**答**：
- 结论：AI 会接管「可验证的重复劳动」（生成/归因/自愈），测试工程师的价值上移到「定义质量标准、设计验证策略、判断业务风险」——越往上越难被替代。
- 趋势判断：测试从「写用例」转向「训 AI + 审 AI + 定护栏」，平台从「执行工具」变成「AI 质量中枢」。
- 能力投资：深耕业务领域知识、质量体系设计、AI 工具链驾驭（RAG/prompt/评测）三项复合能力。
- 心态：把 AI 当杠杆而非威胁——用 AI 把重复工作自动化，把自己的时间投向高判断力任务。
- 追问钩子：如果明年 AI 能自动完成你现在 70% 的工作，你打算把省下的时间投入到哪三件事上？

```javascript
// 竞争力 portfolio：把时间投向 AI 难替代的领域
const portfolio = {
  业务领域知识: '理解业务风险，定义什么值得测',
  质量体系设计: '分层/门禁/度量/成熟度——架构级能力',
  AI工具链驾驭: 'RAG/prompt/eval，把 AI 变成杠杆',
};
function futureProof(currentFocus) {
  const gap = Object.keys(portfolio).filter(k => !currentFocus.includes(k));
  return { recommendation: gap, note: gap.length ? '优先补齐高判断力能力' : '结构均衡' };
}
console.log(futureProof(['写用例', '跑测试'])); // 建议补三项
```
