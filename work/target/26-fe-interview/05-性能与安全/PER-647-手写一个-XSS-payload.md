---
title: [PER-647] 手写一个 XSS payload 回归测试集：payload 库 + 探针执行检测 + 上下文覆盖（HTML 属性/URL/CSS/JS）
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-647：手写一个 XSS payload 回归测试集：payload 库 + 探针执行检测 + 上下文覆盖（HTML 属性/URL/CSS/JS）

**答**：
- payload 按注入上下文分类：HTML 正文、属性值（引号闭合）、URL 属性（javascript:）、CSS（expression/url）、JS 字符串（引号逃逸）、mXSS 变异——上下文不覆盖的用例库测不出真实绕过。
- 探针机制：每个 payload 的执行载体用 `window.__xss_probe=1` 赋值代替 alert（无 UI 阻塞，可断言）；每用例渲染后检查探针是否置位。
- 要点：用例集与净化器版本绑定，升级净化器必须全量重跑；属性上下文要测单双引号与无引号三种闭合。
- 评分点：上下文分类与探针无阻塞断言。

```javascript

const CASES = [
  { ctx: 'html', p: '<img src=x onerror="window.__xss_probe=1">' },
  { ctx: 'attr-dq', p: '" onmouseover="window.__xss_probe=1' },
  { ctx: 'attr-sq', p: "' onmouseover='window.__xss_probe=1" },
  { ctx: 'url', p: 'javascript:window.__xss_probe=1' },
  { ctx: 'css', p: 'expression(window.__xss_probe=1)' },
  { ctx: 'js', p: "\'; window.__xss_probe=1; \'" },
  { ctx: 'mxss', p: '<noscript><p title="</noscript><img src=x onerror=window.__xss_probe=1>">' },
];
async function runXssSuite(renderFn, sanitizeFn) {
  const results = [];
  for (const c of CASES) {
    window.__xss_probe = 0;
    const safe = sanitizeFn(c.p);
    renderFn(safe);                                          // 注入到对应上下文
    await new Promise(r => setTimeout(r, 100));              // 等待可能的内联执行
    results.push({ ctx: c.ctx, escaped: !window.__xss_probe,
      output: safe.slice(0, 40) });
  }
  return { pass: results.every(r => r.escaped), results };
}
// CI：净化器升级 PR 必须附 runXssSuite 全绿截图
```
