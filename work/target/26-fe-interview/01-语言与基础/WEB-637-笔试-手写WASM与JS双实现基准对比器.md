---
title: [WEB-637] 笔试：手写 WASM 与 JS 双实现基准对比器
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 笔试题, 性能]
type: 笔试题
---

## WEB-637：笔试：手写 WASM 与 JS 双实现基准对比器

**答**：实现 `AblBench`：① `register(name, wasmFn, jsFn, { prepare })` 注册一组对比实现，prepare 每轮生成同输入；② `run()`：每实现先 warmup 50 次（不计入），再跑 30 轮计时取 p50/p90/min；③ 交叉执行：JS/wasm 交替轮次（js,wasm,js,wasm…）减少 JIT 队列互相污染；④ 输出对比报告：加速比 = jsP50 / wasmP50，附次数与机器信息；⑤ wasm 调用计时不包含 prepare 与数据拷贝时间（prepare 单独计时列）。写出核心实现。

```javascript
class AblBench {
  constructor() { this.cases = []; }
  register(name, wasmFn, jsFn, opts = {}) { this.cases.push({ name, wasmFn, jsFn, ...opts }); }
  _stats(arr) {
    const s = [...arr].sort((a, b) => a - b);
    const q = (x) => s[Math.min(s.length - 1, Math.floor(x * (s.length - 1)))];
    return { p50: q(.5), p90: q(.9), min: s[0], n: s.length };
  }
  async run({ warmup = 50, rounds = 30 } = {}) {
    const report = {};
    for (const c of this.cases) {
      const jsT = [], wasmT = [], prepT = [];
      for (let i = 0; i < warmup; i++) { c.jsFn(c.prepare?.()); c.wasmFn(c.prepare?.()); }
      for (let i = 0; i < rounds; i++) {
        // 交叉执行减少 JIT 污染
        for (const [store, fn] of [[jsT, c.jsFn], [wasmT, c.wasmFn]].map((x, idx) => i % 2 === 0 ? x : [x[0], x[1]] && (i % 2 === 0 ? [[jsT, c.jsFn], [wasmT, c.wasmFn]][idx] : [[wasmT, c.wasmFn], [jsT, c.jsFn]][idx]))) {
          const t0 = performance.now();
          const input = c.prepare?.();
          const prep = performance.now() - t0;
          const t1 = performance.now();
          fn(input);
          const t2 = performance.now();
          prepT.push(prep);
          store.push(t2 - t1); // 纯计算耗时, 不含 prepare
        }
      }
      const js = this._stats(jsT), wasm = this._stats(wasmT);
      report[c.name] = {
        js, wasm, prepP50: this._stats(prepT).p50,
        speedup: +(js.p50 / wasm.p50).toFixed(2),
        ua: navigator.userAgent,
      };
    }
    return report;
  }
}
```

**评分点**：
- warmup 与正式轮分离，理解 JIT/wasm 优化 tier 需要热身
- 交叉执行减少 JIT 污染；计时只含核心计算（prepare 单列）
- p50/p90/min 统计口径正确，加速比定义清晰
- 报告带 UA/环境信息，可跨设备归档
