---
title: [ARC-534] 页面级 A/B 双跑验证（重写页面上线前）如何设计？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-534：页面级 A/B 双跑验证
**答**:
- 场景：重写页面（架构迁移/改版）上线前验证行为等价性——不只看指标，还要功能等价验证。
- 双跑方式一（流量对拍）：新旧页面各接 1% 流量（同特征用户分桶对称），对拍关键行为指标（转化/错误/性能）；方式二（影子请求）：新页面对同一用户会话影子执行数据请求层，对拍接口调用序列与结果（NODE-438 影子模式的前端版）。
- 功能等价断言：核心路径 E2E 双跑（同一脚本跑新旧两版，断言一致的输出/事件流，埋点 schema 一致性校验 ARC-424）。
- 对拍报告：自动生成差异清单（指标差/行为差/埋点差），差异定级（预期差异：改版本就有 vs 意外差异：必须解释）。
- 上线决策：双跑达标 → 灰度（ARC-476 流程）→ 全量；不达标 → 差异清单进修复。
```javascript
// 影子请求对拍
async function dualRun({ userPath, newImpl }) {
  const old = await runPage(oldImpl, userPath);                  // 现网执行
  const shadow = newImpl.requests.map(r => callApi(r).catch(e => ({ err: e })));
  const cmp = diffRequests(await old.requests, await Promise.all(shadow));
  report({ matchRate: 1 - cmp.diff / cmp.total, diffs: cmp.list }); // 调用序列一致性
}
```
