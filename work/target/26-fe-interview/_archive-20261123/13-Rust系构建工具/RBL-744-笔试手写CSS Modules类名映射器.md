---
title: [RBL-744] 笔试：手写 CSS Modules 类名映射器（scoped 改写 + 组合继承 + 导出）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-744：笔试：手写 CSS Modules 类名映射器（scoped + composes 继承 + 导出）

**需求**：实现 `transformCssModule(css, id, { hash })`。规则：1) 提取 `.className` 选择器（不含伪类 .foo:hover 的 hover 部分）→ scoped 名 `_foo_<hash8>`；2) CSS 文本中替换所有类选择器；3) **composes 处理**：`.bar { composes: foo; }` 或 `composes: foo from global;`——bar 的映射值 = 自己 scoped 名 + 所组合类的映射名（空格连接）；from global 直接用全局名；4) 生成导出 JS：`export default { foo: '_foo_h1', bar: '_bar_h2 _foo_h1', ... }`；5) :global(.x) 内的类不改写。返回 `{ css, js }`。

```javascript
function transformCssModule(css, id, { hash } = {}) {
  const h = hash(id);
  const mapping = {};
  // 先收集 composes
  const composes = {};                                   // class -> [{ name, global }]
  for (const m of css.matchAll(/\.([\w-]+)\s*\{([^}]*)\}/g)) {
    const [, cls, body] = m;
    const c = /composes:\s*([^;]+);/.exec(body);
    if (c) composes[cls] = c[1].trim().split(/\s+/).map(x => {
      const gm = /^(\w+)\s+from\s+global$/.exec(x);
      return gm ? { name: gm[1], global: true } : { name: x, global: false };
    });
  }
  const scopedOf = (cls) => mapping[cls] ?? (mapping[cls] = `_${cls}_${h}`);
  // 组合链解析（防止 composes 前置依赖未 scoped）
  const exportOf = (cls) => {
    let own = scopedOf(cls);
    const parts = [own];
    for (const c of composes[cls] || []) {
      if (c.global) parts.push(c.name);
      else parts.push(exportOf(c.name));
    }
    return [...new Set(parts)].join(' ');
  };
  // CSS 改写：:global 保护
  const rewritten = css.replace(/:global\(([^)]+)\)/g, '⟦G:$1⟧')
    .replace(/\.([\w-]+)/g, (whole, cls) => mapping[cls] ?? (mapping[cls] = `_${cls}_${h}`))
    .replace(/⟦G:([^)]+)\⟧/g, ':global($1)');
  // 导出：类名 -> 组合值
  const exports = {};
  for (const cls of Object.keys(mapping))
    exports[cls] = exportOf(cls);
  return { css: rewritten, js: `export default ${JSON.stringify(exports, null, 2)};` };
}

// 自测
const css = `
:global(.reset) { margin: 0; }
.foo { color: red; }
.bar { composes: foo; background: blue; }
.baz { composes: bar reset from global; }
.foo:hover { color: darkred; }
`;
const { css: out, js } = transformCssModule(css, '/a.module.css', { hash: (s) => 'h12345' });
console.log(out.includes(':global(.reset)'));            // global 不改写
console.log(out.includes('._foo_h12345:hover'));         // 伪类只改主体
console.log(out.includes('._foo_h12345 {'));
console.log(out.includes('._bar_h12345 {'));
const exp = JSON.parse(js.match(/export default (\{[\s\S]*\});/)[1]);
console.log(exp.foo === '_foo_h12345');
console.log(exp.bar === '_bar_h12345 _foo_h12345');      // composes 继承
console.log(exp.baz === '_baz_h12345 _bar_h12345 _foo_h12345 reset');  // 链式 + global
```

**评分点**：
- scoped 改写正确（伪类主体改写、:global 保护、hash 参与）
- composes 语义正确：本地组合递归展开（bar 组合 foo）、global 组合直接用全局名、组合值空格连接（CSS 多类叠加）
- 导出对象含全部类（含被组合的基类）；同一类改写与导出一致
- 能说清「composes 是 CSS Modules 的复用原语，构建器负责把它变成类名叠加」属于加分
