---
title: [PER-1093] WASM 模块的安全考量
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1093：WASM 模块的安全考量

**答**：
- WASM 与 JS 同权限（同 CSP 约束下的网络/DOM 访问），不因二进制更"安全"；导入函数面即攻击面。
- 来源校验：WASM 二进制必须签名/哈希校验（供应链），CSP 加 script-src 或 wasm-unsafe-eval 控制。
- 内存安全：Rust/编译型语言内存安全优于手写 C；避免 wasm 层处理未校验输入直接进入系统调用。
- 隔离：不可信 WASM 用 Worker + 限制导入面（只暴露纯计算函数）。

```javascript
async function loadWasmSecure(url, expectedHash) {
  const buf = await (await fetch(url)).arrayBuffer();
  const hashBuf = await crypto.subtle.digest('SHA-256', buf);
  const hash = [...new Uint8Array(hashBuf)].map(b => b.toString(16).padStart(2, '0')).join('');
  if (hash !== expectedHash) throw new Error('wasm integrity fail');  // 防篡改
  return WebAssembly.instantiate(buf, {
    env: { log: console.log },        // 最小导入面
  });
}
// CSP 需含 'wasm-unsafe-eval'，其余 eval 依旧禁止
```
