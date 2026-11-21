// M4 集成冒烟（基于 nest build 产物，不依赖 MySQL）。
// 运行：node apps/server/test/e2e-m4.cjs
const path = require('path');
const base = path.resolve(__dirname, '../dist/modules/workflow');
const { runDag } = require(path.join(base, 'engine/dag.js'));
const { NODE_REGISTRY } = require(path.join(base, 'nodes/registry.js'));

(async () => {
  const audits = [];
  const ctx = {
    tenantId: 't_demo',
    runId: 'run_smoke',
    caller: 'test',
    audit: async (e) => {
      audits.push(e);
    },
  };

  const graph = {
    nodes: [
      { id: 'n1', type: 'trigger.formSubmit', params: { formId: 'f1', data: { name: '小王', amount: 100 } } },
      { id: 'n2', type: 'script.eval', params: { code: "setOutput({ name: data.data.name, level: data.data.amount > 50 ? 'HIGH' : 'LOW' })" } },
      { id: 'n3', type: 'ai.llm', params: { prompt: '请审批：{{data.name}} 申请等级 {{data.level}}', model: 'mock' } },
      { id: 'n4', type: 'ui.composePage', params: { title: '审批结果-{{data.level}}', components: [{ type: 'text', options: { text: '结论：{{data.level}}' } }] } },
    ],
    edges: [
      { from: 'n1', fromPort: 'out', to: 'n2', toPort: 'in' },
      { from: 'n2', fromPort: 'out', to: 'n3', toPort: 'in' },
      { from: 'n2', fromPort: 'out', to: 'n4', toPort: 'source' },
    ],
  };

  const result = await runDag(graph, NODE_REGISTRY, ctx);
  let ok = 0, bad = 0;
  const assert = (name, cond, extra = '') => { cond ? (ok++, console.log('  ✅', name, extra)) : (bad++, console.log('  ❌', name, extra)); };

  assert('script.eval 输出正确', JSON.stringify(result.n2.out) === JSON.stringify({ name: '小王', level: 'HIGH' }));
  assert('ai.llm 返回文本', typeof result.n3.out.text === 'string' && result.n3.out.text.length > 0);
  assert('composePage 标题注入生效', result.n4.page.title === '审批结果-HIGH');
  assert('审计记录含 script.eval', audits.some((a) => a.nodeType === 'script.eval' && a.status === 'success'));
  assert('审计记录含 ai.llm', audits.some((a) => a.nodeType === 'ai.llm' && a.status === 'success'));
  assert('审计带 nodeId', audits.every((a) => a.nodeId && a.nodeId.length > 0));
  assert('审计带 tenantId', audits.every((a) => a.tenantId === 't_demo'));

  console.log(`\n集成冒烟：${ok} 通过 / ${bad} 失败`);
  process.exit(bad > 0 ? 1 : 0);
})().catch((e) => { console.error('冒烟异常:', e); process.exit(1); });
