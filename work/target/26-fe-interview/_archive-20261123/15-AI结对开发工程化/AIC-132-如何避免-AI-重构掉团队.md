---
title: [AIC-132] 如何避免 AI 重构掉团队的领域概念（命名、抽象）？「领域语言保护」怎么实现？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-132：如何避免 AI 重构掉团队的领域概念（命名、抽象）？「领域语言保护」怎么实现？
**答**:
- 问题：AI 倾向把业务概念泛化成通用名（把 `skuSnapshot` 重构成 `data`、把营销领域的「坑位」改成「slot」），重构后代码可读性对团队反而下降——领域语言是团队的隐性资产。
- 保护手段：① 术语表（glossary）进规则文件，标注「禁止改名的概念清单」及其含义 ② lint 自定义规则保护核心命名（如禁止改特定导出名，用 rename 检测）③ 领域抽象的「注册表」——核心类型/服务清单，AI 改动触碰注册表项必须走增强 review。
- 沟通层面：任务卡里显式写「本模块领域语言见 glossary.md §3，术语按表使用」。
- 反向利用：让 AI 帮忙发现「术语漂移」——扫描代码中同一概念的不同命名，产出统一建议，人裁决后回写术语表。
- 追问钩子：这题考 DDD 与 AI 的结合点——「领域语言是人机共享的契约」，保护它的优先级高于追求通用美感。

```javascript
// 术语保护 lint 规则（伪实现）
const protectedTerms = { skuSnapshot: 'SKU 快照（营销口径）', pit: '坑位（运营位概念）' };
function checkRenames(diff) {
  return diff.renamedSymbols
    .filter(r => protectedTerms[r.from])
    .map(r => ({ level: 'blocker', msg: `${r.from} 是受保护领域术语：${protectedTerms[r.from]}` }));
}
```
