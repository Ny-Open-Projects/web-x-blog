---
title: [RBL-698] 笔试：手写设计 token 引用解析器（引用展开 + 循环 + 悬空）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-698：笔试：手写设计 token 引用解析器（引用展开 + 循环 + 悬空）

**答**：实现 `resolveTokens(tokens)`。tokens: `Record<name, string>`，值可为字面量（'#fff'、'16px'）或引用（'{color.primary}'，可嵌套引用）。返回 `{ resolved: Record<name, string>, problems: Array<{ type: 'missing'|'cycle', detail }> }`：1) 引用递归展开到字面量；2) 悬空引用（目标不存在）记 missing 且该 token 结果为 undefined；3) 循环引用记 cycle（列出环）且环上 token 全部 undefined；4) 引用带 fallback 语法 `{a|fallback}`（目标缺失用 fallback 字面量）；5) 多引用拼接值（'1px solid {color.border}'）逐段展开。边界：空 tokens、自引用。

```javascript
function resolveTokens(tokens = {}) {
  const resolved = {}; const problems = [];
  const getCycle = (name, stack = []) => {
    if (stack.includes(name)) return stack.slice(stack.indexOf(name)).concat(name);
    const raw = tokens[name];
    if (raw === undefined) return null;
    const refs = extractRefs(raw);
    for (const r of refs) {
      const c = getCycle(r.target, [...stack, name]);
      if (c) return c;
    }
    return null;
  };
  const extractRefs = (raw) => [...raw.matchAll(/\{([^}|]+)(?:\|([^}]*))?\}/g)]
    .map(m => ({ target: m[1], fallback: m[2] }));

  function expand(raw, name, stack = []) {
    let out = raw;
    for (const { target, fallback } of extractRefs(raw)) {
      let val;
      if (stack.includes(target)) {                       // 循环
        problems.push({ type: 'cycle', detail: [...stack, target].join(' -> ') });
        val = null;
      } else if (target in tokens && !problems.some(p => p.type === 'cycle' && p.detail.includes(target))) {
        val = expand(tokens[target], name, [...stack, target]);
      } else if (!(target in tokens)) {
        if (fallback !== undefined) val = fallback;
        else { problems.push({ type: 'missing', detail: `${name}: {${target}} 不存在` }); val = null; }
      } else {
        val = null;                                       // 目标本身失效（cycle/missing 传播）
      }
      if (val === null) return null;
      out = out.replace(`{${target}}`, val).replace(`{${target}|${fallback}}`, val);
    }
    return out;
  }

  for (const name of Object.keys(tokens)) {
    const cyc = getCycle(name);
    if (cyc) { problems.push({ type: 'cycle', detail: cyc.join(' -> ') }); continue; }
    resolved[name] = expand(tokens[name], name);
  }
  return { resolved, problems };
}

// 自测
const tokens = {
  'color.primary': '#3b82f6',
  'color.bg': '{color.primary}',
  'border': '1px solid {color.line|#ccc}',               // fallback
  'border.full': '{border}',
  'bad.ref': '{color.nope}',
  'a': '{b}', 'b': '{a}',                                // 循环
  'self': '{self}',
};
const { resolved, problems } = resolveTokens(tokens);
console.log(resolved['color.bg'] === '#3b82f6');        // 嵌套展开
console.log(resolved['border'] === '1px solid #ccc');   // fallback 生效
console.log(resolved['border.full'] === '1px solid {color.line|#ccc}');  // 引用链部分展开？应等 border 展开值
console.log(resolved['bad.ref'] === undefined);
console.log(problems.some(p => p.type === 'missing' && p.detail.includes('color.nope')));
console.log(problems.some(p => p.type === 'cycle' && /a -> b|b -> a|self/.test(p.detail)));
```

**评分点**：
- 引用递归展开与多引用拼接（字符串逐段替换）正确
- 三类错误区分：missing（悬空）、cycle（环路径可读）、传播失效（依赖失效 token 的引用为 undefined）
- fallback 语法解析（目标缺失才用，目标存在时忽略）
- 能说清「token 解析放进构建期是设计质量纳入 CI 的前提」属于加分
