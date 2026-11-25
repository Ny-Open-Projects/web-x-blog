---
title: [WEB-623] WASM trap 与错误处理：JS 侧怎么接住
date: 2026-11-21
categories: [WEB与网络]
tags: [前端面试, 面试题, WebAssembly]
type: 面试题
---

## WEB-623：WASM trap 与错误处理：JS 侧怎么接住

**答**：
- trap 类型：越界访问内存、除零（整数）、不可达指令、调空表函数——表现为 JS 侧抛 `WebAssembly.RuntimeError`，一旦 trap 整个实例状态不可信，不能继续用
- 错误信息贫瘠：trap 栈只有 wasm 帧名（依赖 name section），业务错误码要自己设计——约定出口函数返回错误码或错误指针，而不是让内部 trap
- 防御策略：入口参数校验（长度/指针范围）放在 wasm 内部最前面；JS 侧包装层 try/catch trap 转换为业务错误对象，并丢弃/重建实例
- OOM 不是异常：memory.max 打满时 grow 抛 RangeError，属于可恢复错误（拒绝任务），与 trap 区分处理
- 监控：上报 trap 类型 + 调用链（JS 侧包装层记录 method/参数摘要），wasm 化 SDK 的崩溃率要与 JS 版本对比

```javascript
function wrapExports(instance, { onError }) {
  return new Proxy(instance.exports, {
    get(target, name) {
      const fn = target[name];
      if (typeof fn !== 'function') return fn;
      return (...args) => {
        try { return fn(...args); }
        catch (e) {
          if (e instanceof WebAssembly.RuntimeError) {
            onError?.({ trap: String(e), fn: name, args: args.map(a => typeof a) });
            throw new WasmFatalError(name, e); // 业务层按致命错误处理, 实例待重建
          }
          if (e instanceof RangeError) throw new WasmOOMError(name, e); // 内存满, 可拒绝任务
          throw e;
        }
      };
    },
  });
}
```
