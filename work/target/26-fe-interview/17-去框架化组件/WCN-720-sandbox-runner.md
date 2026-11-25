---
title: [WCN-720] 笔试：手写 live preview 的沙箱脚本执行器（iframe postMessage）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-720：笔试：手写 live preview 的沙箱脚本执行器（iframe postMessage）

**答**：
- 需求：实现 `createSandbox(container)` 返回 `{ run(code), onError(cb), destroy() }`：创建 sandbox iframe，run 通过 postMessage 注入代码执行，错误回传父页；destroy 清理监听与 DOM。
- 要点：用唯一 id 区分消息来源；校验 event.source === iframe.contentWindow 防伪造；错误回调用 Set 管理多订阅；边界：iframe 未就绪时缓存待执行代码。

```javascript
function createSandbox(container) {
  const frame = document.createElement('iframe');
  frame.setAttribute('sandbox', 'allow-scripts');
  frame.srcdoc = `<script>
    window.addEventListener('message', (e) => {
      if (e.data?.type === 'RUN') {
        try { new Function(e.data.code)(); }
        catch (err) { parent.postMessage({ type: 'ERR', id: e.data.id, msg: String(err) }, '*'); }
      }
    });<\/script>`;
  container.appendChild(frame);
  const listeners = new Set();
  let seq = 0;
  function onMessage(e) {
    if (e.source !== frame.contentWindow) return;        // 校验来源
    if (e.data?.type === 'ERR') listeners.forEach((cb) => cb(e.data.msg));
  }
  window.addEventListener('message', onMessage);
  return {
    run(code) {
      frame.contentWindow.postMessage({ type: 'RUN', id: ++seq, code }, '*');
    },
    onError(cb) { listeners.add(cb); },
    destroy() {
      window.removeEventListener('message', onMessage);
      listeners.clear(); frame.remove();
    },
  };
}
console.log(typeof createSandbox);
```

**评分点**：
- 用 event.source 校验消息来源，防止其他窗口伪造消息。
- run/onError/destroy 生命周期完整，destroy 清理监听与 DOM（无泄漏）。
- 错误通过 postMessage 回传并支持多订阅回调。
- sandbox 属性隔离执行环境，避免污染宿主页。
