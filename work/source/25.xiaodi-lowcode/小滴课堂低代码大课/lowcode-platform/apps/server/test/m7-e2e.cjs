// M7 真实运行时 E2E：可视化页面 CRUD + 渲染 + 租户隔离
const BASE = 'http://127.0.0.1:3000/api/pages';

const schema = {
  version: 1,
  title: 'M7 测试页',
  nodes: [
    { id: 'c1', type: 'text', options: { text: '欢迎使用低代码平台' } },
    { id: 'c2', type: 'input', options: { label: '姓名', placeholder: '请输入姓名', required: true } },
    { id: 'c3', type: 'button', options: { label: '提交' } },
  ],
};

function req(url, init, tenant) {
  const h = { 'Content-Type': 'application/json', ...(init?.headers ?? {}) };
  if (tenant) h['x-tenant-id'] = tenant;
  return fetch(url, { ...init, headers: h });
}

(async () => {
  let ok = 0, bad = 0;
  const assert = (name, cond, extra = '') => {
    cond ? (ok++, console.log('  ✅', name, extra)) : (bad++, console.log('  ❌', name, extra));
  };

  // 1. 创建（带租户 A）
  const createRes = await req(BASE, { method: 'POST', body: JSON.stringify({ name: 'M7 测试页', schema }) }, 'tenant-A');
  const created = await createRes.json();
  assert('创建页面 HTTP 201', createRes.status === 201 || createRes.status === 200, `status=${createRes.status}`);
  const pid = created.id;
  assert('返回页面 ID', typeof pid === 'string' && pid.length > 0, pid);

  // 2. 渲染 HTML（含标题与组件）
  const renderRes = await req(`${BASE}/${pid}/render`, {}, 'tenant-A');
  const html = await renderRes.text();
  assert('渲染返回 HTML', renderRes.headers.get('content-type')?.includes('text/html'), renderRes.headers.get('content-type'));
  assert('HTML 含页面标题', html.includes('M7 测试页'), '');
  assert('HTML 含文本组件', html.includes('欢迎使用低代码平台'), '');
  assert('HTML 含输入框 label', html.includes('姓名'), '');
  assert('HTML 含按钮', html.includes('提交'), '');

  // 3. 同一租户读取成功
  const getRes = await req(`${BASE}/${pid}`, {}, 'tenant-A');
  assert('同租户可读取', getRes.status === 200, `status=${getRes.status}`);

  // 4. 跨租户读取被拒(403)
  const crossRes = await req(`${BASE}/${pid}`, {}, 'tenant-B');
  assert('跨租户访问被拒(403)', crossRes.status === 403, `status=${crossRes.status}`);

  // 5. 无租户列表可见
  const listRes = await req(BASE, {}, null);
  const list = await listRes.json();
  assert('列表接口可用', Array.isArray(list), `count=${(list || []).length}`);
  assert('列表含刚建页面', (list || []).some((p) => p.id === pid), '');

  console.log(`\n结果：${ok} 通过 / ${bad} 失败`);
  process.exit(bad ? 1 : 0);
})().catch((e) => { console.error('E2E 异常:', e); process.exit(1); });
