---
title: [AIC-957] IM 消息状态机让 AI 重构，结果「已读→撤回」这个边界被改坏了，如何提前防、事后抓？
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-957：IM 消息状态机让 AI 重构，结果「已读→撤回」这个边界被改坏了，如何提前防、事后抓？
**答**：
- 状态机的边界（合法/非法转换）是最容易被重构破坏的——结论：重构前先把状态机「形式化」为转换表，作为不可变的规格。
- 提前防：把转换表写成 AI 不可改的规格文件 + 转换表测试（枚举所有 from×to），重构产出一律跑这套测试，改坏边界立即失败。
- 事后抓：在灰度期对关键状态转换埋点监控（非法转换次数），一旦出现非零立即回滚——结论：形式化规格 + 运行时监控双保险。
- 追问钩子：能说出「把隐性边界显式化为可执行的规格，是重构安全的前提；AI 不应被允许修改规格本身」的候选人，具备规格驱动的重构观。

```typescript
// 形式化状态机规格（AI 不可改）
const SPEC = { sending:['sent','failed'], sent:['read','recalled'],
  read:['recalled'], recalled:[], failed:['sending'] };
function canTo(from,to){ return (SPEC[from]||[]).includes(to); }
function allTransitionTests() { // 枚举所有 from×to
  const states=Object.keys(SPEC), cases=[];
  for(const f of states) for(const t of states)
    cases.push({ from:f, to:t, legal:canTo(f,t) });
  return cases;
}
// 重构后用同一套测试验证；任何边界被改都会暴露
const cases=allTransitionTests();
console.log(cases.filter(c=>c.from==='read' && c.to==='recalled')); // 合法边界
```
