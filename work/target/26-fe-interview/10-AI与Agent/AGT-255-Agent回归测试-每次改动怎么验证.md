---
title: [AGT-255] Agent 回归测试——prompt/模型/工具变更后怎么验证不退化？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-255：改了一句系统提示，怎么知道 Agent 没有在别的任务上退化？

**答**:
- 回归集是生命线：固定 100~300 条覆盖核心场景的任务集（含边界与历史 badcase），任何变更（prompt/模型版本/工具实现/RAG 索引）必须全量跑一遍对比基线——Agent 的改动牵一发动全身，单点验证不可靠。
- 对比方式：新旧版本并行跑同一评测集（环境固定：mock 工具+固定数据），逐任务对比分数——分级统计（提升/持平/退化的任务数与分布），退化任务抽样人工分析。
- 门禁与灰度：核心集分数下降超阈值（如成功率 -2%）→ 阻断上线；临界变更（小幅波动）→ 线上灰度 5% 流量 + 在线指标观察（AGT-259）后再放量。
- 变更关联：每次评测记录"变更 diff"（改了什么 prompt/什么配置）——评测历史与变更历史关联，才能做长期归因（哪类改动最常引起退化）。

```javascript
async function regression(change) {
  const [oldS, newS] = await Promise.all([
    runSuite(SUITE, { cfg: OLD }),
    runSuite(SUITE, { cfg: NEW }),
  ]);
  const diff = compare(oldS, newS);   // 逐任务分级
  report(change, diff);               // 记录 diff 关联
  if (diff.successRate.delta < -0.02)
    throw new BlockError('回归退化，阻断上线');   // 门禁
  if (Math.abs(diff.successRate.delta) < 0.01)
    return { action: '灰度 5% 观察在线指标' };
  return { action: '放行' };
}
```
