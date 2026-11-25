---
title: [WCN-516] 组件平台化组织：平台组与业务组在「元素 API 变更」上的 SLA 与协商机制怎么设计？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-516：组件平台化组织：平台组与业务组在「元素 API 变更」上的 SLA 与协商机制怎么设计？

**答**：
- 结论：把 API 变更当作「对外契约」，用 semver + 冻结窗口 + 消费方登记三件套约束。
- SLA：breaking 变更提前 2 个大版本预告，提供 codemod 与 6 个月兼容期。
- 协商机制：业务方在 registry 登记依赖版本，平台变更时自动算出影响面并通知 owner。
- 追问：业务方死守旧版本不升级怎么办？（答：兼容期到期强制 + 冻结旧版本安全补丁以外的演进）

```javascript
const consumers = new Map(); // repo -> { deps: {tag: range}, owner }
function registerConsumer(repo, deps, owner) { consumers.set(repo, { deps, owner }); }
function impactOf(tag, newMajor) {
  const affected = [];
  for (const [repo, { deps, owner }] of consumers) {
    const r = deps[tag];
    if (r && !r.startsWith(`^${newMajor}`)) affected.push({ repo, owner, range: r });
  }
  return affected; // 逐个发升级通知
}
```
