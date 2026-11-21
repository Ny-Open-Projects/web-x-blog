import { NodeContract, PortDef, PageSchema, ComponentNode, ComponentType } from '@lowcode/shared';
import { NodeExecutor, NodeDef, ExecCtx, AuditEntry } from '../engine/dag';
import { WorkflowServices, DEFAULT_SERVICES } from './providers';
import { sha256, SANDBOX_CONFIG } from './sandbox';
import { executeWithFallback } from './container-sandbox';
import { createLlmProvider } from './llm';

const p = (name: string, type: any): PortDef => ({ name, type });

/**
 * 节点契约目录：前端画布与后端引擎共用同一份定义（见 06 设计 §2）。
 * M3：节点即平台已有能力的可编排封装，执行逻辑已真实化。
 */
export const NODE_CONTRACTS: NodeContract[] = [
  { type: 'trigger.formSubmit', category: 'trigger', label: '表单提交触发', version: 1, inputs: [], outputs: [p('out', 'data')] },
  { type: 'transform.map', category: 'transform', label: '映射变换', version: 1, inputs: [p('in', 'data')], outputs: [p('out', 'data')] },
  { type: 'ui.composePage', category: 'ui', label: '组合页面', version: 1, inputs: [p('source', 'data')], outputs: [p('page', 'schema')] },
  { type: 'action.sendSms', category: 'action', label: '发送短信', version: 1, inputs: [p('ctx', 'schema')], outputs: [p('out', 'data')] },
  { type: 'action.ossUpload', category: 'action', label: '上传到OSS', version: 1, inputs: [p('in', 'data')], outputs: [p('out', 'data')] },
  { type: 'script.eval', category: 'script', label: '沙箱脚本', version: 1, inputs: [p('in', 'data')], outputs: [p('out', 'data')] },
  { type: 'ai.llm', category: 'ai', label: '大模型调用', version: 1, inputs: [p('in', 'data')], outputs: [p('out', 'data')] },
];

/** 把高风险节点（脚本/大模型）的执行结果写入审计。 */
async function auditNode(ctx: ExecCtx, nodeType: string, e: Omit<AuditEntry, 'tenantId' | 'runId' | 'nodeId' | 'nodeType'>) {
  if (!ctx.audit) return;
  await ctx.audit({
    tenantId: ctx.tenantId,
    runId: ctx.runId,
    nodeId: ctx.currentNodeId ?? '',
    nodeType,
    ...e,
  });
}

/** 把字符串里的 "{{data.x.y}}" 用上游数据替换。 */
export function renderTemplate(tpl: unknown, data: any): any {
  if (typeof tpl === 'string') {
    return tpl.replace(/\{\{\s*data\.([\w.]+)\s*\}\}/g, (_, path) => {
      const v = path.split('.').reduce((o: any, k: string) => (o == null ? undefined : o[k]), data);
      return v === undefined ? '' : String(v);
    });
  }
  if (Array.isArray(tpl)) return tpl.map((x) => renderTemplate(x, data));
  if (tpl && typeof tpl === 'object') {
    const out: any = {};
    for (const [k, v] of Object.entries(tpl)) out[k] = renderTemplate(v, data);
    return out;
  }
  return tpl;
}

let _cseq = 0;
function buildComponent(c: any, data: any): ComponentNode {
  const id = `n${++_cseq}`;
  const opts: any = { ...(c.options ?? {}) };
  for (const f of ['text', 'label', 'placeholder', 'submitLabel', 'src', 'title']) {
    if (typeof opts[f] === 'string') opts[f] = renderTemplate(opts[f], data);
  }
  const base: any = { id, type: (c.type ?? 'text') as ComponentType, options: opts };
  if (Array.isArray(c.children)) base.children = c.children.map((ch: any) => buildComponent(ch, data));
  return base;
}

function getPath(o: any, pth: string): any {
  return pth.split('.').reduce((a, k) => (a == null ? undefined : a[k]), o);
}
function setPath(o: any, pth: string, v: any): void {
  const ks = pth.split('.');
  let cur = o;
  for (let i = 0; i < ks.length - 1; i++) {
    if (cur[ks[i]] == null) cur[ks[i]] = {};
    cur = cur[ks[i]];
  }
  cur[ks[ks.length - 1]] = v;
}

const execs: Record<string, NodeExecutor> = {
  'trigger.formSubmit': async (inputs, params, ctx) => {
    const formId = String(params['formId'] ?? 'form_default');
    const data = ((inputs['out'] as any) ?? params['data'] ?? {}) as Record<string, unknown>;
    const svc: WorkflowServices = ctx.services ?? DEFAULT_SERVICES;
    const rec = await svc.formStore.save({ formId, data, tenantId: ctx.tenantId });
    return { out: { formId, submissionId: rec.id, data: rec.data } };
  },

  'transform.map': async (inputs, params) => {
    const src = ((inputs['in'] as any) ?? {}) as Record<string, unknown>;
    const op = String(params['op'] ?? 'passthrough');
    switch (op) {
      case 'setField': {
        const cp = { ...src };
        setPath(cp, String(params['field']), params['value']);
        return { out: cp };
      }
      case 'pick': {
        const fields = (params['fields'] as string[]) ?? [];
        const out: Record<string, unknown> = {};
        for (const f of fields) out[f] = src[f];
        return { out };
      }
      case 'pickTo': {
        const out = { ...src };
        setPath(out, String(params['to']), getPath(src, String(params['from'])));
        return { out };
      }
      case 'concat':
        return { out: String(params['prefix'] ?? '') + JSON.stringify(src) + String(params['suffix'] ?? '') };
      default:
        return { out: src };
    }
  },

  'ui.composePage': async (inputs, params) => {
    const data = ((inputs['source'] as any) ?? {}) as Record<string, unknown>;
    const title = String(renderTemplate(params['title'] ?? '未命名页面', data));
    const components = ((params['components'] as any[]) ?? []).map((c) => buildComponent(c, data));
    const page: PageSchema = { version: 1, title, nodes: components, meta: { generatedBy: 'workflow' } };
    return { page };
  },

  'action.sendSms': async (inputs, params, ctx) => {
    const svc: WorkflowServices = ctx.services ?? DEFAULT_SERVICES;
    const data = ((inputs['ctx'] as any) ?? {}) as Record<string, unknown>;
    const res = await svc.sms.send({
      phone: String(params['phone'] ?? ''),
      template: String(params['template'] ?? 'PAGE_READY'),
      params: { pageTitle: data?.title ?? '' },
    });
    return { out: { sent: res.ok, provider: res.provider } };
  },

  'action.ossUpload': async (inputs, params, ctx) => {
    const svc: WorkflowServices = ctx.services ?? DEFAULT_SERVICES;
    const data = ((inputs['in'] as any) ?? {}) as Record<string, unknown>;
    const res = await svc.oss.upload({
      key: String(params['key'] ?? `wf/${Date.now()}.bin`),
      content: typeof data === 'string' ? data : JSON.stringify(data),
    });
    return { out: { url: res.url, key: res.key } };
  },

  // ---- M4：高风险节点（沙箱隔离 + 审计）----

  'script.eval': async (inputs, params, ctx) => {
    const code = String(params['code'] ?? '');
    const bag = ((inputs['in'] as any) ?? params['data'] ?? {}) as Record<string, unknown>;
    const res = await executeWithFallback(code, bag, SANDBOX_CONFIG);
    await auditNode(ctx, 'script.eval', {
      codeHash: sha256(code),
      durationMs: res.durationMs,
      status: res.status,
      errorMessage: res.fallbackReason ? `${res.error ?? ''} | ${res.fallbackReason}`.trim() : res.error,
      outputBytes: res.outputBytes,
      isolation: res.isolation,
    });
    if (res.status !== 'success') {
      throw new Error(`脚本节点失败[${res.status}]: ${res.error ?? ''}`);
    }
    return { out: res.out };
  },

  'ai.llm': async (inputs, params, ctx) => {
    const data = ((inputs['in'] as any) ?? {}) as Record<string, unknown>;
    const prompt = String(renderTemplate(params['prompt'] ?? JSON.stringify(data), data));
    const llm = createLlmProvider();
    const t0 = Date.now();
    const r = await llm.complete([{ role: 'user', content: prompt }], {
      model: params['model'] as string | undefined,
      temperature: Number(params['temperature'] ?? 0.7),
      maxTokens: Number(params['maxTokens'] ?? 512),
    });
    const dt = Date.now() - t0;
    await auditNode(ctx, 'ai.llm', {
      codeHash: sha256(prompt),
      durationMs: dt,
      status: 'success',
      outputBytes: Buffer.byteLength(r.text, 'utf8'),
    });
    return { out: { text: r.text, model: r.model, usage: r.usage } };
  },
};

export const NODE_REGISTRY: Record<string, NodeDef> = Object.fromEntries(
  NODE_CONTRACTS.map((c) => [c.type, { contract: c, exec: execs[c.type] ?? (async () => ({})) }]),
);
