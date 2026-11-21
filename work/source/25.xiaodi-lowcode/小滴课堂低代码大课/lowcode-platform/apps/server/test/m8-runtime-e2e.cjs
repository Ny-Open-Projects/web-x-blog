/**
 * M8 运行时 E2E（连真实 MySQL + 运行中的 server，server 以 WF_SANDBOX_MODE=container 启动）：
 *  - 通过 REST API 建图并运行含 script.eval 的工作流
 *  - 审计落库且 isolation='container'（证明硬隔离真的接管了业务链路）
 *  - 页面生成与渲染不受隔离层切换影响
 */
const BASE = 'http://127.0.0.1:3000/api';

let ok = 0;
let bad = 0;
const assert = (name, cond, extra = '') => {
  cond ? (ok++, console.log('  ✅', name, extra)) : (bad++, console.log('  ❌', name, extra));
};

async function req(method, url, body, headers = {}) {
  const r = await fetch(url, {
    method,
    headers: { 'Content-Type': 'application/json', ...headers },
    body: body ? JSON.stringify(body) : undefined,
  });
  const text = await r.text();
  let json;
  try {
    json = JSON.parse(text);
  } catch {
    json = text;
  }
  return { status: r.status, body: json, text };
}

async function main() {
  console.log('=== M8 运行时 E2E（container 隔离层）===');

  const TENANT = 't_m8';
  const headers = { 'x-tenant-id': TENANT };

  const graph = {
    name: 'M8容器隔离验证',
    nodes: [
      { id: 'n1', type: 'trigger.formSubmit', params: { formId: 'f_m8', data: { name: '小李', amount: 200 } }, position: { x: 0, y: 0 } },
      { id: 'n2', type: 'script.eval', params: { code: "setOutput({ name: data.data.name, level: data.data.amount > 100 ? 'HIGH' : 'LOW' })" }, position: { x: 200, y: 0 } },
      { id: 'n3', type: 'ui.composePage', params: { title: 'M8结果页-{{data.level}}', components: [{ type: 'text', options: { text: '级别：{{data.level}}' } }] }, position: { x: 400, y: 0 } },
    ],
    edges: [
      { id: 'e1', from: 'n1', fromPort: 'out', to: 'n2', toPort: 'in' },
      { id: 'e2', from: 'n2', fromPort: 'out', to: 'n3', toPort: 'source' },
    ],
  };

  const created = await req('POST', `${BASE}/workflow`, graph, headers);
  assert('建图成功', created.status === 201 || created.status === 200, `status=${created.status} body=${JSON.stringify(created.body).slice(0, 200)}`);
  const graphId = created.body?.id ?? created.body?.graph?.id;

  const run = await req('POST', `${BASE}/workflow/${graphId}/run`, { trigger: 'manual' }, headers);
  assert('运行成功', run.status === 201 || run.status === 200, `status=${run.status} body=${JSON.stringify(run.body).slice(0, 300)}`);
  const runId = run.body?.runId ?? run.body?.id ?? run.body?.run?.id;
  const generatedPageId = run.body?.generatedPageId;

  const audit = await req('GET', `${BASE}/workflow/audit`, undefined, headers);
  assert('审计查询成功', audit.status === 200, `status=${audit.status}`);
  const list = Array.isArray(audit.body) ? audit.body : audit.body?.items ?? [];
  const mine = list.filter((a) => a.runId === runId);
  const scriptAudit = mine.find((a) => a.nodeType === 'script.eval');
  assert('审计含本次运行的 script.eval', !!scriptAudit, `本次审计条目=${mine.length} 总条目=${list.length}`);
  assert('审计 isolation=container（硬隔离接管）', scriptAudit?.isolation === 'container', `isolation=${scriptAudit?.isolation}`);
  assert('审计状态成功', scriptAudit?.status === 'success', `status=${scriptAudit?.status}`);
  assert('审计含脚本哈希（不存明文）', typeof scriptAudit?.codeHash === 'string' && scriptAudit.codeHash.length === 64, `hash=${scriptAudit?.codeHash}`);
  assert('审计不含脚本明文', !JSON.stringify(scriptAudit).includes('setOutput'), '明文泄露！');

  const pages = await req('GET', `${BASE}/workflow/pages`, undefined, headers);
  const plist = Array.isArray(pages.body) ? pages.body : pages.body?.items ?? [];
  const page =
    plist.find((p) => p.id === generatedPageId) ||
    plist.find((p) => String(p.schemaJson ?? '').includes('M8结果页'));
  assert('生成页面已持久化', !!page, `pages=${plist.length} generatedPageId=${generatedPageId}`);
  if (page) {
    const html = (await req('GET', `${BASE}/workflow/pages/${page.id}/render`, undefined, headers)).text;
    assert('渲染含动态标题（脚本输出注入成功）', /M8结果页-HIGH/.test(html), (html.match(/M8结果页-\w+/) || [''])[0]);
    assert('渲染含脚本计算结果', /级别：HIGH/.test(html), '');
  }

  console.log(`\n===== M8 运行时 E2E：${ok} 通过 / ${bad} 失败 =====`);
  process.exit(bad ? 1 : 0);
}

main().catch((e) => {
  console.error('测试异常:', e);
  process.exit(1);
});
