---
title: [NODE-057] hydration 数据注入时如何防止 XSS？
date: 2026-11-17
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-057：hydration 数据注入时如何防止 XSS？
**答**：
- SSR 把初始状态注入 HTML 通常用 `<script>window.__INITIAL_STATE__ = {...}</script>`。若状态含用户输入（如昵称 `</script><script>alert(1)</script>`），直接 JSON.stringify 会导致**闭合标签逃逸**，形成存储型 XSS。
- 标准防御：序列化后**转义 `<` → `\u003c`**（JSON 兼容转义，JSON.parse 无感知）；或 Base64 编码后客户端 decode。同时输出属性时不可用 `dangerouslySetInnerHTML` 承接未消毒数据。
- 附带：`Content-Security-Policy` 头做纵深防御；`__INITIAL_STATE__` 中剔除 token 等敏感信息（HTML 源码所有人可见）。

```javascript
const { renderToPipeableStream } = require('react-dom/server');

// 安全注入：转义 < 与 >，防 </script> 逃逸
function serializeState(state) {
  return JSON.stringify(state)
    .replace(/</g, '\\u003c')     // 关键：< 转成 unicode 转义，JSON.parse 原样还原
    .replace(/>/g, '\\u003e')
    .replace(/&/g, '\\u0026')     // 防 HTML 实体解析歧义
    .replace(/\u2028/g, '\\u2028') // 防 JS 语法层面的行分隔符报错
    .replace(/\u2029/g, '\\u2029');
}

function renderWithState(res, appElement, state) {
  const stream = renderToPipeableStream(
    <>
      <script
        dangerouslySetInnerHTML={{          // 唯一允许 raw 的位置，且内容已转义
          __html: `window.__INITIAL_STATE__ = JSON.parse(${JSON.stringify(serializeState(state))})`,
        }}
      />
      {appElement}
    </>,
    { onShellReady: () => stream.pipe(res) },
  );
}

// 攻击场景验证：用户昵称 = </script><script>steal()</script>
const state = { user: { name: '</script><script>steal()</script>' } };
console.log(serializeState(state));
// 输出含 \u003c/script\u003e → 不再闭合 script 标签 → JSON.parse 还原为纯字符串
```
