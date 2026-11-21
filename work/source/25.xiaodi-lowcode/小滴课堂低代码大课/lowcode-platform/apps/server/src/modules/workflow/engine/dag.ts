import { NodeContract, GraphNode, GraphEdge } from '@lowcode/shared';
import { WorkflowServices } from '../nodes/providers';

export type PortBag = Record<string, unknown>;

export interface NodeExecutor {
  (
    inputs: PortBag,
    params: Record<string, unknown>,
    ctx: ExecCtx,
  ): Promise<PortBag> | PortBag;
}

/** 审计条目：高风险节点（脚本/大模型）执行后写入。 */
export interface AuditEntry {
  tenantId?: string;
  runId: string;
  nodeId: string;
  nodeType: string;
  codeHash?: string;
  durationMs: number;
  status: 'success' | 'error' | 'timeout';
  errorMessage?: string;
  outputBytes?: number;
  /** 实际隔离层：vm 软隔离 / container 容器硬隔离。 */
  isolation?: 'vm' | 'container';
}

export type AuditSink = (e: AuditEntry) => Promise<void> | void;

export interface ExecCtx {
  tenantId?: string;
  runId: string;
  caller: string;
  /** 副作用节点的可替换 Provider（短信/OSS/表单）。默认 in-memory，生产可换云厂商实现。 */
  services?: WorkflowServices;
  /** 审计写入入口（脚本/大模型节点执行后回调）。 */
  audit?: AuditSink;
  /** 当前执行节点 ID（由 runDag 注入，供审计定位）。 */
  currentNodeId?: string;
}

export interface NodeDef {
  contract: NodeContract;
  exec: NodeExecutor;
}

export type Registry = Record<string, NodeDef>;

export type NodeTrace = (
  nodeId: string,
  status: string,
  input?: unknown,
  output?: unknown,
  durationMs?: number,
) => Promise<void> | void;

/**
 * 拓扑排序（Kahn）。检测到环则抛错，避免死循环。
 * 返回节点执行顺序（数组）。
 */
export function topoSort(graph: { nodes: GraphNode[]; edges: GraphEdge[] }): string[] {
  const indeg: Record<string, number> = {};
  const adj: Record<string, string[]> = {};
  graph.nodes.forEach((n) => {
    indeg[n.id] = 0;
    adj[n.id] = [];
  });
  graph.edges.forEach((e) => {
    if (!(e.from in indeg) || !(e.to in indeg)) throw new Error('边引用了不存在的节点');
    adj[e.from].push(e.to);
    indeg[e.to]++;
  });
  const queue = Object.keys(indeg).filter((k) => indeg[k] === 0);
  const order: string[] = [];
  while (queue.length) {
    const cur = queue.shift()!;
    order.push(cur);
    for (const nxt of adj[cur]) {
      if (--indeg[nxt] === 0) queue.push(nxt);
    }
  }
  if (order.length !== graph.nodes.length) throw new Error('检测到环，无法执行');
  return order;
}

/**
 * 执行 DAG：按拓扑序逐节点运行，将输出沿边注入下游输入端口。
 * 纯函数、无 HTTP 依赖，可独立单测。
 */
export async function runDag(
  graph: { nodes: GraphNode[]; edges: GraphEdge[] },
  registry: Registry,
  ctx: ExecCtx,
  onNode?: NodeTrace,
): Promise<Record<string, PortBag>> {
  const order = topoSort(graph);
  const outputs: Record<string, PortBag> = {};

  for (const nodeId of order) {
    const node = graph.nodes.find((n) => n.id === nodeId)!;
    const def = registry[node.type];
    if (!def) throw new Error(`未知节点类型: ${node.type}`);

    const inputs: PortBag = {};
    for (const e of graph.edges.filter((e) => e.to === nodeId)) {
      const src = outputs[e.from];
      if (src) inputs[e.toPort] = src[e.fromPort] ?? src['out'];
    }

    ctx.currentNodeId = nodeId;
    const start = Date.now();
    const out = await def.exec(inputs, node.params ?? {}, ctx);
    const duration = Date.now() - start;
    outputs[nodeId] = out;
    await onNode?.(nodeId, 'success', inputs, out, duration);
  }
  return outputs;
}
