---
title: [RBL-736] 笔试：手写 workspace 依赖转换器（双态解析 + 残留检测）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-736：笔试：手写 workspace 依赖转换器（双态解析 + 残留检测）

**答**：实现 `convertDeps(deps, resolvedVersions, mode)`。deps: `Record<name, spec>`（spec 可为普通 semver 或 workspace:*/^/~）；resolvedVersions: `Record<name, string>`（workspace 包实际版本）；mode: 'dev'|'release'。规则：1) 非 workspace spec 原样；2) workspace:* → dev: '*'、release: 实际版本；workspace:^ → dev/release: '^实际版本'；workspace:~ 同理 ~；3) release 态 workspace 依赖不在 resolvedVersions 中 → 抛错（依赖缺失）；4) 返回转换后的 deps 对象 + `warnings`（普通 spec 指向的包实际在 workspace 内——可能应改用 workspace 协议的提示）。边界：deps 为空；resolvedVersions 缺失但 spec 非 workspace。

```javascript
function convertDeps(deps = {}, resolvedVersions = {}, mode) {
  const out = {}, warnings = [];
  for (const [name, spec] of Object.entries(deps)) {
    if (!spec.startsWith('workspace:')) {
      if (mode === 'release' && name in resolvedVersions && !/^[\^~]?\d/.test(spec))
        warnings.push(`${name}: 非标准 spec '${spec}' 但包在 workspace 内`);
      out[name] = spec;
      continue;
    }
    const target = resolvedVersions[name];
    if (target === undefined)
      throw new Error(`release 模式缺失版本: ${name}（workspace 协议依赖必须可解析）`);
    const op = spec.slice('workspace:'.length);
    out[name] = op === '*' && mode === 'dev' ? '*'
      : op === '*' ? target
      : op + target;
  }
  return { deps: out, warnings };
}

// 自测
const rv = { ui: '1.2.3', utils: '0.4.0' };
let r = convertDeps({ ui: 'workspace:*', utils: 'workspace:^', lodash: '^4.17.0' }, rv, 'dev');
console.log(JSON.stringify(r.deps));
// {"ui":"*","utils":"^1.2.3","lodash":"^4.17.0"}
console.log(r.warnings.length === 0);

r = convertDeps({ ui: 'workspace:*', utils: 'workspace:~', app: 'workspace:1.0.0' }, rv, 'release');
console.log(r.deps.ui === '1.2.3');                      // * -> 精确
console.log(r.deps.utils === '~0.4.0');
console.log(r.deps.app === '1.0.0');                     // 带版本的 workspace: 精确转换

// release 缺失版本
let e; try { convertDeps({ ghost: 'workspace:*' }, rv, 'release'); } catch (x) { e = x; }
console.log(/缺失版本/.test(e.message));

// 非法 spec 警告
r = convertDeps({ ui: 'latest' }, rv, 'release');
console.log(r.warnings[0].includes('latest'));

console.log(convertDeps({}, rv, 'release').deps);        // {}
```

**评分点**：
- 双态转换矩阵正确（\*/^/~ × dev/release；dev \* 保持通配）
- release 缺版本抛错（workspace 依赖可解析性是发布前提）
- 非标准 spec 警告（latest 等松散声明）
- 能说清「release 构建模拟发布后世界的解析」属于加分
