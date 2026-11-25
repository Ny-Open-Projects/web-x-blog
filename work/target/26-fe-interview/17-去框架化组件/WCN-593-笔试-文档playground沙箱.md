---
title: [WCN-593] 笔试：实现「文档 playground」的在线编辑器沙箱（代码编译 + iframe 隔离 + 错误捕获）。
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-593：笔试：实现「文档 playground」的在线编辑器沙箱（代码编译 + iframe 隔离 + 错误捕获）。

**答**：
- 结论：沙箱接收用户代码，经编译（ESM 转译 + 依赖映射）后注入 sandbox iframe 执行，捕获错误与 console。
- 用 srcdoc + sandbox 属性隔离，postMessage 回传运行结果与错误。
- 代码编译失败（语法错误）直接回传错误，不执行。
- 追问：如何支持 import 裸模块？（答：importmap 映射到 CDN URL，在 iframe 内注入）

```javascript
function compile(code, version) {
  try { new Function(code); } catch (e) { return { ok: false, error: String(e) }; }
  return { ok: true, html: `<!doctype html><script type="importmap">
    {"imports":{"@ds/":"/ds/${version}/"}}<\/script>
    <div id="app"></div><script type="module">
    const ctx = { log: (...a) => parent.postMessage({t:'log',a},'*') };
    try { ${code} } catch(e) { parent.postMessage({t:'error',msg:String(e)},'*'); }
    <\/script>` };
}
function mountSandbox(code, version) {
  const res = compile(code, version);
  const f = document.createElement('iframe'); f.sandbox = 'allow-scripts';
  f.srcdoc = res.ok ? res.html : `<pre>${res.error}</pre>`;
  return f;
}
```

**评分点**：
- 代码编译与语法预检
- sandbox iframe 隔离
- 错误/日志 postMessage 回传
- importmap 裸模块映射
