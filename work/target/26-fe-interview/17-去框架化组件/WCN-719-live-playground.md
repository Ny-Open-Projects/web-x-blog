---
title: [WCN-719] 组件文档站如何实现「示例可运行即可复制」的 live playground？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-719：组件文档站如何实现「示例可运行即可复制」的 live playground？

**答**：
- 结论：每个示例用 iframe sandbox 隔离执行，源码与预览双向绑定；用 postMessage 在父页与 iframe 间传递代码和错误，避免示例污染文档站本身。
- 编译器把 JSX/模板在 iframe 内即时转译（或预编译）；依赖走 CDN importmap；错误边界捕获并回显到控制台面板。
- 追问钩子：playground 里能访问父站点的 cookie/token 吗？考察 sandbox 安全边界与最小权限原则。

```javascript
// 父页：把代码发给 iframe 执行
const frame = document.querySelector('#preview');
function run(code) {
  frame.contentWindow.postMessage({ type: 'RUN', code }, '*');
}
window.addEventListener('message', (e) => {
  if (e.data?.type === 'ERROR') console.error('示例运行错误:', e.data.msg);
});
run(`document.body.innerHTML = '<ds-button>点我</ds-button>';`);
// iframe 内
window.addEventListener('message', (e) => {
  if (e.data?.type === 'RUN') {
    try { new Function(e.data.code)(); }
    catch (err) { parent.postMessage({ type: 'ERROR', msg: String(err) }, '*'); }
  }
});
```
