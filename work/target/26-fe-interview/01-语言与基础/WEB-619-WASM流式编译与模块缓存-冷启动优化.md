---
title: [WEB-619] WASM 流式编译与模块缓存：冷启动优化
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-619：WASM 流式编译与模块缓存：冷启动优化

**答**：
- 流式编译：`WebAssembly.instantiateStreaming(fetch(url), imports)` 边下载边编译，编译与网络并行，比先下完再编译省 30%+ 时间；前提是服务器正确返回 `application/wasm` MIME
- 编译缓存：`compileStreaming` 拿到 Module 后存 IndexedDB（结构化克隆支持 Module），下次启动免编译直接 instantiate——大模块（几 MB）收益显著
- 需要兜底：MIME 错误/浏览器不支持流式时降级 arrayBuffer → instantiate；IDB 缓存损坏时降级网络编译
- 加载策略：wasm 模块与 JS bundle 分开缓存管理，版本号进 URL，避免缓存脏模块
- 实测口径：冷启动 = 下载 + 编译 + 实例化 + 初始化数据，四段分别计时上报，定位哪段是瓶颈

```javascript
async function loadModule(url) {
  // 1) 尝试 IDB 缓存的已编译 Module
  const cached = await idbGet(`wasm:${url}`);
  if (cached) return cached;
  // 2) 流式编译(网络与编译并行), 失败降级
  let mod;
  try { mod = await WebAssembly.compileStreaming(fetch(url)); }
  catch { mod = await WebAssembly.compile(await (await fetch(url)).arrayBuffer()); }
  await idbSet(`wasm:${url}`, mod);       // 存编译产物, 下次免编译
  return mod;
}
```
