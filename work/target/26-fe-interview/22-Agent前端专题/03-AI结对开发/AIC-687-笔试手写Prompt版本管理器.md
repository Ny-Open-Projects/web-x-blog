---
title: [AIC-687] 笔试：手写 Prompt 版本管理器
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-687：笔试：手写 Prompt 版本管理器

**答**：实现 `managePromptVersions(ops)`。ops: `{ op:'publish'|'render'|'rollback'|'compare', id:string, ... }[]`：
- publish: `{op, id, template, evalScore:number}` — 新增版本（版本号自增），仅当 evalScore ≥ 上一版本 evalScore×0.9（不允许明显退化）才发布成功，否则拒绝。
- render: `{op, id, vars:Record<string,string>, version?:number}` — 渲染模板（{var} 替换），默认最新版。
- rollback: `{op, id, version:number}` — 将「当前激活版本」设为指定版本。
- compare: `{op, id, v1:number, v2:number}` — 返回两版 template 差异（不同的变量名列表）。
返回 `{ results:any[], state:Record<string,{versions:Array<{v:number,template:string,score:number}>,active:number}> }`。边界：id 不存在时 render/rollback/compare 返回 error；publish 首个版本总是成功。

```javascript
function managePromptVersions(ops = []) {
  const state = {};
  const results = [];
  for (const op of ops) {
    const s = state[op.id] || (state[op.id] = { versions: [], active: 0 });
    if (op.op === 'publish') {
      const last = s.versions[s.versions.length - 1];
      if (last && op.evalScore < last.score * 0.9) {
        results.push({ error: 'regression-rejected', id: op.id, score: op.evalScore });
        continue;
      }
      const v = s.versions.length + 1;
      s.versions.push({ v, template: op.template, score: op.evalScore });
      s.active = v;
      results.push({ published: v, id: op.id });
    } else if (op.op === 'render') {
      const target = s.versions.find(x => x.v === (op.version ?? s.active));
      if (!target) { results.push({ error: 'version-not-found', id: op.id }); continue; }
      const rendered = target.template.replace(/\{(\w+)\}/g, (_, k) => op.vars?.[k] ?? `{${k}}`);
      results.push({ rendered, version: target.v });
    } else if (op.op === 'rollback') {
      if (!s.versions.find(x => x.v === op.version)) { results.push({ error: 'version-not-found' }); continue; }
      s.active = op.version;
      results.push({ active: op.version });
    } else if (op.op === 'compare') {
      const a = s.versions.find(x => x.v === op.v1), b = s.versions.find(x => x.v === op.v2);
      if (!a || !b) { results.push({ error: 'version-not-found' }); continue; }
      const vars = t => [...t.matchAll(/\{(\w+)\}/g)].map(m => m[1]);
      const va = new Set(vars(a.template)), vb = new Set(vars(b.template));
      const diff = [...new Set([...va, ...vb])].filter(k => va.has(k) !== vb.has(k));
      results.push({ diff });
    }
  }
  return { results, state };
}

// 自测
const ops = [
  { op: 'publish', id: 'p1', template: '写{thing}的描述', evalScore: 0.8 },
  { op: 'publish', id: 'p1', template: '根据{ctx}写{thing}', evalScore: 0.5 }, // 明显退化，拒绝
  { op: 'publish', id: 'p1', template: '根据{ctx}和{extra}写{thing}', evalScore: 0.85 },
  { op: 'render', id: 'p1', vars: { ctx: 'c', thing: 'PR', extra: 'i' } },
  { op: 'rollback', id: 'p1', version: 1 },
  { op: 'compare', id: 'p1', v1: 1, v2: 2 },
];
const r = managePromptVersions(ops);
console.log(r.state.p1.versions.length === 2); // 第二个被拒
console.log(r.results[1].error === 'regression-rejected');
console.log(r.state.p1.active === 1); // 回滚生效
console.log(r.results[5].diff.includes('ctx'));
```

**评分点**：
- publish 版本号自增与退化拒绝（evalScore < 上版×0.9）
- render 变量替换（{var}）与默认激活版本
- rollback 改 active 版本，compare 找差异变量名
- 错误分支（版本不存在/退化拒绝）正确返回
- 能说清「prompt 像代码一样版本化，且每次修改必须跑评测防退化——评测是版本管理的灵魂」属于加分
