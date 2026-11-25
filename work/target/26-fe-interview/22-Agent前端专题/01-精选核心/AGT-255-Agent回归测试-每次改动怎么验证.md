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

**边界与易错**：

- 评测集只留经典题、不回流近期 badcase：集上不退化而线上崩，badcase 必须按月回流并标注来源。
- 新旧对比两次跑的 seed、工具 mock、数据版本不一致：差异被噪声淹没，必须固定 seed 与 mock 返回值，同一批样例跑三次取分布。
- 只看总分不看分桶：总分涨 1% 但某类任务跌 15% 照样上线，必须按场景分组看退化分布。

**追问**：

1. 输出本身随机，-2% 怎么判断是真退化？→ 固定温度与 seed 多次采样比较分布，或同一用例跑 N 次算成功率，单次差异不下结论。
2. 评测集被反复调参刷过了怎么办？→ 留一份不公开的 holdout 只在上线前跑，公开集用于日常迭代。
3. 工具实现改了，mock 会不会把 bug 盖住？→ 会；工具自身的编排逻辑要有单测，另留少量连真实沙箱的端到端用例。
