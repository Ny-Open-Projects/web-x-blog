---
title: [NODE-456] Node 服务端风控规则引擎（实时决策）如何设计？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-456：服务端风控规则引擎
**答**:
- 决策链：事件接入（登录/下单/提现）→ 特征提取（实时特征：频率/金额/设备；离线特征：画像标签——特征服务缓存热点）→ 规则执行（条件组合 ARC-452 服务端版 + 名单：黑白灰）→ 决策（放行/挑战/拒绝/人工复核）→ 结果落库与反馈闭环（误判标注回调规则）。
- 性能预算：风控在交易链路内同步执行——P99 < 50ms（特征预计算 + 规则本地缓存 + 并行特征获取；超时降级放行（记录待审——风控超时不能拖死交易））。
- 规则治理：规则版本化与灰度（新规则先影子模式跑——只记录决策不改行为，验证命中率再生效 NODE-438）、规则效果监控（拦截率/误杀率/资金损失率）。
- 名单治理：名单变更审计（谁加的谁删的 NODE-442）、名单自动流转（灰名单按时间/行为晋级或解除）。
- 与前端配合：挑战动作（验证码/人脸）的下发协议与前端渲染（ARC-158 行为验证分级）。
```javascript
async function decide(event) {
  const feats = await Promise.race([features.get(event), timeout(30)]);
  const hits = rules.evaluate(feats, lists.of(event.uid));       // 条件 + 名单
  const decision = hits.some(h => h.action === 'reject') ? 'reject'
    : hits.some(h => h.action === 'challenge') ? 'challenge'
    : shadow.some(h => h.match) ? 'pass+shadow' : 'pass';        // 影子规则只记录
  await record(event, decision, hits);                           // 反馈闭环数据
  return decision;
}
```
