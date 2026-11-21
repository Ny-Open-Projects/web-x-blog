---
title: [ARC-095] 流程引擎的前端可视化（节点连线 DAG）如何设计？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-095：流程引擎的前端可视化（节点连线 DAG）如何设计？
**答**：
- 数据模型：nodes + edges 两个集合，DAG 约束（无环）在编辑时校验（拓扑检测），不是靠用户自觉。
- 编辑器分层：数据层（图模型操作：增删节点/连线，可撤销）、几何层（坐标/碰撞/吸附）、视图层（SVG/Canvas 渲染，节点多时 Canvas）。
- 连线规则引擎化：端口类型匹配、必连/禁连规则声明式配置，非法连线即时反馈。

```typescript
// 流程编辑器数据模型 + DAG 校验
interface FlowNode { id: string; type: 'start' | 'approve' | 'cc' | 'end'; x: number; y: number; props: Record<string, unknown>; }
interface FlowEdge { id: string; source: string; target: string; condition?: string; }

class FlowModel {
  nodes: FlowNode[] = [];
  edges: FlowEdge[] = [];

  addEdge(e: FlowEdge): { ok: boolean; reason?: string } {
    if (e.source === e.target) return { ok: false, reason: '自环禁止' };
    if (this.hasPath(e.target, e.source)) return { ok: false, reason: '会形成环，DAG 不允许' };  // 拓扑检测
    const rule = portRules(this.node(e.source).type, this.node(e.target).type);
    if (!rule.allowed) return { ok: false, reason: rule.reason };          // 声明式连线规则
    this.edges.push(e);
    return { ok: true };
  }
  private hasPath(from: string, to: string, seen = new Set<string>()): boolean {
    if (from === to) return true;
    if (seen.has(from)) return false;
    seen.add(from);
    return this.edges.filter(e => e.source === from)
      .some(e => this.hasPath(e.target, to, seen));
  }
  validate(): string[] {                       // 保存前全图校验
    const errors: string[] = [];
    if (!this.nodes.some(n => n.type === 'start')) errors.push('缺少开始节点');
    for (const n of this.nodes) {
      const inDeg = this.edges.filter(e => e.target === n.id).length;
      const outDeg = this.edges.filter(e => e.source === n.id).length;
      if (n.type !== 'start' && inDeg === 0) errors.push(`节点 ${n.id} 不可达`);
      if (n.type !== 'end' && outDeg === 0) errors.push(`节点 ${n.id} 无下游出口`);
    }
    return errors;
  }
}
```
