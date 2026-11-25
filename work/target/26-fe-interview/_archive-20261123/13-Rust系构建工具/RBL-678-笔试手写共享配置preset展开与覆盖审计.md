---
title: [RBL-678] 笔试：手写共享配置 preset 展开器与覆盖审计
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-678：笔试：手写共享配置 preset 展开器与覆盖审计

**需求**：实现 `apply(preset, { overrides })` 与 `auditLog`。preset 可以是对象或 `(base) => object` 函数（base 是 base preset 的产物）。规则：1) overrides 深合并进 preset 产物（数组替换语义）；2) 每次覆盖记录日志 `{ path, from, to }`（from 是 preset 原值）；3) overrides 中的 key 在 preset 不存在时不记「覆盖」而记 `added`（新增字段也要显式）；4) 返回 `{ config, log }`；5) preset 函数里调用未定义 preset 抛错。提供 `flatten(obj)` 辅助（点路径展开）。

```javascript
function flatten(obj, prefix = '', out = {}) {
  for (const k of Object.keys(obj ?? {})) {
    const p = prefix ? `${prefix}.${k}` : k;
    const v = obj[k];
    if (v && typeof v === 'object' && !Array.isArray(v)) flatten(v, p, out);
    else out[p] = v;
  }
  return out;
}

function apply(preset, base, { overrides = {} } = {}) {
  const source = typeof preset === 'function' ? preset(base) : structuredClone(preset);
  const log = [];
  const flatSrc = flatten(source);
  const merged = deepMerge(source, overrides, log, flatSrc);
  return { config: merged, log };
}

function deepMerge(target, patch, log, flatSrc, prefix = '') {
  if (patch === undefined) return target;
  if (!isPlain(target) || !isPlain(patch)) {             // 数组/标量整体替换
    if (prefix) {
      const has = prefix in flatSrc;
      log.push({ type: has ? 'override' : 'added', path: prefix, from: flatSrc[prefix] ?? undefined, to: patch });
    }
    return patch;
  }
  const out = { ...target };
  for (const k of Object.keys(patch)) {
    out[k] = deepMerge(target?.[k], patch[k], log, flatSrc, prefix ? `${prefix}.${k}` : k);
  }
  return out;
}
const isPlain = (v) => v !== null && typeof v === 'object' && !Array.isArray(v);

// 自测
const base = { output: { format: 'es', dir: 'dist' }, resolve: { extensions: ['.ts'] } };
const reactApp = (b) => ({ ...b, plugins: ['react'], output: { ...b.output, sourcemap: true } });

const { config, log } = apply(reactApp, base, {
  overrides: { output: { dir: 'build' }, serverPort: 3000 },
});
console.log(config.output.dir === 'build');
console.log(config.output.sourcemap === true);
console.log(config.plugins[0] === 'react');
console.log(config.serverPort === 3000);

const types = Object.fromEntries(log.map(l => [l.path, l.type]));
console.log(types['output.dir'] === 'override');         // 覆盖
console.log(types['serverPort'] === 'added');            // 新增
console.log(log.find(l => l.path === 'output.dir').from === 'dist');
console.log('output.format' in types === false);         // 未覆盖不记日志

// 数组替换
const { config: c2 } = apply(reactApp, base, { overrides: { resolve: { extensions: ['.js'] } } });
console.log(JSON.stringify(c2.resolve.extensions));      // [".js"] 整体替换
```

**评分点**：
- preset 函数形态（接收 base 产物）与对象形态都支持；深合并数组替换语义正确
- 覆盖/新增区分记录（added 也要显式——新增同样偏离 preset 统一性），from 值可追溯
- 未覆盖字段不产生日志（审计信噪比）；点路径展开正确
- 能说清「覆盖显式化是为了消灭分叉假象」属于加分
