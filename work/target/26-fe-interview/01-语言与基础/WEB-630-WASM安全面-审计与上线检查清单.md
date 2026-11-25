---
title: [WEB-630] WASM 安全面：审计与上线检查清单
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-630：WASM 安全面：审计与上线检查清单

**答**：
- 沙箱基线：wasm 运行在浏览器沙箱内、线性内存边界强制——wasm 本身不放大权限，风险主要来自「import 了什么」
- import 审计：实例化时传入的宿主函数是能力面（能 fetch/能读 DOM），第三方 wasm 模块 import 范围最小化；禁用未审计模块的任意 import
- 供应链：wasm 二进制难审（等价于二进制依赖），要锁定构建来源（可复现构建/CI 产出签名）、版本哈希入包校验
- SRI 与完整性：wasm 文件加 content hash 校验（SRI 不直接支持 wasm 加载，但可在 JS 侧 fetch 后校验 SHA 再 instantiate），防 CDN 篡改
- 资源限制：memory.max 防线性内存吃爆设备、任务超时与 Worker 终止、防止恶意输入触发超长计算（DoS 自身）

```javascript
async function safeInstantiate(url, allowedImports, maxPages = 256) {
  const bytes = new Uint8Array(await (await fetch(url)).arrayBuffer());
  const digest = await crypto.subtle.digest('SHA-256', bytes);
  if (btoa(String(...new Uint8Array(digest))) !== EXPECTED_HASH[url]) throw new Error('wasm integrity fail');
  const module = await WebAssembly.compile(bytes);
  // 只注入白名单 import, 越权直接实例化失败
  const instance = await WebAssembly.instantiate(module, buildImports(allowedImports));
  return instance;
}
```
