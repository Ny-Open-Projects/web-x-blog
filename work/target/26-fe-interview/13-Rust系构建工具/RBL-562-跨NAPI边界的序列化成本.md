---
title: [RBL-562] NAPI 边界的序列化成本：JS 调 Rust 工具链的通信设计
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-562：NAPI 边界的序列化成本：JS 调 Rust 工具链的通信设计

**答**：
- JS↔Rust 每次跨边界都要做数据转换（JS object ↔ Rust struct），序列化成本常被低估：传一个完整 AST JSON 可能比 Rust 侧解析源码本身还慢——所以设计目标永远是「粗粒度调用、细粒度留在 Rust 内」。
- 三种通信形态：1) **函数调用型**（@swc/core：传字符串返回字符串，边界只过源码/配置，最廉价）；2) **对象共享型**（NAPI 的 ThreadSafeFunction/backreference，JS 持 Rust 侧句柄，避免拷贝但要管理生命周期与 GC 终结器）；3) **进程隔离型**（turbopack/rolldown 的 JS 回调走 TaskQueue，构建主循环在 Rust，JS 插件钩子是异步消息）。
- 关键权衡：插件钩子频率决定架构——每模块每钩子都跨边界（webpack 风格）在 Rust 工具里不可持续，所以 rolldown 把高频钩子（resolve/load/transform）设计为可下沉：没有 JS 插件介入时全走 Rust 快路径。
- GC 终结器（Finalizer）的坑：JS 侧对象回收时通知 Rust drop——但终结器回调时机不确定，Rust 侧资源（arena/临时文件）要设计成可显式 close + 终结器兜底。
- 追问钩子：为什么不统一走 shared array buffer？——AST 树形结构共享需要自研序列化协议，收益集中在「AST 跨边界」场景（prettier 类），构建场景源码字符串就够小。

```javascript
// 形态对比示意
// 1) 函数调用型：边界最小
const out = transformSync(src, options); // 只传 String in/out

// 2) 对象共享型：JS 持有 Rust 侧状态
class RustCache {
  #ptr;                       // Rust 侧对象句柄
  constructor() { this.#ptr = napi_create_cache(); }
  get(k) { return napi_cache_get(this.#ptr, k); } // 无拷贝，返回浅对象
  close() { napi_cache_free(this.#ptr); this.#ptr = null; } // 显式释放
  // 终结器兜底：JS GC 回收实例时 Rust 侧再 drop 一次
}

// 3) 进程内消息型（构建器主循环在 Rust）
await build({                       // Rust 是调用方
  resolve(id, importer) {           // JS 插件钩子 = ThreadSafeFunction
    return callJsHook('resolve', [id, importer]); // 异步消息往返
  },
});
// 快路径优化：无 JS 插件命中时跳过钩子分发，直接 Rust 内置 resolve
```
