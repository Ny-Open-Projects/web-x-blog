import type { PageSchema, ComponentNode } from '@lowcode/shared';

const BASE = '/api/pages';

interface PageDefDto {
  id: string;
  name: string;
  tenantId?: string | null;
  schemaJson?: string;
  createdAt?: string;
  updatedAt?: string;
}

async function http<T>(url: string, init?: RequestInit): Promise<T> {
  const r = await fetch(url, {
    ...init,
    headers: { 'Content-Type': 'application/json', ...(init?.headers ?? {}) },
  });
  if (!r.ok) throw new Error(`${init?.method ?? 'GET'} ${url} -> ${r.status}`);
  return (await r.json()) as T;
}

export const pageApi = {
  list: () => http<PageDefDto[]>(`${BASE}`),
  get: (id: string) => http<PageDefDto>(`${BASE}/${id}`),
  create: (name: string, schema: PageSchema) =>
    http<PageDefDto>(`${BASE}`, { method: 'POST', body: JSON.stringify({ name, schema }) }),
  update: (id: string, name: string, schema: PageSchema) =>
    http<PageDefDto>(`${BASE}/${id}`, { method: 'PUT', body: JSON.stringify({ name, schema }) }),
  renderUrl: (id: string) => `${BASE}/${id}/render`,
};

export type { PageDefDto };
