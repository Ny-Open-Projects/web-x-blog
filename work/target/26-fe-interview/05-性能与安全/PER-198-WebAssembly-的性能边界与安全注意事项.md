---
title: [PER-198] WebAssembly 的性能边界与安全注意事项？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-198：WebAssembly 的性能边界与安全注意事项？

**答**：
- 性能边界：纯计算密集（加解密/图像处理/解析器）wasm 收益 2-10 倍；**DOM/网络场景 wasm 无优势**——边界穿越（JS↔wasm 传值）本身有成本。
- 使用要点：流式编译（`compileStreaming`）边下边编；数据**批量搬运**（一次调用算完，不逐元素跨界）；`memory.grow` 会使旧 buffer detach，扩容后必须重新取 view。
- 安全注意：实例化时**限制导入面**（只暴露必要 env，不给 fs/net）；wasm 二进制同样过 SRI 与 CSP；从可信源分发并锁定版本。
- 加载体积：wasm 模块通常比等价 JS 小，但要防止"为了 wasm 而 wasm"——先宏基准证明 JS 版真是瓶颈。

```javascript
// WASM：重计算卸载到 wasm，但有加载成本与边界成本
export async function loadWasmModule(url) {
  // 1. 流式编译：边下载边编译
  const mod = await WebAssembly.compileStreaming(fetch(url));
  // 2. 安全：限制导入面，只暴露必要 env，不给 fs net 等危险导入
  return new WebAssembly.Instance(mod, {
    env: { memory: new WebAssembly.Memory({ initial: 64 }) },
  });
}

// 3. 数据批量搬运：一次调用算完，避免逐元素跨界调用
export function sumWasm(instance, data) {
  const { memory, sum } = instance.exports;
  const ptr = memory.buffer.byteLength;
  memory.grow(Math.ceil((data.length * 8) / 65536)); // 扩容后旧 buffer detach
  const view = new Float64Array(memory.buffer, ptr, data.length); // 必须重新取 view
  view.set(data);
  return sum(ptr, data.length);
}
// 边界结论：纯计算密集 wasm 收益 2-10 倍；DOM 与网络场景 wasm 无优势
```
