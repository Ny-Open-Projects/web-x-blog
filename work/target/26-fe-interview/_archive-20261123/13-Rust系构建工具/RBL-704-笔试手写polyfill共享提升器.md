---
title: [RBL-704] 笔试：手写 polyfill 共享提升器（引用计数 + 提取合并 + 引用改写）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-704：笔试：手写 polyfill 共享提升器（引用计数 + 提取合并 + 引用改写）

**需求**：实现 `hoistPolyfills(chunks, { minRefs })`。chunk: `{ name, code }`，code 中 polyfill 形如 `import 'polyfill:FEATURE';`（行级）。规则：1) 统计每个 polyfill 特性被多少 chunk 引用；2) 引用数 ≥ minRefs 的特性提取到新 polyfill chunk（排在 chunks 首位），从原 chunk 移除对应行；3) 原 chunk 在头部加一行 `import 'polyfill:__shared';`（引用共享 chunk）；4) 无提取时原样返回（不加共享 chunk）；5) 返回新数组（不改入参）+ `report: Record<feature, refs>`。

```javascript
const RE = /^import 'polyfill:([^']+)';$/;

function hoistPolyfills(chunks, { minRefs = 2 } = {}) {
  const report = {};
  for (const c of chunks)
    for (const line of c.code.split('\n')) {
      const m = RE.exec(line.trim());
      if (m) report[m[1]] = (report[m[1]] || 0) + 1;
    }
  const shared = Object.keys(report).filter(f => report[f] >= minRefs);
  if (!shared.length) return { chunks: structuredClone(chunks), report, shared: [] };

  const newChunks = chunks.map(c => {
    const kept = c.code.split('\n').filter(l => {
      const m = RE.exec(l.trim());
      return !m || !shared.includes(m[1]);
    });
    return { name: c.name, code: `import 'polyfill:__shared';\n` + kept.join('\n') };
  });
  newChunks.unshift({ name: 'polyfill',
    code: shared.map(f => `import 'polyfill:${f}';`).join('\n') });
  return { chunks: newChunks, report, shared };
}

// 自测
const chunks = [
  { name: 'main', code: ["import 'polyfill:array.flat';", "import 'polyfill:string.at';", 'code1;'].join('\n') },
  { name: 'a', code: ["import 'polyfill:array.flat';", 'code2;'].join('\n') },
  { name: 'b', code: ["import 'polyfill:array.flat';", "import 'polyfill:string.at';", 'code3;'].join('\n') },
  { name: 'c', code: ["import 'polyfill:proxy';", 'code4;'].join('\n') },
];
const { chunks: out, report, shared } = hoistPolyfills(chunks, { minRefs: 2 });
console.log(JSON.stringify(report));                     // array.flat:3, string.at:2, proxy:1
console.log(shared.join(','));                           // array.flat,string.at
console.log(out[0].name === 'polyfill');
console.log(out[0].code.split('\n').sort().join('|'));
// import 'polyfill:array.flat';|import 'polyfill:string.at';
console.log(!out[1].code.includes('polyfill:array.flat') && out[1].code.startsWith("import 'polyfill:__shared';"));
console.log(out[3].code.includes('polyfill:proxy'));     // proxy 引用少未提升
console.log(out.length === 5);

// minRefs 不满足
const r2 = hoistPolyfills(chunks, { minRefs: 5 });
console.log(r2.shared.length === 0 && r2.chunks[0].name === 'main');

// 入参不变
console.log(chunks[0].code.includes('polyfill:array.flat'));
```

**评分点**：
- 引用计数正确（跨 chunk 统计）；阈值过滤（minRefs 不达不提取、原样返回）
- 提取后原 chunk 移除对应行且头部加共享引用（不改入参的纯函数性）
- polyfill chunk 排首位（加载顺序：先 polyfill 后业务）
- 能说清「重复注入 vs 共享提升的体积与请求数权衡」属于加分
