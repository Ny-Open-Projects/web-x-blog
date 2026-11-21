/**
 * M9 嵌套组件 E2E（连真实 MySQL + 运行中的 server）：
 *  - 创建含"表单 → 输入框/下拉框"、"栅格 → 容器 → 文本"的多层嵌套页面
 *  - 渲染 HTML 必须体现真实嵌套层级（form > input、grid > container > p）
 *  - 栅格列数生效
 *  - 子组件增删改后落库再读回一致
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

const schema = {
  version: 1,
  title: '嵌套页面验证',
  nodes: [
    {
      id: 'f1',
      type: 'form',
      options: { submitLabel: '提交申请', formId: 'form_nested_1' },
      children: [
        { id: 'f1_i1', type: 'input', options: { label: '姓名', placeholder: '请输入姓名', required: true } },
        {
          id: 'f1_s1',
          type: 'select',
          options: { label: '部门', options: [{ label: '技术', value: 'tech' }, { label: '市场', value: 'mkt' }] },
        },
      ],
    },
    {
      id: 'g1',
      type: 'grid',
      options: { columns: 2 },
      children: [
        {
          id: 'g1_c1',
          type: 'container',
          options: { label: '说明区' },
          children: [{ id: 'g1_c1_t1', type: 'text', options: { text: '这是三层嵌套的文本' } }],
        },
        { id: 'g1_b1', type: 'button', options: { label: '确认' } },
      ],
    },
  ],
};

console.log('=== M9 嵌套组件 E2E ===');

async function main() {
const created = await req('POST', `${BASE}/pages`, { name: '嵌套页面验证', schema });
assert('创建页面返回 201', created.status === 201, `status=${created.status} body=${JSON.stringify(created.body).slice(0, 200)}`);
const pageId = created.body?.id;

if (!pageId) {
  console.log('\n===== M9 结果：0 通过 / 1 失败 =====');
  process.exit(1);
}

const rendered = await req('GET', `${BASE}/pages/${pageId}/render`);
assert('渲染返回 200', rendered.status === 200, `status=${rendered.status}`);
const html = rendered.text;

assert('含 form 容器', /<form class="lc-form"/.test(html));
assert('form 内含 input（子组件下钻）', /<form class="lc-form"[\s\S]*<input name="f1_i1"/.test(html));
assert('form 内含 select 子组件', /<form class="lc-form"[\s\S]*<select name="f1_s1"/.test(html));
assert('栅格容器存在', /<div class="lc-grid"/.test(html));
assert('栅格列数生效', /grid-template-columns:repeat\(2,1fr\)/.test(html), (html.match(/grid-template-columns[^"]*/) || [''])[0]);
assert('栅格内含 container', /<div class="lc-grid"[\s\S]*<div class="lc-container"/.test(html));
assert('三层嵌套：container 内含文本', /<div class="lc-container"[\s\S]*<p class="lc-text">这是三层嵌套的文本<\/p>/.test(html));
assert('提交按钮文字生效', /提交申请/.test(html));
assert('下拉选项渲染', /<option value="tech">技术<\/option>/.test(html));
assert('必填标记生效', /name="f1_i1"[^>]*required/.test(html));

// 读回验证落库
const fetched = await req('GET', `${BASE}/pages/${pageId}`);
assert('读回成功', fetched.status === 200);
const saved = JSON.parse(fetched.body.schemaJson);
assert('落库保留 children 层级', saved.nodes?.[0]?.children?.length === 2, `children=${saved.nodes?.[0]?.children?.length}`);
assert('落库保留三层嵌套', saved.nodes?.[1]?.children?.[0]?.children?.[0]?.id === 'g1_c1_t1');

// 更新：删除一个子组件
const mutated = JSON.parse(JSON.stringify(saved));
mutated.nodes[0].children = mutated.nodes[0].children.filter((c) => c.id !== 'f1_s1');
const upd = await req('PUT', `${BASE}/pages/${pageId}`, { name: '嵌套页面验证', schema: mutated });
assert('更新返回 200', upd.status === 200, `status=${upd.status}`);
const after = JSON.parse((await req('GET', `${BASE}/pages/${pageId}`)).body.schemaJson);
assert('子组件删除已持久化', after.nodes[0].children.length === 1 && after.nodes[0].children[0].id === 'f1_i1');

const html2 = (await req('GET', `${BASE}/pages/${pageId}/render`)).text;
assert('重新渲染不再含已删 select', !/name="f1_s1"/.test(html2));

console.log(`\n===== M9 结果：${ok} 通过 / ${bad} 失败 =====`);
process.exit(bad ? 1 : 0);
}

main().catch((e) => {
  console.error('测试异常:', e);
  process.exit(1);
});
