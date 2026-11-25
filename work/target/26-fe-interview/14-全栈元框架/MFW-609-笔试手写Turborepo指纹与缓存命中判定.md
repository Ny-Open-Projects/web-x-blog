---
title: [MFW-609] 笔试：手写 Turborepo 指纹与缓存命中
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-609：笔试：手写 Turborepo 指纹

**答**：实现 `taskFingerprint(task, ctx)`。task: `{ name, inputs, envVars, outputs }`；ctx: `{ fileHashes: Record<path, hash>, env: Record<string, string>, depHashes: Record<depName, hash>, toolVersion }`。规则：1) 输入指纹：inputs 模式匹配的文件 hash（glob 简化：startsWith/endsWith）；2) 依赖闭包：dependsOn 的包的 hash（^build 前缀）；3) 环境变量：envVars 列表的 env 值（`NEXT_PUBLIC_*` 通配——env 键匹配前缀）；4) 工具版本；5) 组合 hash（稳定排序）。`cacheHit(fingerprint, cache)`：键匹配 → { hit, artifact? }；miss → { miss }。边界：inputs 空（只有 deps/env）；env 通配无匹配（空串参与）；依赖缺失 → 抛错（闭包不完整 = 键不可信 RBL-582）。

```javascript
const djb2 = (s) => { let h = 5381; for (const c of s) h = ((h << 5) + h + c.charCodeAt(0)) >>> 0;
  return h.toString(16); };
function globMatch(pattern, path) {
  if (pattern.startsWith('!')) return null;              // 排除项跳过
  if (pattern.endsWith('/**')) return path.startsWith(pattern.slice(0, -3));
  if (pattern.endsWith('*')) return path.startsWith(pattern.slice(0, -1));
  return path === pattern || path.startsWith(pattern);
}
function taskFingerprint(task, ctx) {
  const parts = [];
  for (const pattern of task.inputs ?? []) {
    for (const [path, hash] of Object.entries(ctx.fileHashes))
      if (globMatch(pattern, path)) parts.push(`${path}:${hash}`);
  }
  for (const dep of task.dependsOn ?? []) {
    const depName = dep.replace('^\.', '');              // ^build → build 的包名
    const dh = ctx.depHashes[depName];
    if (dh === undefined) throw new Error(`依赖闭包不完整: ${depName}`);
    parts.push(`dep:${depName}:${dh}`);
  }
  for (const ev of task.envVars ?? []) {
    for (const [k, v] of Object.entries(ctx.env))
      if (ev.endsWith('*') ? k.startsWith(ev.slice(0, -1)) : k === ev)
        parts.push(`${k}=${v}`);
  }
  parts.push(`tool:${ctx.toolVersion}`);
  parts.sort();                                          // 稳定排序
  return djb2(parts.join('|'));
}
function cacheHit(fp, cache) {
  return cache[fp] ? { hit: true, artifact: cache[fp] } : { hit: false };
}

// 自测
const ctx = {
  fileHashes: { 'src/a.ts': 'h1', 'src/b.ts': 'h2', 'test/x.test.ts': 'h3' },
  env: { 'NEXT_PUBLIC_API': 'https://api', NODE_ENV: 'prod' },
  depHashes: { ui: 'dh1' }, toolVersion: 'turbo@2',
};
const task = { name: 'build', inputs: ['src/**'],
  dependsOn: ['^build'], envVars: ['NEXT_PUBLIC_*'] };
let fp = taskFingerprint(task, ctx);
console.log(typeof fp === 'string' && fp.length > 0);

// 稳定性：同输入同指纹
console.log(taskFingerprint(task, ctx) === fp);
// env 变化 → 指纹变
console.log(taskFingerprint(task, { ...ctx,
  env: { ...ctx.env, 'NEXT_PUBLIC_API': 'https://api2' } }) !== fp);
// 依赖缺失 → 抛错
let e; try { taskFingerprint(task, { ...ctx, depHashes: {} }); } catch (x) { e = x; }
console.log(/依赖闭包/.test(e.message));

// 缓存命中
const cache = { [fp]: { output: 'dist' } };
console.log(cacheHit(fp, cache).hit === true);
console.log(cacheHit(fp + 'x', cache).hit === false);
```

**评分点**：
- 指纹四要素：文件/依赖闭包/环境变量/工具版本（漏一环 = 错缓存 RBL-587）
- 依赖缺失抛错（闭包不完整 = 键不可信——fail-fast 而非静默错缓存）
- 稳定排序 + djb2；env 通配前缀匹配；边界
- 能说清「Turborepo 指纹的正确性 = 输入闭包完备性——环境变量进 bundle 所以必须进指纹」属于加分
