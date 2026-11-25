---
title: [RBL-611] 笔试：手写 transform 管线调度器（过滤 + 分层排序 + 错误上下文）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-611：笔试：手写 transform 管线调度器（过滤 + 分层排序 + 错误上下文）

**需求**：实现 `createPipeline()`：`use(pass)` 注册 pass `{ name, layer: 'syntax'|'type'|'target', filter(id)->bool, run(ast, mod)->ast }`；`run(mod)` 按 layer 顺序 syntax→type→target（同层按注册序）执行 `filter` 命中的 pass，返回 `{ ast, applied, profile }`（profile 记录 pass 名与耗时）。pass 抛错时抛出带 `{ pass, module }` 上下文的错误（原错误保留在 cause）；无 pass 命中时 applied 为空但 run 正常完成。边界：layer 非法值抛错；重复注册同名 pass 抛错。

```javascript
const LAYERS = { syntax: 0, type: 1, target: 2 };
function createPipeline() {
  const passes = [];
  return {
    use(pass) {
      if (!(pass.layer in LAYERS)) throw new Error(`非法 layer: ${pass.layer}`);
      if (passes.some(p => p.name === pass.name)) throw new Error(`重复 pass: ${pass.name}`);
      passes.push(pass);
    },
    async run(mod) {
      const ordered = [...passes].sort((a, b) =>
        LAYERS[a.layer] - LAYERS[b.layer]);              // 分层排序，同层保持注册序（稳定排序）
      const applied = [], profile = [];
      let ast = mod.ast;
      for (const pass of ordered) {
        if (!pass.filter(mod.id)) continue;              // 过滤
        const t0 = performance.now();
        try {
          ast = await pass.run(ast, mod);
        } catch (e) {
          const err = new Error(`[pipeline] pass=${pass.name} module=${mod.id}: ${e.message}`);
          err.cause = e;                                 // 原错误保留
          throw err;
        }
        applied.push(pass.name);
        profile.push({ pass: pass.name, ms: +(performance.now() - t0).toFixed(3) });
      }
      return { ast, applied, profile };
    },
  };
}

// 自测
const pipe = createPipeline();
pipe.use({ name: 'downlevel', layer: 'target', filter: () => true, run: (a) => ({ ...a, step: 'down' }) });
pipe.use({ name: 'jsx', layer: 'syntax', filter: (id) => /\.jsx$/.test(id), run: (a) => ({ ...a, jsx: true }) });
pipe.use({ name: 'strip-ts', layer: 'type', filter: () => true, run: (a) => ({ ...a, ts: 'stripped' }) });

const r1 = await pipe.run({ id: 'a.tsx', ast: {} });
// 断言：applied = ['strip-ts', 'downlevel']（type 层先于 target；jsx 被过滤？tsx 也应命中 jsx filter —— filter 设计 /\.jsx$/ 不含 tsx，验证过滤生效）
console.log(r1.applied.join(','));
const r2 = await pipe.run({ id: 'b.jsx', ast: {} });
// 断言：applied = ['jsx', 'downlevel']
console.log(r2.applied.join(','));

pipe.use({ name: 'bad', layer: 'wrong', filter: () => true, run: () => {} });
// 断言：抛非法 layer
let e1; try { createPipeline().use({ name: 'jsx', layer: 'syntax', filter: () => 1, run: () => {} }); }
catch (e) { e1 = e; }
console.log(/非法 layer|重复 pass/.test(e1?.message || ''));

// 错误上下文
pipe.use({ name: 'boom', layer: 'target', filter: () => true, run: () => { throw new Error('x'); } });
let e2; try { await pipe.run({ id: 'c.js', ast: {} }); } catch (e) { e2 = e; }
console.log(/boom/.test(e2.message) && e2.cause.message === 'x');
```

**评分点**：
- 分层排序正确且同层保持注册序（稳定排序意识）；非法 layer/重复名抛错
- filter 过滤生效（未命中 pass 不执行不计时）；applied/profile 数据完整
- 错误包装带 pass+module 上下文且保留 cause 原始错误（不吞栈）
- 能说明「TS 剥离（type 层）先于降级（target 层）」的语义依赖理由属于加分
