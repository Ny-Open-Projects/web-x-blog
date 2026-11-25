---
title: [WCN-686] 笔试：实现 Figma token JSON 到 CSS 变量的转换器（含命名规范化 + 引用解析 + 单位处理）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-686：笔试：实现 Figma token JSON 到 CSS 变量的转换器（含命名规范化 + 引用解析 + 单位处理）

**答**：
- 需求：实现 figmaToCss(tokens)：输入 Figma Variables 风格 JSON（{name, value, type}[]），value 可能是别名引用（如 {ref:'color/blue'}）；输出 CSS 变量字符串，name 转 kebab-case 并加 --ds- 前缀，别名解析为 var(--ds-...)。
- 思路：先建 name→变量映射；value 含 ref 则解析引用（支持链式）；名称空格/斜杠转 -；带尺寸类型补 px（若原值无单位）。
- 边界：循环引用检测报错；未解析引用保留并告警；同名后者覆盖前者。

```javascript
export function figmaToCss(tokens) {
  const byName = new Map();
  tokens.forEach(t => byName.set(t.name, t));
  const kebab = s => s.replace(/[\s/]+/g, '-').toLowerCase();
  const varName = n => `--ds-${kebab(n)}`;
  const resolving = new Set();
  function resolve(name) {
    const t = byName.get(name);
    if (!t) return null;
    if (resolving.has(name)) throw new Error(`循环引用 ${name}`);
    resolving.add(name);
    let v = t.value;
    if (v && typeof v === 'object' && v.ref) {
      const target = resolve(v.ref);
      v = target ? `var(${varName(v.ref)})` : null;
    }
    resolving.delete(name);
    return { value: v, type: t.type };
  }
  return tokens.map(t => {
    const r = resolve(t.name);
    if (!r || r.value == null) { console.warn('未解析', t.name); return ''; }
    const unit = r.type === 'FLOAT' && !/px|rem|em/.test(String(r.value)) ? 'px' : '';
    return `${varName(t.name)}: ${r.value}${unit};`;
  }).filter(Boolean).join('\n');
}
console.log(figmaToCss([
  { name: 'color/blue', value: '#165DFF', type: 'COLOR' },
  { name: 'color/primary', value: { ref: 'color/blue' }, type: 'COLOR' },
]));
```

**评分点**：
- 名称规范化（空格/斜杠→连字符，加 --ds- 前缀）。
- 别名引用解析为 var(--ds-...)，支持链式引用。
- 循环引用检测并报错（避免无限递归）。
- FLOAT 类型无单位时补 px，未解析引用告警。
