---
title: [TST-759] 收束题：AI 能替代性能/安全专家吗，边界在哪
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-759：收束题：AI 能替代性能/安全专家吗，边界在哪

**答**：
- 结论：AI 替代的是「重复的诊断与枚举」，替代不了「业务上下文判断 + 创造性攻防 + 责任承担」。
- 性能侧：AI 能归因常见回归、生成负载，但容量决策与权衡需要人；安全侧：AI 能扫已知漏洞，但逻辑漏洞与攻防博弈靠人。
- 正确表述是「AI 放大专家产能」——把专家从琐事解放到高价值判断，而非取代。
- 追问钩子：面试官说「我们已经用 AI 全代替了安全团队」，你怎么回应？

```javascript
// 能力边界矩阵：哪些可委托 AI
const BOUNDARY = {
  perf: { delegate: ['回归归因', '负载生成', '阈值调整'], human: ['容量决策', '架构权衡'] },
  sec: { delegate: ['已知漏洞扫描', 'payload 变体'], human: ['逻辑漏洞', '攻防博弈', '责任认定'] },
};
function whoOwns(domain, task) {
  if (BOUNDARY[domain].delegate.includes(task)) return 'AI';
  if (BOUNDARY[domain].human.includes(task)) return 'human';
  return 'unclear';
}
console.log(whoOwns('sec', '逻辑漏洞')); // human
```
