---
title: [BLD-165] 动态 import 的运行时实现：webpack jsonp loadScript 的源码级解读。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-165：动态 import 的运行时实现：webpack jsonp loadScript 的源码级解读。
**答**：
- `import('./lazy')` 编译为 `__webpack_require__.e("lazy_chunk").then(() => __webpack_require__.t("./lazy.js", 0))`：`.e` 负责加载 chunk 文件（script/jsonp），`.t` 负责 interop 取模块。
- 加载内核：`__webpack_require__.l`（loadScript）创建 `<script src=publicPath+chunkId.contenthash.js>`，通过 `onScriptComplete` 监听 load/error；chunk 真正的"加载完成"信号是文件尾部的 `webpackChunk.push([chunkIds, modules])` 把 `installedChunks[chunkId]` 的 promise resolve 掉。
- 错误处理：script onerror → reject promise → **删除失败 script 标签**（允许重试）、chunk 加载失败标记 `installedChunks[chunkId] = undefined` 可再次尝试；上线发版后旧 hash 404 的"动态路由白屏"就是这里 reject 未被 catch。
- 面试要点：contenthash 文件名 + `document.head.appendChild` 时序 + promise 状态机三层讲清；对比 vite 的 import() 运行时（原生 ESM，无需 preload 机制，dev 下没有 chunk 加载这一步）。

```javascript
// dist/runtime（LoadScriptRuntimeModule + chunk loading，逐行注释版）
var installedChunks = { main: 0 };   // 0=已加载；数组=[resolve,reject]；undefined=失败可重试

// ① script 加载器：promise 化的动态 script 注入
__webpack_require__.l = (url, done, key, chunkId) => {
  if (inProgress[url]) { inProgress[url].push(done); return; }
  var script, needAttach;
  var onScriptComplete = (prev, event) => {
    if (script.readyState && script.readyState !== 'complete' && script.readyState !== 'loaded') return;
    clearTimeout(timeout);                                  // ② 120s 超时兜底（__webpack_chunk_load_timeout__）
    var scriptDone = event && (event.type === 'load' ? 'complete' : 'error');
    // error 时清理：允许 promise retry 重新注入 script
    if (scriptDone === 'error') { /* remove script node */ }
    done && done(scriptDone, event);
  };
  // ③ 创建 script：contenthash 文件名 + crossorigin + charset
  script = document.createElement('script');
  script.src = url;                                          // __webpack_require__.p + "js/" + chunkId + "." + hash + ".js"
  inProgress[url] = [done];
  needAttach && document.head.appendChild(script);
};

// ④ ensureChunk：查状态机 → 未加载则拼 url 并挂 f.j 回调
__webpack_require__.e = (chunkId) => Promise.all(
  Object.keys(__webpack_require__.f).reduce((promises, key) => {
    __webpack_require__.f[key](chunkId, promises);
    return promises;
  }, [])
);
__webpack_require__.f.j = (chunkId, promises) => {
  var installed = installedChunks[chunkId];
  if (installed !== 0) {
    if (installed) promises.push(installed[2]);              // 加载中：复用同一 promise
    else promises.push(installedChunks[chunkId] = new Promise((resolve, reject) => {
      var url = __webpack_require__.p + "js/" + ({}[chunkId] || chunkId) + "." + { "lazy": "8f3c" }[chunkId] + ".chunk.js";
      __webpack_require__.l(url, (status, event) => {
        if (status !== 'complete') {                         // ⑤ 失败：清状态可重试
          delete installedChunks[chunkId];
          script.onerror = script.onload = null; clearTimeout(timeout);
          reject(new Error('Loading chunk ' + chunkId + ' failed.\n(' + status + ')'));
        } else resolve();                                    // 成功由 chunk 尾部 webpackChunk.push 兜底 resolve
      });
      var timeout = setTimeout(() => __webpack_require__.l(url, null, null, chunkId, 'timeout'), 120000);
    }));
  }
};

// 业务侧最佳实践：动态 import 必须有失败降级（发版后旧 hash 404 的标准解法）
// const mod = await import('./lazy').catch(() => location.reload());  // chunk 404 → 整页刷新拿新 manifest
```
