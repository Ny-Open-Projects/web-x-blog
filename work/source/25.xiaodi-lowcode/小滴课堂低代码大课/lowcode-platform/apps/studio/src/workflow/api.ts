import type { NodeContract, GraphNode, GraphEdge, WorkflowGraph } from '@lowcode/shared';

const BASE = '/api/workflow';

interface RunResult {
  runId: string;
  generatedPageId?: string;
  result: Record<string, Record<string, unknown>>;
}

async function http<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...(init?.headers ?? {}) },
  });
  if (!r.ok) throw new Error(`${init?.method ?? 'GET'} ${url} -> ${r.status}`);
  return (await r.json()) as T;
}

export const api = {
  nodes: () => http<NodeContract[]>(`${BASE}/nodes`),
  list: () => http<WorkflowGraph[]>(`${BASE}`),
  get: (id: string) => http<WorkflowGraph>(`${BASE}/${id}`),
  create: (g: { name: string; nodes: GraphNode[]; edges: GraphEdge[] }) =>
    http<WorkflowGraph>(`${BASE}`, { method: 'POST', body: JSON.stringify(g) }),
  run: (id: string, trigger?: unknown) =>
    http<RunResult>(`${BASE}/${id}/run`, {
      method: 'POST',
      body: JSON.stringify({ trigger: trigger ?? null }),
    }),
  pageRenderUrl: (pageId: string) => `${BASE}/pages/${pageId}/render`,
};
