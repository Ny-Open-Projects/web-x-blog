---
title: [PER-935] 性能平台如何支撑「页面级 Owner 制」
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-935：性能平台如何支撑「页面级 Owner 制」

**答**：
- 归属自动化：根据路由与代码目录映射自动计算页面 Owner（git blame + 路由注册表），避免手工维护过期。
- Owner 权责：接收劣化告警、门禁豁免审批人、季度体检报告第一责任人；支持多 Owner（主责 + 备份）。
- 移交机制：页面归属变更时性能资产（基线/告警配置/豁免单）随路由移交，防止换人后告警无人认领。
- 度量：Owner 维度统计响应时长与修复率，纳入工程师影响力可见化。

```javascript
// 自动归属
const ROUTE_OWNER = [
  { match: /^\/shop/, owner: 'team-commerce', backup: 'alice' },
  { match: /^\/im/,   owner: 'team-im',       backup: 'bob' },
];
function ownerOf(path) {
  const r = ROUTE_OWNER.find(r => r.match.test(path));
  if (!r) return { owner: 'default', backup: null, warn: '未登记路由归属' };
  return { owner: r.owner, backup: r.backup };
}
// 告警按 ownerOf(page) 派发；路由表变更触发资产自动移交
```
