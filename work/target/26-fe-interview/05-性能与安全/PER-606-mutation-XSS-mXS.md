---
title: [PER-606] mutation XSS（mXSS）是什么？为什么净化后再渲染仍可能被绕过？
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-606：mutation XSS（mXSS）是什么？为什么净化后再渲染仍可能被绕过？

**答**：
- mXSS 的机制：payload 在字符串态是安全的（净化器看到的 DOM 树没问题），但浏览器解析/序列化往返（innerHTML 赋值 -> innerHTML 读出 -> 再赋值）过程中**重新解析**改变了结构，安全结构变异成可执行结构。
- 经典载体：`<svg>`/`<math>` 外来命名空间内的 `<style>` 内容、`<noscript>`（脚本开启/关闭时解析不同）、`<template>` 内容、注释被错误闭合、双引号属性在序列化时被重写。例如 `<noscript><p title="</noscript><img src=x onerror=alert(1)>">` 在某些往返中逃逸。
- 防御组合拳：净化后不要再走一遍 HTML 字符串往返"（避免 parse-serialize-parse）；对高危上下文（svg/math/noscript/template）直接从白名单剔除；用 DOMPurify 最新版（针对 mXSS 有专门修复）并升级要及时；CSP 做最后兜底。
- 检验方式：mXSS 用例集回归——净化器跑完再赋值两次 innerHTML，检查最终 DOM 是否出现 script/事件属性。

```javascript

// mXSS 回归用例集：净化 -> 赋值 -> 再读出 -> 再赋值，检查最终态
const MXSS_CASES = [
  '<noscript><p title="</noscript><img src=x onerror=alert(1)>">',
  '<svg><style><img src=x onerror=alert(1)></style></svg>',
  '<math><mtext><table><mglyph><style><!--</style><img src=x onerror=alert(1)>',
  '<form><math><mtext></form><form><mglyph><style></math><img src onerror=alert(1)>',
];
function mxssRegression(sanitizeFn) {
  return MXSS_CASES.map(payload => {
    let html = sanitizeFn(payload);
    const div = document.createElement('div');
    div.innerHTML = html;                                    // 第一次解析
    html = div.innerHTML;                                    // 序列化
    div.innerHTML = html;                                    // 第二次解析（变异点）
    const bad = div.querySelector('script, [onerror], [onclick]');
    return { payload: payload.slice(0, 30), mutated: !!bad,
      verdict: bad ? 'mXSS 变异成功，净化器有漏洞' : '安全' };
  });
}
// 防御落点：svg/math/noscript/template 进净化黑名单 + 升级 DOMPurify + CSP 兜底
```
