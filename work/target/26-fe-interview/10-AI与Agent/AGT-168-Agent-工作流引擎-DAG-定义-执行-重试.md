---
title: [AGT-168] Agent 工作流引擎（DAG 定义/执行/重试）如何平台化？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-168：Agent 工作流引擎（DAG 定义/执行/重试）如何平台化？
**答**：
- 三层分离：DAG 定义（声明式 JSON/YAML：节点=Agent 或工具，边=数据依赖，支持条件分支）、执行器（拓扑排序调度、并行分支并发跑、失败节点的重试与下游跳过）、平台能力（版本化、运行历史、人工节点、回填重跑）。
- 重试策略节点级配置：指数退避重试 × 次数、失败后「跳过继续」（软依赖）或「熔断整图」（硬依赖）由边类型声明。
- 状态与恢复：每个节点完成的输出持久化（同 AGT-137 checkpoint），重跑只执行失败节点及其下游——这对「跑了两小时的流水线挂在第 19 步」是生死能力。
- 前端价值：DAG 可视化编辑 + 运行时状态上色（绿/红/黄）+ 节点点击看输入输出，是 Agent 平台最核心的调试界面。

```typescript
// 迷你 DAG 工作流引擎：定义 schema + 拓扑执行 + 节点级重试
import { z } from 'zod';

const NodeDef = z.object({
  id: z.string(), type: z.enum(['agent', 'tool', 'human']),
  config: z.record(z.unknown()),
  retry: z.object({ times: z.number().default(2), backoffMs: z.number().default(1000) }).default({ times: 2, backoffMs: 1000 }),
  onFailure: z.enum(['abort', 'skip']).default('abort'),
});
const DagDef = z.object({ nodes: z.array(NodeDef), edges: z.array(z.object({ from: z.string(), to: z.string(), soft: z.boolean().default(false) })) });
type DagDef = z.infer<typeof DagDef>;

export async function runDag(dag: DagDef, runId: string, input: unknown, store: CheckpointStore) {
  const outputs = new Map<string, unknown>([['__input__', input]]);
  const indeg = new Map(dag.nodes.map((n) => [n.id, dag.edges.filter((e) => e.to === n.id).length]));
  const dec = (id: string) => { const v = indeg.get(id)! - 1; indeg.set(id, v); return v; }; // 入度递减
  const queue = dag.nodes.filter((n) => indeg.get(n.id) === 0).map((n) => n.id);
  const skipped = new Set<string>();

  while (queue.length) {
    const id = queue.shift()!;
    const node = dag.nodes.find((n) => n.id === id)!;
    if (skipped.has(id)) { /* 软依赖上游失败被跳过 */ }
    else {
      const deps = Object.fromEntries(dag.edges.filter((e) => e.to === id).map((e) => [e.from, outputs.get(e.from)]));
      let ok = false, lastErr: unknown;
      for (let i = 0; i <= node.retry.times; i++) {                      // 节点级重试 + 退避
        try {
          outputs.set(id, await executeNode(node, deps, runId, store));  // 执行结果持久化（checkpoint）
          ok = true; break;
        } catch (e) { lastErr = e; await new Promise((r) => setTimeout(r, node.retry.backoffMs * 2 ** i)); }
      }
      if (!ok) {
        if (node.onFailure === 'abort') throw lastErr;                 // 硬依赖：熔断整图
        skipped.add(id); metrics.inc(`dag.skip.${id}`);                // 软依赖：跳过
      }
    }
    for (const e of dag.edges.filter((x) => x.from === id)) {
      if (e.soft && skipped.has(id)) skipped.add(e.to);
      if (dec(e.to) === 0) queue.push(e.to);                           // 拓扑推进
    }
  }
  return outputs;
}

function executeNode(n: any, deps: unknown, runId: string, store: CheckpointStore) {
  void deps; void runId; void store;
  return Promise.resolve({ nodeId: n.id, at: Date.now() });
}
const metrics = { inc: (n: string) => { void n; } };
// 使用前 new CheckpointStore()（AGT-137 实现）
```

---

## 二十九、数据与训练视角
