---
title: [WEB-599] 笔试：手写跨源隔离能力检测与降级封装
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 浏览器架构]
type: 笔试题
---

## WEB-599：笔试：手写跨源隔离能力检测与降级封装

**答**：实现 `withIsolation(feature)`：检测 `crossOriginIsolated` 决定能力分支：① isolated → 用 SharedArrayBuffer 版实现（多线程 WASM/Worker 共享内存）；② 非 isolated → 降级到 MessageChannel 传拷贝版本；③ 检测结果缓存模块级变量；④ 提供 `probeReport()` 输出诊断信息（isolated 状态、缺哪个头、SAB 可用性）帮助排查 COOP/COEP 配置。写出实现与诊断逻辑。

```javascript
let cached = null;

function isIsolated() {
  if (cached !== null) return cached;
  cached = typeof SharedArrayBuffer !== 'undefined'
    && self.crossOriginIsolated === true;
  return cached;
}

function withIsolation({ sharedImpl, fallbackImpl }) {
  return isIsolated() ? sharedImpl : fallbackImpl;
}

function probeReport() {
  const r = {
    crossOriginIsolated: self.crossOriginIsolated ?? false,
    sabAvailable: typeof SharedArrayBuffer !== 'undefined',
    ua: navigator.userAgent,
  };
  // 诊断: isolated=false 时最常见的缺失
  r.diagnosis = r.crossOriginIsolated ? 'ok'
    : !r.sabAvailable ? '旧浏览器/未启用站点隔离'
    : '缺 COOP/COEP 响应头 (需 COOP: same-origin + COEP: require-corp)';
  return r;
}

// 用法: 多线程 WASM 或 Worker 共享内存的自动降级
const pool = withIsolation({
  sharedImpl: () => new SharedMemoryPool(new SharedArrayBuffer(1024 * 1024)),
  fallbackImpl: () => new CopyMessagePool(), // MessageChannel 拷贝传输
});
```

**评分点**：
- 检测条件完整：crossOriginIsolated + SharedArrayBuffer 类型存在
- 模块级缓存避免重复判断；双实现分支注入
- 诊断输出能定位「缺哪个响应头」，体现 COOP/COEP 配置排障能力
- 能说明为什么 fallback 用拷贝传输（无 SAB 无法共享内存）
