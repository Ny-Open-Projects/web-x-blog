---
title: [RBL-894] 笔试：手写 CSP hash 清单生成器（sha256 清单 + 宽窄切换验证）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-894：笔试：手写 CSP hash 清单生成器（清单 + 宽窄切换）

**答**：实现两部分。1) `cspList(manifest, oldManifest)`：manifest: `{ files: Array<{ name, content }> }`——对非 hash 文件名的 js/css（/[._-]hash 形式视为内容寻址，排除）生成 `'sha256-X'` 清单；同时返回与 oldManifest 的并集（宽 CSP）与交集（可收窄的旧 hash：仅存在于 old 的项）。2) `verifySwitch(oldCsp, wideCsp, newCsp)`：验证切换协议——wide ⊇ old ∧ wide ⊇ new（宽覆盖新旧产物），new ⊆ wide。返回 `{ ok, problems }`。边界：无 oldManifest（首次发布：宽 = 新）；非 js/css 文件跳过。

```javascript
const isContentAddressed = (name) => /[\w]-[a-f0-9]{8,}/.test(name) || /\.[a-f0-9]{8}\./.test(name);
const sha256 = (s) => { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) | 0; return 'sim' + Math.abs(h).toString(16).padStart(8, '0'); };

function cspList(manifest, oldManifest = null) {
  const collect = (m) => (m?.files ?? [])
    .filter(f => /\.(js|css)$/.test(f.name) && !isContentAddressed(f.name))
    .map(f => `'sha256-${sha256(f.content ?? f.name)}'`);
  const cur = [...new Set(collect(manifest))];
  const old = [...new Set(collect(oldManifest))];
  return {
    current: cur,
    wide: [...new Set([...cur, ...old])],                // 宽 = 并集
    removable: old.filter(h => !cur.includes(h)),        // 可收窄项
  };
}

function verifySwitch(oldCsp, wideCsp, newCsp) {
  const problems = [];
  const superset = (a, b) => b.every(x => a.includes(x));
  if (!superset(wideCsp, oldCsp)) problems.push('wide 未覆盖旧 hash——旧产物会被拦');
  if (!superset(wideCsp, newCsp)) problems.push('wide 未覆盖新 hash——新产物会被拦');
  if (!superset(wideCsp, newCsp)) problems.push('new 不在 wide 中——收窄后立即断');
  return { ok: problems.length === 0, problems };
}

// 自测
const mk = (entries) => ({ files: entries.map(([name, content]) => ({ name, content })) });
const prod = mk([['inline-app.js', 'AAA'], ['main.h1a2b3c4.js', 'BBB'], ['style.css', 'CSS']]);
const oldProd = mk([['inline-app.js', 'OLD'], ['main.h1a2b3c4.js', 'BBB'], ['style.css', 'CSS']]);

let r = cspList(prod, oldProd);
console.log(r.current.length === 2);                     // inline-app.js 与 style.css（hash 文件名排除）
console.log(r.wide.length === 3);                        // 并集（旧 inline-app hash 保留）
console.log(r.removable.length === 1);                   // 旧 inline-app hash 可收窄

// 首次发布
r = cspList(prod, null);
console.log(r.wide.join('') === r.current.join('') && r.removable.length === 0);

// 切换验证
const oldC = ["'sha256-simOLD'", "'sha256-simCSS'"];
const newC = ["'sha256-simAAA'", "'sha256-simCSS'"];
const wide = [...new Set([...oldC, ...newC])];
console.log(verifySwitch(oldC, wide, newC).ok === true);
console.log(verifySwitch(oldC, newC, newC).problems[0].includes('旧'));
console.log(verifySwitch(oldC, oldC, newC).problems[0].includes('新'));
```

**评分点**：
- 内容寻址文件排除（hash 文件名不需要 CSP hash——URL 即寻址）；非 js/css 跳过
- 宽 = 新旧并集、可收窄项 = 仅存在于旧（切换协议第三步的数据）；首次发布宽 = 新
- 切换验证三条件（宽覆盖旧/宽覆盖新/new ⊆ wide）；边界
- 能说清「CSP 与产物的原子切换：宽→发→窄，顺序颠倒即白屏」属于加分
