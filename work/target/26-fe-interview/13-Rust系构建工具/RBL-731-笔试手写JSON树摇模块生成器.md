---
title: [RBL-731] 笔试：手写 JSON 树摇模块生成器（路径收集 + 具名导出 + 保守回退）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-731：笔试：手写 JSON 树摇模块生成器（路径收集 + 具名导出）

**答**：实现两部分。1) `collectUsage(code, importName)`：收集代码中 `importName.xxx` 与 `importName["a-b"]` 的字段路径（嵌套点路径如 `config.db.host`）；返回去重数组。2) `jsonToModule(json, paths)`：paths 为空 → `export default <json>` 全量；否则对每个路径生成 `export const <合法标识符> = <值>`（路径不存在的字段跳过并 warn）；路径含非法标识符字符（`a-b`）时改用索引式导出对象 `export const __fields = { 'a-b': val }` 与合法键的具名导出混合。边界：json 非对象（数组/标量）忽略 paths 全量导出。

```javascript
function collectUsage(code, importName) {
  const esc = importName.replace(/[$]/g, '\\$');
  const paths = new Set();
  for (const m of code.matchAll(new RegExp(`${esc}\\.([\\w$]+(?:\\.[\\w$]+)*)`, 'g')))
    paths.add(m[1]);
  for (const m of code.matchAll(new RegExp(`${esc}\\[(['"])([^'"]+)\\1\\]`, 'g')))
    paths.add(m[2]);
  return [...paths];
}
const ident = (p) => p.replace(/[^\w$]/g, '_');
const get = (o, p) => p.split('.').reduce((a, k) => (a == null ? a : a[k]), o);

function jsonToModule(json, paths = []) {
  if (!paths.length || typeof json !== 'object' || json === null || Array.isArray(json))
    return `export default ${JSON.stringify(json)};`;
  const named = [], bracket = [];
  for (const p of paths) {
    const v = get(json, p);
    if (v === undefined) { console.warn(`skip: ${p}`); continue; }
    if (/^[A-Za-z_$][\w$]*$/.test(p)) named.push(`export const ${p} = ${JSON.stringify(v)};`);
    else bracket.push(`  ${JSON.stringify(p)}: ${JSON.stringify(v)},`);
  }
  const out = [...named];
  if (bracket.length) out.push(`export const __fields = {\n${bracket.join('\n')}\n};`);
  return out.join('\n');
}

// 自测
const json = { version: '1.2', 'db-host': 'pg://x', config: { db: { host: 'h', port: 5432 } } };
let r = jsonToModule(json, ['version', 'config.db.host', 'db-host']);
console.log(r.includes(`export const version = "1.2";`));
console.log(r.includes(`export const config_db_host = "h";`));
console.log(r.includes(`"db-host": "pg://x"`));          // 非法标识符进 __fields
console.log(!r.includes('"1.2", "pg://x"'.slice(0, 5)));  // 无全量

r = jsonToModule(json, ['ghost.path']);                  // 不存在 -> 仅 warn，空导出
console.log(!r.includes('export'));

r = jsonToModule(json, []);                              // 全量默认导出
console.log(r.startsWith('export default'));
console.log(jsonToModule([1, 2], ['0']).startsWith('export default'));   // 数组全量

console.log(collectUsage('const v = cfg.version; cfg["db-host"]; cfg.config.db.port;', 'cfg')
  .sort().join(','));
// config.db.port, db-host, version
```

**评分点**：
- 路径收集覆盖点语法与方括号语法（引号键）；去重
- 具名导出合法性分流（合法标识符具名 / 非法键进 __fields）；缺失路径 warn 跳过不崩
- 空 paths/非对象 JSON 保守回退全量（静态分析不完备时的安全默认）
- 能说清「动态访问收集不到所以保守回退 + 告警」属于加分
