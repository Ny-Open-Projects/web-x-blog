---
title: [TST-644] 前端 XSS 的自动化验证怎么做？
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-644：前端 XSS 的自动化验证怎么做？

**答**：
- 结论：按「注入点 × 上下文」做矩阵测试——同一 payload 在 HTML/属性/JS/URL 四种上下文表现不同。
- 把 payload 注入表单/URL 参数，断言 DOM 中没有新增 script 节点、没有执行标记。
- 用 CSP 报告端点做二次确认；对富文本走白名单净化器专项测试。
- 追问钩子：现代框架默认转义了，为什么还要专门测 XSS？

```javascript
const CONTEXTS = ['html', 'attr', 'js', 'url'];
const PAYLOADS = ['"><img src=x onerror=window.__xss=1>',
  'javascript:alert(1)', '</script><script>window.__xss=1'];
function xssMatrix(inject) {
  const cases = [];
  CONTEXTS.forEach(ctx => PAYLOADS.forEach(p => {
    inject(ctx, p);
    cases.push({ ctx, payload: p.slice(0, 20),
      executed: !!window.__xss });
    delete window.__xss;
  }));
  return cases.filter(c => c.executed);
}
// 断言：xssMatrix(inject).length === 0
```
