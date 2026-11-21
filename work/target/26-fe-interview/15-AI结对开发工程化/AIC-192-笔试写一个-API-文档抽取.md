---
title: [AIC-192] 笔试：实现一个 API 文档抽取校验器：从类型定义抽导出签名、比对文档字段、输出编造参数清单？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-192：笔试：实现一个 API 文档抽取校验器：从类型定义抽导出签名、比对文档字段、输出编造参数清单？
**需求**：实现 `checkDocs(typeDef, doc)`：
- 从 TS interface/type 文本抽取字段名与类型、必填性（无 `?`）；
- doc: `{fn: {params: [{name, desc}], returns}}`；
- 校验：文档参数 ⊆ 类型字段（编造检测）、必填字段全部覆盖（遗漏检测）、类型名一致性抽查；
- 输出 `{phantom, missing, typeMismatch, ok}`。

```javascript
function extractFields(typeDef) {
  const fields = new Map();
  // 抽 interface body
  const body = typeDef.match(/(?:interface|type)\s+\w+[^{]*\{([\s\S]*?)\n\}/)?.[1] ?? typeDef;
  for (const m of body.matchAll(/^\s{2}(\w+)(\?)?:\s*([^;]+);/gm)) {
    fields.set(m[1], { type: m[3].trim(), required: !m[2] });
  }
  return fields;
}

function checkDocs(typeDef, doc) {
  const fields = extractFields(typeDef);
  const docNames = doc.params.map(p => p.name);
  const phantom = docNames.filter(n => !fields.has(n));           // 编造
  const missing = [...fields.entries()]
    .filter(([n, f]) => f.required && !docNames.includes(n))      // 遗漏必填
    .map(([n]) => n);
  const typeMismatch = doc.params
    .filter(p => fields.has(p.name) && p.type && fields.get(p.name).type !== p.type)
    .map(p => ({ name: p.name, docType: p.type, realType: fields.get(p.name).type }));
  return {
    phantom, missing, typeMismatch,
    ok: !phantom.length && !missing.length && !typeMismatch.length,
  };
}

// 测试
const typeDef = `interface GoodsQuery {
  keyword?: string;
  page: number;
  pageSize: number;
  category?: 'all' | 'hot';
}`;
const doc = {
  params: [
    { name: 'keyword', type: 'string' },
    { name: 'page', type: 'number' },
    { name: 'sort', type: 'string' },   // 编造！类型里没有
    { name: 'pageSize', type: 'string' }, // 类型不符
  ],
};
console.log(checkDocs(typeDef, doc));
// phantom:['sort'] missing:['pageSize']? 不——pageSize 在 doc 里但类型错 → typeMismatch；missing 为空
// 实际：phantom=['sort'], typeMismatch=[pageSize]，若去掉 pageSize 则 missing=['pageSize']
```

**评分点**：
1. 文档参数是「编造」还是「遗漏」分开检测——两者修复动作不同（删文档 vs 补文档）；
2. 类型一致性抽查防 AI 写出「语义正确的谎言」（参数存在但类型写错）；
3. 正则抽 interface 要匹配缩进与 `?` 可选标记；
4. ok 判定三条件与结构化输出（可直接回喂 AI 修文档）；
5. 追问：真正的实现应基于 TS Compiler API（AST），正则版无法处理联合类型/泛型——说出边界加分。
