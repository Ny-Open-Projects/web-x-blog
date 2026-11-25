---
title: [RBL-682] 笔试：手写 external 依赖覆盖校验器（含传递闭包与版本冲突检测）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-682：笔试：手写 external 依赖覆盖校验器（传递闭包与版本冲突）

**需求**：实现 `verifyRuntimeDeps(externals, installed, depTree)`。externals: `string[]`（bundle 保留的运行时依赖）；installed: `Record<name, version>`（镜像里实际安装的）；depTree: `Record<name, Record<depName, versionReq>>`（各包声明的依赖）。校验：1) externals 直接依赖全部 installed（缺失报 `missing`）；2) 传递闭包：depTree 递归展开的依赖也要 installed（环去重）；3) 版本冲突：同一包被声明为不同版本需求时报警告 `conflict`（installed 只有一个版本，需求不兼容时报 error）；4) 返回 `{ problems: Array<{ type, detail }>, closure: string[] }`（closure 是传递闭包全集，排序输出）。

```javascript
function satisfies(installedVer, req) {
  // 简化：^ / 精确 / *
  if (req === '*' || req === installedVer) return true;
  if (req.startsWith('^')) {
    const [m1] = req.slice(1).split('.'), [m2] = installedVer.split('.');
    return m1 === m2;
  }
  return false;
}

function verifyRuntimeDeps(externals, installed, depTree) {
  const problems = []; const seen = new Set();
  const visit = (name, neededBy) => {
    if (seen.has(name)) return;
    seen.add(name);
    if (!(name in installed)) {
      problems.push({ type: 'missing', detail: `${name}（被 ${neededBy} 需要）` });
      return;
    }
    const deps = depTree[name] ?? {};
    for (const [dep, req] of Object.entries(deps)) {
      if (!satisfies(installed[dep], req))
        problems.push({ type: 'conflict', detail: `${dep} 需要 ${req}，已装 ${installed[dep] ?? '无'}（来自 ${name}）` });
      visit(dep, name);
    }
  };
  for (const ext of externals) visit(ext, '<externals>');
  return { problems, closure: [...seen].sort() };
}

// 自测
const externals = ['express', 'pg'];
const installed = { express: '4.18.0', pg: '8.11.0', 'body-parser': '1.20.0', 'pg-protocol': '1.6.0' };
const depTree = {
  express: { 'body-parser': '^1.20.0' },
  pg: { 'pg-protocol': '^1.6.0' },
  'body-parser': {},
  'pg-protocol': {},
};
let r = verifyRuntimeDeps(externals, installed, depTree);
console.log(r.problems.length === 0);
console.log(r.closure.join(',') === 'body-parser,express,pg,pg-protocol');   // 闭包全集

// 缺失传递依赖
r = verifyRuntimeDeps(['express'], { express: '4.18.0' }, depTree);
console.log(r.problems.some(p => p.type === 'missing' && p.detail.includes('body-parser')));

// 版本冲突
r = verifyRuntimeDeps(['pg'], { pg: '8.11.0', 'pg-protocol': '1.0.0' }, {
  pg: { 'pg-protocol': '^1.6.0' }, 'pg-protocol': {},
});
console.log(r.problems.some(p => p.type === 'conflict' && p.detail.includes('pg-protocol')));

// external 直接缺失
r = verifyRuntimeDeps(['vue'], {}, {});
console.log(r.problems[0].type === 'missing' && r.problems[0].detail.includes('vue'));

// 传递环不爆栈
r = verifyRuntimeDeps(['a'], { a: '1.0.0', b: '1.0.0' }, { a: { b: '^1.0.0' }, b: { a: '^1.0.0' } });
console.log(r.problems.length === 0 && r.closure.join(',') === 'a,b');
```

**评分点**：
- 传递闭包展开完整（含环去重），closure 排序输出
- 缺失检测带 neededBy（可诊断谁缺它）；版本需求校验（^ 主版本匹配、精确、\*）
- 冲突按 installed 实际版本判定（需求不兼容报 error）
- 能说清「external 清单是镜像瘦身与运行时正确性的契约」属于加分
