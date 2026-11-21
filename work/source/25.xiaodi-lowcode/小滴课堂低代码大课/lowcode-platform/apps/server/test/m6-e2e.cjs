// M6 真实运行时 E2E（需先起 server 连 MySQL）。
// 运行：node apps/server/test/m6-e2e.cjs
const BASE = 'http://127.0.0.1:3000/api';
const TENANT = 't_demo';
const OTHER = 't_other';

(async () => {
  const headers = (t) => ({ 'content-type': 'application/json', 'x-tenant-id': t });
  let ok = 0, bad = 0;
  const assert = (name, cond, extra = '') => { cond ? (ok++, console.log('  ✅', name, extra)) : (bad++, console.log('  ❌', name, extra)); };

  const graph = {
    name: 'M6-E2E-审批流',
    nodes: [
      { id: 'n1', type: 'trigger.formSubmit', params: { formId: 'f_apply', data: { name: '小王', amount: 120 } } },
      { id: 'n2', type: 'script.eval', params: { code: "setOutput({ name: data.data.name, level: data.data.amount > 50 ? 'HIGH' : 'LOW' })" } },
      { id: 'n3', type: 'ai.llm', params: { prompt: '请审批：{{data.name}} 等级 {{data.level}}', model: 'mock' } },
      { id: 'n4', type: 'ui.composePage', params: { title: '审批结果-{{data.level}}', components: [{ type: 'text', options: { text: '结论：{{data.level}}' } }] } },
    ],
    edges: [
      { id: 'e1', from: 'n1', fromPort: 'out', to: 'n2', toPort: 'in' },
      { id: 'e2', from: 'n2', fromPort: 'out', to: 'n3', toPort: 'in' },
      { id: 'e3', from: 'n2', fromPort: 'out', to: 'n4', toPort: 'source' },
    ],
  };

  console.log('== M6 真实运行时 E2E ==');
  const create = await fetch(`${BASE}/workflow`, { method: 'POST', headers: headers(TENANT), body: JSON.stringify(graph) }).then((r) => r.json());
  assert('创建工作流', !!create.id, create.id ? `-> ${create.id}` : JSON.stringify(create).slice(0, 200));
  const id = create.id;

  const run = await fetch(`${BASE}/workflow/${id}/run`, { method: 'POST', headers: headers(TENANT), body: JSON.stringify({ trigger: 'manual' }) }).then((r) => r.json());
  assert('运行成功', !!run.runId, run.runId ? `-> ${run.runId}` : JSON.stringify(run).slice(0, 200));
  assert('脚本产出 level=HIGH', run.result?.n2?.out?.level === 'HIGH', `-> ${JSON.stringify(run.result?.n2?.out)}`);
  assert('LLM 节点产出文本', typeof run.result?.n3?.out?.text === 'string' && run.result.n3.out.text.length > 0);
  assert('生成页面已持久化', !!run.generatedPageId, `pageId=${run.generatedPageId}`);

  // 审计落库（DB）
  const audit = await fetch(`${BASE}/workflow/audit`, { headers: headers(TENANT) }).then((r) => r.json());
  const types = audit.map((a) => a.nodeType);
  assert('审计含 script.eval', types.includes('script.eval'));
  assert('审计含 ai.llm', types.includes('ai.llm'));
  assert('审计均带租户', audit.every((a) => a.tenantId === TENANT));

  // 统计
  const stats = await fetch(`${BASE}/workflow/stats`, { headers: headers(TENANT) }).then((r) => r.json());
  assert('统计 total>=1', (stats.total ?? 0) >= 1, `-> ${JSON.stringify(stats)}`);

  // 页面渲染
  if (run.generatedPageId) {
    const html = await fetch(`${BASE}/workflow/pages/${run.generatedPageId}/render`).then((r) => r.text());
    assert('页面 HTML 含标题', html.includes('审批结果-HIGH'), `len=${html.length}`);
  }

  // 表单真实落库（直查 MySQL，mysql2 由 TypeORM 依赖提供）
  const { createConnection } = require('mysql2/promise');
  const conn = await createConnection({ host: '127.0.0.1', port: 3306, user: 'lowcode', password: 'change_me', database: 'lowcode' });
  const [rows] = await conn.query('SELECT COUNT(*) AS c FROM wf_submission');
  await conn.end();
  assert('表单提交真实落库 wf_submission', rows[0].c >= 1, `-> count=${rows[0].c}`);

  // 租户隔离：用其他租户头访问同图应被拒
  const forbidden = await fetch(`${BASE}/workflow/${id}`, { headers: headers(OTHER) });
  assert('跨租户访问被拒(403)', forbidden.status === 403, `-> ${forbidden.status}`);

  console.log(`\n结果：${ok} 通过 / ${bad} 失败`);
  process.exit(bad > 0 ? 1 : 0);
})().catch((e) => { console.error('E2E 异常:', e); process.exit(1); });
