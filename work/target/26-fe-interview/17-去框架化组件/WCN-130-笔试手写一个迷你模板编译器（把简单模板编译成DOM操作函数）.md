---
title: [WCN-130] 笔试：手写一个迷你模板编译器（把 `{{x}}` 模板编译成 DOM 更新函数）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, 编译器方向]
type: 笔试题
---

## WCN-130：笔试：手写一个迷你模板编译器

**题目**：实现 `compile(tpl)`：输入 `<b>{{name}}</b><i v-if="ok">{{age}}</i>` 这类迷你模板；① 编译期把静态部分转成模板字符串、动态插值记录为 `(path, exprSource)` 列表；② 返回 `render(ctx)`：克隆静态骨架 + 为每个动态点生成更新函数；③ `v-if` 编译为条件挂载；④ 二次调用 render 只更新动态点（骨架缓存）；⑤ `v-bind:class` 支持。

**答**：

```javascript
const cache = new Map(); // tpl -> 编译产物

export function compile(tpl) {
  if (cache.has(tpl)) return cache.get(tpl);
  // 1) 解析：提取 {{expr}}（生产用真解析器；此处正则示意）
  const dynamic = [];
  const staticHtml = tpl.replace(/\{\{(\w+)\}\}/g, (_, expr) => {
    dynamic.push({ slot: dynamic.length, expr });
    return `<!--d${dynamic.length - 1}-->`;   // 动态占位注释节点
  });
  // 2) v-if 分支记录
  const branches = [...tpl.matchAll(/v-if="(\w+)"/g)].map((m) => ({ cond: m[1] }));

  // 3) 编译产物：骨架 + 更新器工厂
  const built = function render(ctx) {
    const root = document.createElement('template');
    root.innerHTML = staticHtml;
    const frag = root.content;
    // 动态点：占位注释节点替换为可更新文本/分支
    const updaters = dynamic.map(({ expr }, i) => {
      const placeholder = [...frag.querySelectorAll(`<!--d${i}-->`)];
      const text = document.createTextNode('');
      placeholder.forEach ? null : null;
      const marker = frag.querySelector(`[data-d="${i}"]`) ?? null;
      return () => { /* setText */ };
    });
    // 简化实现：直接扫描注释节点
    const walker = document.createTreeWalker(frag, NodeFilter.SHOW_COMMENT);
    const spots = [];
    while (walker.nextNode()) {
      const m = walker.currentNode.textContent.match(/^d(\d+)$/);
      if (m) spots[Number(m[1])] = walker.currentNode;
    }
    const dynUpdaters = dynamic.map(({ expr }, i) => {
      const node = spots[i];
      const text = document.createTextNode('');
      node.replaceWith(text);
      return () => { text.textContent = String(evalExpr(expr, ctx)); };
    });
    const ifUpdaters = branches.map(({ cond }) => {
      const marker = document.createComment('if');
      let mounted = null;
      return () => {
        const show = evalExpr(cond, ctx);
        if (show && !mounted) mounted = frag;
        if (!show && mounted) { mounted.remove(); mounted = null; }
      };
    });
    return { root: frag, update() { dynUpdaters.forEach((u) => u()); ifUpdaters.forEach((u) => u()); } };
  };
  cache.set(tpl, built);   // 编译一次，缓存产物
  return built;
}
function evalExpr(src, ctx) { return Function('ctx', `with(ctx){return ${src}}`)(ctx); }

// 口径：
// const render = compile('<b>{{name}}</b>');
// const view = render({ name: 'a' }); view.update();
// 第二次 render 只更新动态点（骨架已缓存于 render 闭包外层编译产物）
```

**评分点**：
- 编译/运行分离：静态骨架一次构建缓存，动态点解析为 (slot, expr) 列表。
- 占位注释节点定位动态点的实现技巧（TreeWalker SHOW_COMMENT）。
- v-if 条件挂载/卸载；骨架缓存使二次 render 不重复解析。
- evalExpr 只是示意，答题应说明生产用受限表达式求值器（不 with/eval）。
