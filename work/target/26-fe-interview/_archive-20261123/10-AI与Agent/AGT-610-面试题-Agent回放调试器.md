---
title: [AGT-610] 基于 trace 的「回放」功能怎么实现（重现一次任务执行的完整过程）？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-610：基于 trace 的「回放」功能怎么实现（重现一次任务执行的完整过程）

**答**：
- 回放 = 按时序重演 span 树 + 每个节点的输入输出（L3 数据按引用解密拉取）；回放器提供时间轴 scrubbing、节点断点、单节点重跑（工具节点真实重跑、LLM 节点可选"复用记录"或"重新生成"看漂移）。
- 回放与生产隔离：重跑走影子环境（同参数不同出口），LLM 重新生成的结果标记为 replay 变体不写回用户会话。
- 权限与成本：回放消耗真实 token（重新生成时），要配额与审批；只读回放（复用记录）零成本默认开放。

```javascript
async function replayTurn(trace, nodeId, { regen = false } = {}) {
  const node = trace.get(nodeId);
  if (node.kind === 'llm' && regen) {
    const variant = await shadowLLM(node.input, { tag: 'replay' });
    return { original: node.output, variant };   // 漂移对比，不写回
  }
  if (node.kind === 'tool') return shadowTool(node.tool, node.args); // 影子重跑
  return node.output;                            // 复用记录：零成本
}
```

