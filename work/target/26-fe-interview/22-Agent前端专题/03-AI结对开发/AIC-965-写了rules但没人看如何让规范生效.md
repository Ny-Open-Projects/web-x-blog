---
title: [AIC-965] 团队写了厚厚的 AI rules 文档，但大家还是凭习惯用、规范形同虚设，如何让规范真正生效？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-965：团队写了厚厚的 AI rules 文档，但大家还是凭习惯用、规范形同虚设，如何让规范真正生效？
**答**：
- 根因是「规范与工作流脱节」——结论：靠自觉的规范必然失效，要把规范嵌入工具链（IDE 提示、pre-commit、CI 门禁）让人绕不开。
- 降低遵从成本：规范要「就在手边」——rules 文件放在仓库里随代码版本走、AI 自动加载，而不是让人去另一个 wiki 拷贝；越省力越会被遵守。
- 让违规「立刻可见且可解释」：工具报错时说清「违反了哪条规范、为什么、怎么改」，而非冷冰冰的 error——教育而非惩罚。
- 追问钩子：能提出「规范的生命力在于反馈闭环——收集违规数据看哪些规范常被违反，要么改规范（可能本身不合理）要么加强工具」的候选人，把规范当产品来迭代。

```typescript
// 规范生效：嵌入工具链 + 可解释的违规提示
const RULES = [
  { id:'PRICE-INT', check:src=>!src.includes('parseFloat'), msg:'金额必须用整数分（避免浮点误差）', fix:'改用 Math.round(price*100)' },
];
function enforce(src) {
  return RULES.filter(r=>!r.check(src)).map(r=>({
    rule:r.id, why:r.msg, how:r.fix })); // 说清违反什么、为什么、怎么改
}
// 违规反馈闭环：统计哪条规范最常被违反，反推规范本身是否合理
function violationStats(sources) {
  const counts = {};
  for (const src of sources) for (const v of enforce(src))
    counts[v.rule] = (counts[v.rule] || 0) + 1;
  return Object.entries(counts).sort((a,b) => b[1]-a[1]);
}
console.log(enforce('const p = parseFloat(input)'));
console.log(violationStats(['parseFloat(x)', 'parseFloat(y)'])); // 高频违规→考虑改规范/工具
```
