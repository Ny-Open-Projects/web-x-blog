---
title: [MFW-635] 笔试：手写 LLM 组件白名单渲染器
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-635：笔试：手写 LLM 组件白名单渲染器

**答**：实现 `renderAIRoot(spec, registry)`。spec: `{ component: string, props: object, children?: spec[] }`。registry: `Record<name, { render: (props) => Node, schema: { validate(props) -> { ok, reason? } }, maxDepth?: number }>`. 规则：1) 组件不在 registry → throw 'unknown-component'；2) props schema 校验失败 → throw 'invalid-props'（含 reason）；3) children 递归渲染（子 spec 同规则）；4) **深度限制**：嵌套 > maxDepth（默认 5）→ throw 'depth-exceeded'（防 LLM 生成深树——DoS）；5) 节点计数上限（> 100 节点 throw 'too-many-nodes'）。边界：children 空；嵌套恰在限内（允许）；registry 空。

```javascript
function renderAIRoot(spec, registry, { maxDepth = 5, maxNodes = 100 } = {}) {
  let nodeCount = 0;
  function render(spec, depth, path) {
    if (depth > maxDepth) throw new Error(`depth-exceeded at ${path}（> ${maxDepth}）`);
    const entry = registry[spec.component];
    if (!entry) throw new Error(`unknown-component: ${spec.component} at ${path}`);
    const v = entry.schema.validate(spec.props ?? {});
    if (!v.ok) throw new Error(`invalid-props at ${path}: ${v.reason}`);
    nodeCount++;
    if (nodeCount > maxNodes) throw new Error(`too-many-nodes (> ${maxNodes})`);
    const childNodes = (spec.children ?? []).map((c, i) => render(c, depth + 1, `${path}.${spec.component}[${i}]`));
    return entry.render(spec.props ?? {}, childNodes);
  }
  return render(spec, 0, 'root');
}

// 自测
const registry = {
  Card: { schema: { validate: (p) => p.title ? { ok: true } : { ok: false, reason: 'title required' } },
    render: (p, children) => `<card>${p.title}${children.join('')}</card>` },
  Text: { schema: { validate: () => ({ ok: true }) },
    render: (p) => `<t>${p.text ?? ''}</t>` },
};
let r = renderAIRoot({ component: 'Card', props: { title: 'Hi' },
  children: [{ component: 'Text', props: { text: 'deep' } }] }, registry);
console.log(r === '<card>Hi<t>deep</t></card>');

// 白名单外
let e; try { renderAIRoot({ component: 'Evil', props: {} }, registry); } catch (x) { e = x; }
console.log(/unknown-component.*Evil/.test(e.message));
// props 校验
e = null; try { renderAIRoot({ component: 'Card', props: {} }, registry); } catch (x) { e = x; }
console.log(/invalid-props.*title/.test(e.message));

// 深度限制
const deep = (n) => n === 0 ? { component: 'Text', props: {} }
  : { component: 'Card', props: { title: 'x' }, children: [deep(n - 1)] };
e = null; try { renderAIRoot(deep(10), registry, { maxDepth: 3 }); } catch (x) { e = x; }
console.log(/depth-exceeded/.test(e.message));

// 节点上限
const wide = { component: 'Card', props: { title: 'x' },
  children: Array.from({ length: 150 }, () => ({ component: 'Text', props: {} })) };
e = null; try { renderAIRoot(wide, registry, { maxNodes: 100 }); } catch (x) { e = x; }
console.log(/too-many-nodes/.test(e.message));

// 空 children
r = renderAIRoot({ component: 'Card', props: { title: 'x' }, children: [] }, registry);
console.log(r === '<card>Hi</card>');
```

**评分点**：
- 白名单 + props schema 双校验（LLM 输出的约束化——RBL-934 注入面收敛）
- 深度与节点数上限（LLM 生成树的 DoS 防护——资源限制 RBL-557 的生成版）
- 递归渲染 + 路径定位（错误信息可定位到树中位置——诊断体验）
- 能说清「LLM 输出组件引用而非 HTML：生成自由度收敛到合法组件+合法 props 的组合」属于加分
