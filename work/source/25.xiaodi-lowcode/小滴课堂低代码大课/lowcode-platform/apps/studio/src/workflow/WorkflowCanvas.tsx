import { useCallback, useRef, useState, useEffect } from 'react';
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
  addEdge,
  useNodesState,
  useEdgesState,
  type Connection,
  type Edge,
  type Node,
  type NodeTypes,
} from 'reactflow';
import { api } from './api';
import { Palette } from './Palette';
import { WorkflowNode } from './WorkflowNode';
import { WF_NODE_TYPE, type RFNodeData } from './types';
import type { NodeContract, GraphNode, GraphEdge, WorkflowGraph } from '@lowcode/shared';

const nodeTypes: NodeTypes = { [WF_NODE_TYPE]: WorkflowNode };

function defaultParams(c: NodeContract): Record<string, unknown> {
  if (c.type === 'ui.composePage') return { title: '动态生成的页面', components: [] };
  if (c.type === 'trigger.formSubmit') return { formId: 'form_default', data: { name: '示例', amount: 0 } };
  if (c.type === 'script.eval') return { code: 'setOutput({ ...data })' };
  if (c.type === 'ai.llm') return { prompt: '请处理：{{data}}', model: '', temperature: 0.7, maxTokens: 512 };
  return {};
}

function fallbackContract(type: string): NodeContract {
  return { type, label: type, category: 'transform', version: 1, inputs: [], outputs: [] };
}

export function WorkflowCanvas() {
  const [contracts, setContracts] = useState<NodeContract[]>([]);
  const contractByType = useRef<Record<string, NodeContract>>({});
  const [nodes, setNodes, onNodesChange] = useNodesState<RFNodeData>([]);
  const [edges, setEdges, onEdgesChange] = useEdgesState<Edge>([]);
  const [name, setName] = useState('未命名工作流');
  const [currentId, setCurrentId] = useState<string | null>(null);
  const [log, setLog] = useState('');
  const [busy, setBusy] = useState(false);
  const [generatedPageId, setGeneratedPageId] = useState<string | null>(null);
  const addCount = useRef(0);

  useEffect(() => {
    api
      .nodes()
      .then((cs) => {
        setContracts(cs);
        contractByType.current = Object.fromEntries(cs.map((c) => [c.type, c]));
      })
      .catch((e) => setLog('加载节点目录失败: ' + e.message));
  }, []);

  const portType = useCallback(
    (nodeId: string, handleId: string | null | undefined, dir: 'in' | 'out'): string | undefined => {
      const n = nodes.find((x) => x.id === nodeId);
      if (!n) return undefined;
      const c = n.data.contract;
      const port = (dir === 'in' ? c.inputs : c.outputs).find((p) => p.name === handleId);
      return port?.type;
    },
    [nodes],
  );

  const isValidConnection = useCallback(
    (c: Connection | Edge) => {
      const s = portType(c.source ?? '', c.sourceHandle ?? null, 'out');
      const t = portType(c.target ?? '', c.targetHandle ?? null, 'in');
      return !!s && s === t;
    },
    [portType],
  );

  const onConnect = useCallback(
    (c: Connection) => {
      if (!isValidConnection(c)) return;
      setEdges((eds) =>
        addEdge(
          {
            ...c,
            id: `e_${c.source}.${c.sourceHandle}->${c.target}.${c.targetHandle}`,
            type: 'smoothstep',
          },
          eds,
        ),
      );
    },
    [isValidConnection, setEdges],
  );

  const onAdd = useCallback(
    (c: NodeContract) => {
      addCount.current += 1;
      const id = `n_${Date.now()}_${addCount.current}`;
      const position = {
        x: 80 + (addCount.current % 4) * 70,
        y: 60 + (addCount.current % 5) * 60,
      };
      setNodes((nds) => [
        ...nds,
        { id, type: WF_NODE_TYPE, position, data: { contract: c, params: defaultParams(c) } },
      ]);
    },
    [setNodes],
  );

  const hasCycle = useCallback((): boolean => {
    const adj: Record<string, string[]> = {};
    edges.forEach((e) => (adj[e.source] = [...(adj[e.source] ?? []), e.target]));
    const state: Record<string, number> = {};
    const dfs = (u: string): boolean => {
      state[u] = 1;
      for (const v of adj[u] ?? []) {
        if (state[v] === 1) return true;
        if (state[v] === undefined && dfs(v)) return true;
      }
      state[u] = 2;
      return false;
    };
    return nodes.some((n) => state[n.id] === undefined && dfs(n.id));
  }, [nodes, edges]);

  const toGraph = useCallback(
    (): { name: string; nodes: GraphNode[]; edges: GraphEdge[] } => ({
      name,
      nodes: nodes.map((n) => ({
        id: n.id,
        type: n.data.contract.type,
        params: n.data.params,
        position: n.position,
      })),
      edges: edges.map((e) => ({
        id: e.id,
        from: e.source,
        fromPort: (e.sourceHandle as string) ?? '',
        to: e.target,
        toPort: (e.targetHandle as string) ?? '',
      })),
    }),
    [name, nodes, edges],
  );

  const onSave = async () => {
    if (hasCycle()) {
      setLog('⚠ 检测到环，无法保存（DAG 不允许环）');
      return;
    }
    setBusy(true);
    try {
      const g = await api.create(toGraph());
      setCurrentId(g.id ?? null);
      setLog('✓ 已保存，ID=' + (g.id ?? '?'));
    } catch (e: any) {
      setLog('保存失败: ' + e.message);
    } finally {
      setBusy(false);
    }
  };

  const onRun = async () => {
    if (!currentId) {
      setLog('请先保存再运行');
      return;
    }
    setBusy(true);
    try {
      const res = await api.run(currentId);
      setGeneratedPageId(res.generatedPageId ?? null);
      const tail = res.generatedPageId
        ? '\n✓ 已生成页面，可点「查看生成页面」'
        : '';
      setLog('✓ 运行完成\n' + JSON.stringify(res.result, null, 2) + tail);
    } catch (e: any) {
      setLog('运行失败: ' + e.message);
    } finally {
      setBusy(false);
    }
  };

  const onLoad = async (id: string) => {
    if (!id) return;
    try {
      const g: WorkflowGraph = await api.get(id);
      const ns: Node<RFNodeData>[] = (g.nodes ?? []).map((n) => ({
        id: n.id,
        type: WF_NODE_TYPE,
        position: n.position ?? { x: 0, y: 0 },
        data: {
          contract: contractByType.current[n.type] ?? fallbackContract(n.type),
          params: n.params ?? {},
        },
      }));
      const es: Edge[] = (g.edges ?? []).map((e) => ({
        id: e.id,
        source: e.from,
        sourceHandle: e.fromPort,
        target: e.to,
        targetHandle: e.toPort,
        type: 'smoothstep',
      }));
      setNodes(ns);
      setEdges(es);
      setName(g.name ?? '未命名工作流');
      setCurrentId(g.id ?? null);
      setLog('✓ 已加载 ' + (g.id ?? ''));
    } catch (e: any) {
      setLog('加载失败: ' + e.message);
    }
  };

  const cycle = hasCycle();

  return (
    <div style={{ display: 'flex', height: '100%' }}>
      <Palette contracts={contracts} onAdd={onAdd} />
      <div style={{ flex: 1, display: 'flex', flexDirection: 'column', minWidth: 0 }}>
        <div
          style={{
            display: 'flex',
            gap: 8,
            alignItems: 'center',
            padding: '8px 12px',
            borderBottom: '1px solid #eee',
          }}
        >
          <input value={name} onChange={(e) => setName(e.target.value)} style={{ padding: '4px 8px', width: 200 }} />
          <button onClick={onSave} disabled={busy}>
            保存
          </button>
          <button onClick={onRun} disabled={busy || !currentId}>
            运行
          </button>
          {generatedPageId && (
            <a
              href={api.pageRenderUrl(generatedPageId)}
              target="_blank"
              rel="noreferrer"
              style={{ textDecoration: 'none' }}
            >
              <button type="button" style={{ background: '#1677ff', color: '#fff', border: 'none' }}>
                查看生成页面
              </button>
            </a>
          )}
          <LoadSelect onLoad={onLoad} />
          <span style={{ color: '#999', fontSize: 12 }}>{currentId ? '已存 ' + currentId : '未保存'}</span>
          {cycle && <span style={{ color: '#cf1322', fontSize: 12 }}>⚠ 存在环</span>}
        </div>
        <div style={{ flex: 1, minHeight: 0 }}>
          <ReactFlow
            nodes={nodes}
            edges={edges}
            nodeTypes={nodeTypes}
            onNodesChange={onNodesChange}
            onEdgesChange={onEdgesChange}
            onConnect={onConnect}
            isValidConnection={isValidConnection}
            fitView
          >
            <Background />
            <Controls />
            <MiniMap />
          </ReactFlow>
        </div>
        <pre
          style={{
            margin: 0,
            maxHeight: 160,
            overflow: 'auto',
            padding: 12,
            background: '#1e1e1e',
            color: '#0f0',
            fontSize: 11,
            whiteSpace: 'pre-wrap',
          }}
        >
          {log}
        </pre>
      </div>
    </div>
  );
}

function LoadSelect({ onLoad }: { onLoad: (id: string) => void }) {
  const [items, setItems] = useState<WorkflowGraph[]>([]);
  const [open, setOpen] = useState(false);
  const refresh = () => api.list().then(setItems).catch(() => setItems([]));
  return (
    <span style={{ position: 'relative' }}>
      <button
        onClick={() => {
          setOpen((v) => !v);
          if (!open) refresh();
        }}
      >
        加载▾
      </button>
      {open && (
        <div
          style={{
            position: 'absolute',
            top: 28,
            left: 0,
            background: '#fff',
            border: '1px solid #ddd',
            borderRadius: 6,
            minWidth: 200,
            zIndex: 10,
            maxHeight: 240,
            overflow: 'auto',
          }}
        >
          {items.length === 0 && <div style={{ padding: 8, color: '#999', fontSize: 12 }}>暂无</div>}
          {items.map((g) => (
            <div
              key={g.id}
              onClick={() => {
                onLoad(g.id!);
                setOpen(false);
              }}
              style={{ padding: '6px 8px', cursor: 'pointer', borderBottom: '1px solid #f0f0f0' }}
            >
              {g.name} <code style={{ fontSize: 10, color: '#888' }}>{g.id}</code>
            </div>
          ))}
        </div>
      )}
    </span>
  );
}
