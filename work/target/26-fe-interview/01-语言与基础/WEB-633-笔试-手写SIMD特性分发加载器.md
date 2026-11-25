---
title: [WEB-633] 笔试：手写 SIMD 特性分发加载器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, WebAssembly]
type: 笔试题
---

## WEB-633：笔试：手写 SIMD 特性分发加载器

**答**：实现 `loadWithFeature(base, simd)`：同时给出基础版与 SIMD 版两个 wasm URL：① 先 `WebAssembly.validate(simdBytes)` 探测 SIMD 支持（编译 simd 模块做验证）；② 支持 → 加载 simd 版；不支持 → 加载 base 版；③ 探测结果缓存全局（同页面只探测一次）；④ 两种加载都走「下载+编译」并行优化，失败时互相降级（simd 失败回退 base）；⑤ 返回 `{ exports, simd }`。写出核心实现。

```javascript
let simdProbe = null;

async function probeSimd() {
  if (simdProbe !== null) return simdProbe;
  // 最小 SIMD 探测模块: (module (func (result v128) v128.const i32x4 0 0 0 0))
  const probeBytes = new Uint8Array([0,97,115,109,1,0,0,0, 1,5,1,96,0,1,123, 3,2,1,0, 10,22,1,20, 0,253,12, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 11]);
  try { simdProbe = WebAssembly.validate(probeBytes); }
  catch { simdProbe = false; }
  return simdProbe;
}

async function loadWithFeature(baseUrl, simdUrl) {
  const useSimd = await probeSimd();
  const tryLoad = async (url) =>
    WebAssembly.instantiateStreaming(fetch(url)).then(({ instance }) => instance.exports);
  try {
    const exports = await tryLoad(useSimd ? simdUrl : baseUrl);
    return { exports, simd: useSimd };
  } catch (e) {
    const exports = await tryLoad(useSimd ? baseUrl : simdUrl); // 主选失败回退另一版本
    return { exports, simd: !useSimd };
  }
}
```

**评分点**：
- 用最小二进制 validate 探测 SIMD（或 fetch 模块后 validate），探测结果缓存
- 特性分发选择逻辑正确，失败互为降级
- instantiateStreaming 网络编译并行
- 返回值带 simd 标记便于监控归因

## 变体与延伸（补充）

**变体与延伸**：

1. WebAssembly.validate 与直接编译探测的差别？ → validate 只校验字节是否合法、不实例化不执行，开销极小且对不支持的引擎返回 false，比编译完整业务模块更合适做探测。
2. 为什么用几十字节的最小模块而不是业务模块？ → 业务模块体积大，探测失败要重下重编代价高；最小 v128 模块既能判定 SIMD 支持又几乎不耗流量。
3. SIMD 支持在 Node 与浏览器完全一致吗？ → 不一致，底层同为 V8 但 Node 版本绑定的 V8 可能落后，部分 SIMD 指令与 relaxed-simd 支持度有差异，需按引擎版本而非环境类型判断。
