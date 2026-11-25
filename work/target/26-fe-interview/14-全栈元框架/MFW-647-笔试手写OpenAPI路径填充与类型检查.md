---
title: [MFW-647] 笔试：手写 OpenAPI 路径填充器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-647：笔试：手写 OpenAPI 路径填充器

**答**：实现 `fillPath(template, params, { strict })`。template: `/products/{id}/reviews/{rid}`；params: `Record<name, value>`。规则：1) `{name}` 替换为 params[name]（URL encode——值含 / ? 等）；2) **strict 模式**：template 中所有 {name} 必须有对应 param（缺失抛错——URL 缺段 = 请求打错）；params 中多余键（不在 template 中）→ warn（typo 检出：id→idx）；3) 未转义的 value 转义（encodeURIComponent——路径段的保留字符处理）；4) 返回填充后的 URL。边界：无参数 template（原样返回）；params 为 null/undefined；重复的 {id} 占位（全部替换）。

```javascript
function fillPath(template, params = {}, { strict = true } = {}) {
  const placeholders = [...template.matchAll(/\{(\w+)\}/g)].map(m => m[1]);
  const missing = placeholders.filter(p => params[p] === undefined);
  if (strict && missing.length)
    throw new Error(`路径参数缺失: ${missing.join(',')} in ${template}`);
  const extra = Object.keys(params).filter(k => !placeholders.includes(k));
  const warnings = extra.length ? [`多余参数: ${extra.join(',')}`] : [];
  const url = template.replace(/\{(\w+)\}/g, (_, name) => {
    const v = params[name];
    return v === undefined ? `{${name}}` : encodeURIComponent(String(v));
  });
  return { url, warnings };
}

// 自测
let r = fillPath('/products/{id}/reviews/{rid}', { id: 42, rid: 'r1' });
console.log(r.url === '/products/42/reviews/r1');

// URL encode
r = fillPath('/users/{name}', { name: '张 三/a' });
console.log(r.url === '/users/' + encodeURIComponent('张 三/a'));   // %E5%BC%A0%20%E4%B8%89%2Fa

// 缺失参数 strict 抛错
e = null; try { fillPath('/p/{id}/{rid}', { id: 1 }); } catch (x) { e = x; }
console.log(/路径参数缺失.*rid/.test(e.message));
// 非严格：保留占位
r = fillPath('/p/{id}/{rid}', { id: 1 }, { strict: false });
console.log(r.url === '/p/1/{rid}');

// 多余参数 warn
r = fillPath('/p/{id}', { id: 1, idx: 9 });
console.log(r.warnings[0].includes('idx'));

// 重复占位
r = fillPath('/p/{id}/x/{id}', { id: 7 });
console.log(r.url === '/p/7/x/7');

// 无参数
console.log(fillPath('/health').url === '/health');
console.log(fillPath('/health', null).url === '/health');
```

**评分点**：
- 占位替换 + URL encode（路径段的保留字符——'/' 在值内的转义）；strict 缺失抛错
- 多余参数 warn（typo 检出——类型化的运行时版）；重复占位全替换
- 边界（无参数/null params）；非 strict 保留占位（可调试）
- 能说清「strict 模式把 URL 拼装错误前置到调用时——多余参数 warn 是 typo 检出」属于加分
