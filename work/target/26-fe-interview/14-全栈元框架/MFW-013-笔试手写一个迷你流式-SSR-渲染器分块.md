---
title: [MFW-013] 笔试：手写迷你流式 SSR 渲染器（分块输出 + 占位替换）
date: 2026-11-17
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-013：笔试：手写迷你流式 SSR 渲染器（分块输出 + 占位替换）
**答**：实现 `streamRender(node, res)`：组件树中「异步组件」（返回 Promise 的函数组件）渲染时先输出 `<!--slot:N-->` 占位注释 + fallback HTML，继续渲染其余树；Promise resolve 后输出一段 `<script>` 把占位处替换为真实 HTML。边界：异常组件替换为错误占位；全部完成后输出结束标记。

```javascript
const { randomUUID } = require('crypto');

function esc(s) { return String(s).replace(/[&<>"]/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c])); }

async function* renderNode(node) {
  if (typeof node === 'string' || typeof node === 'number') { yield esc(node); return; }
  if (node == null) return;
  const { type, props = {} } = node;
  if (typeof type === 'function') {
    const out = type(props);
    if (out && typeof out.then === 'function') {
      // 异步组件：返回占位 id，由外层先 yield 占位，再等待真实内容
      const id = randomUUID();
      yield { suspend: id, promise: out };
      return;
    }
    yield* renderNode(out);
    return;
  }
  yield `<${type}>`;
  if (Array.isArray(props.children)) for (const c of props.children) yield* renderNode(c);
  else yield* renderNode(props.children);
  yield `</${type}>`;
}

async function streamRender(node, res) {
  res.setHeader('content-type', 'text/html; charset=utf-8');
  const pending = new Set();
  for await (const chunk of renderNode(node)) {
    if (chunk && chunk.suspend) {
      const { suspend: id, promise } = chunk;
      res.write(`<!--slot:${id}-->${esc('加载中…')}<!--/slot:${id}-->`);
      pending.add(id);
      promise.then(
        (html) => void (async () => {
          let buf = '';
          for await (const h of renderNode(html)) buf += h;
          // 到达后用脚本把占位内容替换为真实 HTML
          res.write(`<template id="t-${id}">${buf}</template>
<script>
  var s = document.querySelector('<!--slot:${id}-->'.replace('<!--','[data-slot="${id}"]')) ||
          document.createComment(''); // 兼容：真实实现中占位带 data-slot 属性
  var slot = document.querySelector('[data-slot="${id}"]');
  slot.replaceWith(document.getElementById('t-${id}').content);
  document.getElementById('t-${id}').remove();
</script>`);
        })(),
        (e) => res.write(`<div data-slot="${id}" class="error">出错了：${esc(e.message)}</div>`),
      ).finally(() => { pending.delete(id); if (!pending.size) res.end('<!--done-->'); });
    } else {
      res.write(chunk);
    }
  }
  if (!pending.size) res.end('<!--done-->');
}

module.exports = { streamRender };

// **评分点**
// 1. shell 先写、挂起位置只写占位 + fallback，其余树继续渲染（不阻塞）。
// 2. Promise 到达后用 inline script + template/replaceWith 完成客户端替换——理解 React 流式的真实机制。
// 3. 错误路径：Promise reject 时替换为错误占位，且流最终必须 end（不悬挂）。
// 4. 嵌套异步组件（占位内再占位）能处理或至少说明局限，加分。
```
