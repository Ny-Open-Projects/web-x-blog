---
title: [WEB-618] Emscripten 胶水代码做了什么，什么时候该手写
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-618：Emscripten 胶水代码做了什么，什么时候该手写

**答**：
- Emscripten 胶水（.js loader）职责：实例化 wasm、维护堆视图（HEAPU8 等）、C/C++ 字符串/指针与 JS 互转（UTF8ToString/stringToUTF8）、文件系统模拟（MEMFS）、异常与 malloc/free 封装
- 体积与启动代价：胶水 JS 通常几十~几百 KB 且包含大量兼容分支；包体积敏感场景（首屏 SDK）胶水成本可能超过 wasm 本体
- 手写胶水的时机：只用固定几个导出函数 + 纯数值/字节数据交互时，手写 50 行 loader 比 Emscripten 全家桶干净得多——自己管理实例化、内存分配、字符串编解码
- 字符串互转手写要点：JS 字符串 TextEncoder 编码进线性内存 + 传长度；返回时按 UTF-8 从内存解码，注意字节长度而非字符数
- 折中方案：Emscripten 用 `-s MINIMAL_RUNTIME` / `-s ENVIRONMENT=web` 裁剪输出，或 Rust wasm-bindgen 生成更小的绑定

```javascript
// 手写最小 loader
async function loadWasm(url) {
  const { instance } = await WebAssembly.instantiateStreaming(fetch(url), { env: { abort: () => {} } });
  const { memory, alloc, free, process } = instance.exports;
  const enc = new TextEncoder(), dec = new TextDecoder();
  return {
    process(str) {
      const bytes = enc.encode(str);
      const ptr = alloc(bytes.length);
      new Uint8Array(memory.buffer, ptr, bytes.length).set(bytes);
      const outPtr = process(ptr, bytes.length);
      // 假设导出 out_len: 返回结果按约定解码
      return dec.decode(new Uint8Array(memory.buffer, outPtr, instance.exports.out_len()));
    },
  };
}
```
