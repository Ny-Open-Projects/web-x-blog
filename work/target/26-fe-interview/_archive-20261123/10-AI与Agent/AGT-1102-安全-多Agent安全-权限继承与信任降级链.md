---
title: [1102] 多 Agent 链路里权限怎么传递与降级
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 面试题, 安全, 多Agent]
type: 面试题
---

## 1102：多 Agent 链路里权限怎么传递与降级

**答**：
- 权限继承规则：子 Agent 权限 ⊆ 父 Agent 权限 ∩ 自身任务所需——每往下传一层只能收窄不能放大；编排器下发能力令牌时显式收窄。
- 信任随距离衰减：距离原始用户越远（委托层级越深）信任等级越低，高危动作要求「距用户 N 跳内」的 Agent 才能执行。
- 链路审计：每跳传递记录令牌指纹（谁授的、缩了哪些权），事故时可沿链回溯「哪一跳放大了权限」。
- 追问钩子：为什么「只能收窄」如此重要？——放大权限的传递等于把凭证复制给更不可信的环节，是横向越权的主要来源；收窄是单向阀。

```ts
function delegate(parentCap, brief) {
  const child = intersect(parentCap, brief.required);   // 只能收窄
  child.depth = (parentCap.depth ?? 0) + 1;
  if (child.depth > 3 && brief.needsHighRisk) {
    return escalate(parentCap);                          // 深层委托高危回上级
  }
  return sign(child);                                    // 下发收窄令牌
}
```
