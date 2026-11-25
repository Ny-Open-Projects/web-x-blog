---
title: [NODE-438] Node 服务的灰度期数据一致性（新旧逻辑并行写）如何保证？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-438：灰度期新旧逻辑并行写一致性
**答**:
- 场景：灰度切换核心逻辑（如计费规则重写），新旧代码同时处理不同用户的同类请求——数据结构/口径必须兼容（ARC-449 服务端版）。
- 双跑验证（影子模式）：新逻辑对同一输入影子计算（不落库只比对结果），灰度前先双跑校验一致率（新逻辑 bug 在灰度前暴露）；双跑结果抽样审计。
- 数据口径兼容：新旧逻辑写同一表时字段语义必须一致（金额单位/状态枚举——schema 前向兼容 NODE-335）；确实不同的新字段双写（旧逻辑写默认值）。
- 切换顺序：影子双跑 → 灰度读新写旧（或反之）→ 全量切换 → 旧逻辑下线；每步数据对账（ARC-382 加密切点对账）。
- 回滚数据兼容：全量切换后短期回滚——新逻辑写的字段旧逻辑必须能忽略（未知字段忽略策略，禁止 NOT NULL 新字段立即生效）。
```javascript
// 影子双跑
async function withShadow(req, newLogic, oldLogic) {
  const old = await oldLogic(req);
  if (shadowEnabled) {
    newLogic(req).then(n => shadowCompare(req, old, n)).catch(e => shadowError(e)); // 不落库
  }
  return grayEnabled(req) ? newLogic(req) : old;                 // 灰度后真切换
}
```
