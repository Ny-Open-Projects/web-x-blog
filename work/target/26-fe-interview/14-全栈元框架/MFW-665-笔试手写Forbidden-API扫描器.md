---
title: [MFW-665] 笔试：手写 Forbidden API 扫描器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-665：笔试：手写 Forbidden API 扫描器

**答**：实现 `scanForbidden(bundles, { targetRules })`。bundles: `{ name, target, code }[]`；targetRules: `Record<target, string[]>`（禁止 API 列表）。规则：1) 精确匹配（code.includes(api)——压缩后仍识别）；2) **守卫识别**：API 的宿主全局有 `typeof X === 'undefined'` 守卫 → 降级 'guarded'（合法的条件 polyfill）；3) 严重度：裸引用 = error（阻断）；guarded = warn；4) 豁免清单（opts.allow: `Record<target, string[]>`——已知的合法引用如 polyfill 库）；5) 返回 `{ errors, warnings, ok }`（ok = 无 error）。边界：target 无规则（跳过）；code 空；豁免命中（不报）。

```javascript
function scanForbidden(bundles = [], { targetRules = {}, allow = {} } = {}) {
  const errors = [], warnings = [];
  for (const b of bundles) {
    const rules = targetRules[b.target] ?? [];
    for (const api of rules) {
      if (b.code?.includes(api)) {
        if ((allow[b.target] ?? []).includes(api)) continue;   // 豁免
        const host = api.split(/[.\[]/)[0];
        const guarded = b.code.includes(`typeof ${host} === 'undefined'`) ||
                        b.code.includes(`typeof ${host} !== 'undefined'`);
        const finding = { bundle: b.name, target: b.target, api };
        if (guarded) warnings.push({ ...finding, severity: 'guarded' });
        else errors.push({ ...finding, severity: 'error' });
      }
    }
  }
  return { errors, warnings, ok: errors.length === 0 };
}

// 自测
const rules = {
  client: ['require("fs")', 'localStorage.', 'window.document'],
  server: ['window.', 'document.'],
};
const bundles = [
  { name: 'client.js', target: 'client', code: 'fetch("/api"); require("fs").readFile();' },   // error: fs
  { name: 'client2.js', target: 'client', code: 'typeof localStorage === "undefined" ? null : localStorage.getItem("k");' },   // guarded
  { name: 'server.js', target: 'server', code: 'if (typeof window !== "undefined") { window.alert(1) }' },   // guarded
  { name: 'server2.js', target: 'server', code: 'return document.title;' },   // error: document
];
let r = scanForbidden(bundles, { targetRules: rules });
console.log(r.errors.length === 2);                      // client fs + server document
console.log(r.warnings.length === 2);                    // 两个 guarded
console.log(r.ok === false);
console.log(r.errors.find(e => e.bundle === 'client.js').api === 'require("fs")');

// 豁免
r = scanForbidden(bundles, { targetRules: rules,
  allow: { client: ['require("fs")'] } });               // polyfill 库豁免
console.log(r.errors.length === 1);                      // fs 被豁免

// target 无规则跳过
r = scanForbidden([{ name: 'x', target: 'worker', code: 'require("fs")' }], { targetRules: rules });
console.log(r.errors.length === 0);
console.log(scanForbidden([], { targetRules: rules }).ok === true);
```

**评分点**：
- 守卫识别（typeof 检查 → 降级 warn——条件 polyfill 的合法引用不误报）
- 豁免清单（已知合法引用——polyfill 库的显式声明）；target 无规则跳过
- 严重度分级（裸引用 error / guarded warn——阻断与告警分离）
- 能说清「Forbidden API 扫描必须在产物层：依赖的间接 API 引用（import 链带来的 fs）只有产物才能发现」属于加分
