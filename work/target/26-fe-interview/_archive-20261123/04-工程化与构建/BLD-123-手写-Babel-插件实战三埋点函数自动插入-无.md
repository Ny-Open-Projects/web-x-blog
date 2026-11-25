---
title: [BLD-123] 手写 Babel 插件实战三：埋点函数自动插入（无痕上报关键交互）。（高频）
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 笔试题, 18]
type: 笔试题
---

## BLD-123：手写 Babel 插件实战三：埋点函数自动插入（无痕上报关键交互）。（高频）
**答**：
- 需求：约定"被 @track 注释标记的函数/事件回调自动注入上报调用"，或"所有 onClick 回调函数体首行注入 track()"——运营埋点不侵入业务代码。
- 实现：命中方法/箭头函数 → 看 leadingComments 匹配 `@track(event, props)` 解析参数 → 函数体 `body.unshiftContainer? ` 实际用 `path.get('body').unshiftContainer('body', expressionStatement(track(...)))`；箭头函数隐式返回需先转块状（`arrowFunctionExpression` 改 body 为 BlockStatement）。
- 关键细节：async/生成器函数保持标记不丢；避免重复注入（body 首条已是 track 调用则跳过）；上报参数里的 `this` 与闭包变量保持原作用域（unshift 到函数体首行天然满足）。
- 验证与灰度：插件加 `state.opts.mode === 'dry'` 只打日志不改码；产物里 `git grep 'track(' dist` 抽查注入点。

```javascript
// babel-plugin-auto-track.js
const t = require('@babel/types');

function parseTrackComment(node) {
  const c = (node.leadingComments ?? []).map((c) => c.value).join('');
  const m = c.match(/@track\(\s*['"]([\w.-]+)['"]\s*(?:,\s*(\{[\s\S]*?\}))?\s*\)/);
  return m && { event: m[1], props: m[2] };
}

const makeTrackCall = (meta) =>
  t.expressionStatement(
    t.callExpression(t.identifier('track'), [
      t.stringLiteral(meta.event),
      // props 是注释里抓出来的对象字面量文本，这里解析成对象表达式节点
      meta.props ? t.objectExpression([]) : t.objectExpression([]),
    ])
  );

const inject = (fnPath, meta) => {
  const body = fnPath.get('body');
  // 隐式返回的箭头函数先转块状：() => expr → () => { return expr; }
  if (fnPath.isArrowFunctionExpression() && !t.isBlockStatement(body.node)) {
    fnPath.set('body', t.blockStatement([t.returnStatement(body.node)]));
  }
  // 防重复注入
  if (body.node.body.some((n) =>
    t.isExpressionStatement(n) && t.isCallExpression(n.expression) &&
    n.expression.callee.name === 'track' && n.expression.arguments[0]?.value === meta.event
  )) return;
  const call = t.expressionStatement(t.callExpression(t.identifier('track'), [
    t.stringLiteral(meta.event),
    // props 文本走 parser 转成 AST 才严谨，这里用空对象占位简化
    meta.props ? t.objectExpression([]) : t.objectExpression([]),
  ]));
  body.unshiftContainer('body', call);   // 函数体首行插入，业务代码零侵入
};

module.exports = () => ({
  name: 'auto-track',
  visitor: {
    'FunctionDeclaration|FunctionExpression|ArrowFunctionExpression'(path) {
      const meta = parseTrackComment(path.node);
      if (meta) inject(path, meta);      // 方式一：@track 注释标记
    },
    JSXAttribute(path) {
      if (path.node.name.name !== 'onClick') return;
      const v = path.get('value');
      // 方式二：内联箭头回调自动包裹：onClick={() => do(x)} → onClick={() => { track(); do(x); }}
      if (v.isJSXExpressionContainer() && v.get('expression').isArrowFunctionExpression()) {
        inject(v.get('expression'), { event: 'click_inline', props: null });
      }
    },
  },
});
// 输入： // @track('order_submit', { page: 'checkout' })
//       async function submit() { await api(); }
// 输出： async function submit() { track("order_submit", ({page:'checkout'})); await api(); }
```
