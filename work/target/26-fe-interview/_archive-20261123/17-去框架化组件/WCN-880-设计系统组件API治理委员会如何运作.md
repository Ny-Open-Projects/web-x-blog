---
title: [WCN-880] 设计系统的「组件 API 治理委员会」如何运作？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-880：设计系统的「组件 API 治理委员会」如何运作？

**答**：
- 结论先行：治理委员会的职责是「守住组件 API 的长期一致性」——它不是审批一切的官僚机构，而是对「新增/破坏性变更」做把关，日常变更靠自动化门禁 + owner 自治。
- 组成：设计系统核心团队 + 资深业务前端代表 + a11y 专家 + 平台架构师——兼顾一致性、业务可用性、合规与工程可行性。
- 职责边界：需要委员会评审的是——新增公共组件、API 破坏性变更（deprecation/重命名）、跨团队共享的契约调整；纯内部 bugfix、不影响公共 API 的改动由 owner 自行决定。
- 运作机制：定期例会（如双周）+ 异步 RFC（重大变更先写 RFC 收集意见）；评审用统一 checklist（复用价值、API 设计、a11y、token 化、向后兼容）；决策落 ADR 留痕。
- 效率保障：大部分变更由自动化门禁（契约校验、a11y 扫描、体积预算）拦截，委员会只看机器判不了的「设计取舍」；设评审 SLA（如 3 个工作日）避免成为瓶颈。
- 追问钩子：面试官会问「委员会会不会拖慢业务」——答：靠「分层授权」——把 80% 的常规变更交给自动化 + owner，委员会只处理 20% 的高影响决策，并用 SLA 约束；定期审查委员会自身效率。

```javascript
// 变更分级：决定走 owner 自治还是委员会评审
function routeChange(change) {
  const needsCommittee =
    change.kind === 'new-component' ||
    change.breaking === true ||
    change.affectsSharedContract === true;
  return needsCommittee
    ? { route: '委员会', reason: '高影响变更，需 RFC + 评审' }
    : { route: 'owner 自治', reason: '自动化门禁通过即可合入' };
}
console.log(routeChange({ kind: 'bugfix', breaking: false }));
console.log(routeChange({ kind: 'api-change', breaking: true, affectsSharedContract: true }));
```
