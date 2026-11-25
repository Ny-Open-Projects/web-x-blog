---
title: [WEB-631] 笔试：手写 WASM 加载器（流式 + 完整性校验 + 缓存）
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebAssembly]
type: 笔试题
---

## WEB-631：笔试：手写 WASM 加载器（流式 + 完整性校验 + 缓存）

**答**：实现 `loadWasm(url, expectHash)`：① fetch 后先校验 SHA-256 与期望哈希（不匹配抛错拒载）；② 校验通过走 `compileStreaming`，MIME 异常降级 arrayBuffer 编译；③ 编译产物 Module 存 IndexedDB（key 带 url+hash），命中缓存免编译免下载；④ 实例化时注入白名单 imports；⑤ 加载各阶段（download/compile/instantiate）耗时打点返回。写出核心实现。

```javascript
const enc = new TextEncoder();

async function sha256Hex(bytes) {
  const d = await crypto.subtle.digest('SHA-256', bytes);
  return [...new Uint8Array(d)].map(b => b.toString(16).padStart(2, '0')).join('');
}

async function loadWasm(url, expectHash, imports = {}) {
  const cacheKey = `wasm:${url}:${expectHash.slice(0, 12)}`;
  const cached = await idbGet(cacheKey);
  if (cached) return { module: cached, timings: { download: 0, compile: 0 } };

  const t0 = performance.now();
  const res = await fetch(url);
  const bytes = new Uint8Array(await res.arrayBuffer());
  const download = performance.now() - t0;

  const hash = await sha256Hex(bytes);
  if (hash !== expectHash) throw new Error(`wasm integrity fail: ${hash}`);

  const t1 = performance.now();
  let module;
  try { module = await WebAssembly.compileStreaming(new Blob([bytes]).stream()); }
  catch { module = await WebAssembly.compile(bytes); } // MIME/流式不支持降级
  const compile = performance.now() - t1;

  await idbSet(cacheKey, module);              // 结构化克隆支持 Module
  const instance = await WebAssembly.instantiate(module, imports);
  return { module, instance, timings: { download, compile } };
}
```

**评分点**：
- 校验在前、实例化在后（防篡改二进制进运行时）
- 流式编译降级路径处理 MIME 与兼容性
- Module 存 IndexedDB 且 key 绑定版本 hash
- 阶段耗时打点支撑冷启动归因
