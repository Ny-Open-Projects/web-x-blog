---
title: [AIC-997] 用 AI 加速迁移，结果生成了一堆「临时适配层、兼容开关、半成品抽象」，反而制造了新遗留，如何避免？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-997：用 AI 加速迁移，结果生成了一堆「临时适配层、兼容开关、半成品抽象」，反而制造了新遗留，如何避免？
**答**：
- 根因是「迁移只用不收」：临时适配/开关本就是过渡手段，缺少清理机制就会沉淀为新遗留——结论：每个临时产物出生时就要有「死亡计划」。
- 给临时产物打标记与到期：用 `// @temporary since:2026-11 reason:... owner:...` 注释或登记到台账，配合 CI 扫描在到期后提醒/阻断，强制清理。
- 控制 AI 产出「半成品抽象」：要求 AI 每次改动是完整闭环（实现 + 调用方 + 测试），不做「先留个空壳以后填」的抽象；评审时警惕过度设计。
- 追问钩子：能提出「迁移的完成标准应包括『临时产物清零』——如果开关和适配层还在，迁移就还没真正结束」的候选人，把清理纳入了迁移定义。

```typescript
// 临时产物台账 + 到期扫描
const temps = [
  { id:'adapter-v1', kind:'adapter', created:'2026-06-01', expires:'2026-12-01', owner:'a' },
  { id:'flag-price', kind:'flag', created:'2026-09-01', expires:'2026-11-20', owner:'b' },
];
function overdue(temps, today) {
  return temps.filter(t=>t.expires<today).map(t=>({ id:t.id, owner:t.owner, overdueDays:
    Math.floor((new Date(today)-new Date(t.expires))/864e5) }));
}
console.log(overdue(temps,'2026-11-23')); // flag-price 已过期 → 强制清理
```
