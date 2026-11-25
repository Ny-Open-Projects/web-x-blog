---
title: [RBL-849] 笔试：手写迁移 checklist 校验执行器（步骤执行 + 预期断言 + 断点续跑）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-849：笔试：手写迁移 checklist 校验执行器（执行 + 断言 + 续跑）

**需求**：实现 `runChecklist(steps, { runner, statePath })`。steps: `{ id, cmd, expect: (out) => boolean | { code, detail }, skipIf?: (state) => boolean }[]`。规则：1) 顺序执行，expect 失败 → 停止并返回 `{ ok: false, failedAt: id, detail }`；2) **断点续跑**：state 记录已完成 step id（持久化到 statePath——注入 store）；重跑时 skip 已完成；skipIf 命中跳过（记录 skipped）；3) runner 注入：`cmd -> Promise<{ out, exit }>`；4) 返回 `{ ok, completed: string[], skipped: string[] }`。边界：state 已全完成（全部 skip）；expect 非 boolean（对象带 code/detail）；steps 空。

```javascript
async function runChecklist(steps, { runner, store } = {}) {
  const done = new Set((await store?.load?.()) ?? []);
  const completed = [], skipped = [];
  for (const s of steps) {
    if (done.has(s.id)) { skipped.push(s.id); continue; }
    if (s.skipIf?.({ done: [...done] })) { skipped.push(s.id); done.add(s.id); continue; }
    const r = await runner(s.cmd);                       // 失败直接抛
    const exp = s.expect(r.out ?? r);
    const pass = exp === true || (exp && exp.code === 0);
    if (!pass) {
      await store?.save?.([...done]);
      return { ok: false, failedAt: s.id,
        detail: exp && exp.detail ? exp.detail : `输出不符: ${String(r.out ?? r).slice(0, 80)}`,
        completed, skipped };
    }
    done.add(s.id); completed.push(s.id);
    await store?.save?.([...done]);
  }
  return { ok: true, completed, skipped };
}

// 自测
const store = { mem: [], load: async () => [...this?.mem ?? []],
  save: async (ids) => { store.mem = ids; } };
store.load = async () => [...store.mem];

let calls = 0;
const runner = async (cmd) => { calls++;
  if (cmd.includes('build')) return { out: 'dist/manifest.json written', exit: 0 };
  if (cmd.includes('fail')) return { out: 'ERR', exit: 1 };
  return { out: 'ok', exit: 0 };
};
const steps = [
  { id: 'install', cmd: 'pnpm i', expect: () => true },
  { id: 'build', cmd: 'pnpm build', expect: (out) => out.includes('manifest') },
  { id: 'verify', cmd: 'node verify.mjs', expect: () => true },
];
let r = await runChecklist(steps, { runner, store });
console.log(r.ok === true && r.completed.join(',') === 'install,build,verify');

// 断点续跑：重跑全部 skip
r = await runChecklist(steps, { runner, store });
console.log(r.ok === true && r.skipped.join(',') === 'install,build,verify' && r.completed.length === 0);

// 失败停止
store.mem = [];
const bad = [...steps.slice(0, 1), { id: 'build', cmd: 'pnpm build-fail', expect: (out) => out.includes('manifest') }];
r = await runChecklist(bad, { runner, store });
console.log(r.ok === false && r.failedAt === 'build');

// skipIf
r = await runChecklist([{ id: 'a', cmd: 'x', expect: () => true, skipIf: () => true }], { runner, store });
console.log(r.skipped.join(',') === 'a');
```

**评分点**：
- 断点续跑正确（store 持久化、重跑 skip 已完成）；skipIf 独立跳过也记账
- expect 双形态（boolean / { code, detail }）；失败停止并带上下文（failedAt + detail）
- 每步成功即持久化（中途崩溃可续）；边界：空 steps
- 能说清「checklist 可校验化把『读文档验证』变成『跑命令验证』，断点续跑适配长迁移」属于加分
