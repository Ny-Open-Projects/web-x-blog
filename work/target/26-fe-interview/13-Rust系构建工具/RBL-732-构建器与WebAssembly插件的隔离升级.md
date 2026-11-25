---
title: [RBL-732] WASM 插件的隔离升级：ABI 版本协商与插件热替换
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-732：WASM 插件的隔离升级：ABI 版本协商与插件热替换

**答**:
- WASM 插件（RBL-553/580）的升级难点：插件编译时绑定的核心 ABI（内存布局/导入函数签名）必须与运行时核心一致——「ABI 版本协商」协议：插件加载时声明 `abi_version`，核心按范围判定（major 必须相等，minor 核心向后兼容插件）；不兼容即拒绝加载并给出升级指引，而不是内存错乱。
- 热替换（dev server 场景插件更新）：插件 WASM 实例替换要保证「无在途调用」（等待当前钩子调用完成 → 替换实例 → 后续调用走新实例）；替换失败的回退（旧实例继续服务 + 告警）。热替换的价值是「改插件不用重启 dev server」。
- 隔离的资源语义：每个插件实例独立 WASM 内存——崩溃/泄漏不传染核心；但共享状态（如插件间传递的转换结果）要走核心中转（序列化），这是「隔离换通信」的固定成本。
- 升级的灰度：核心升级后插件矩阵测试（RBL-652 的反向——核心升级触发插件兼容扫描）；「插件兼容性报告」作为核心 release notes 的一部分（哪些插件确认兼容/已知问题）。
- 追问钩子：为什么 WASM 插件比 NAPI 插件更适合热替换与隔离？——WASM 实例是纯值对象（可整体丢弃重建），NAPI 插件与 Node 事件循环共享线程状态（替换会撕裂正在执行的调用）；代价是 WASM 的通信序列化成本——高频钩子的插件慎用 WASM。

```javascript
// ABI 协商与热替换
class WasmPluginHost {
  #plugins = new Map();
  load(name, wasmModule, { abiVersion }) {
    if (!this.coreAbiCompatible(abiVersion))
      throw new Error(`${name} ABI ${abiVersion} 与核心 ${this.coreAbi} 不兼容——请升级插件`);
    const instance = new WebAssembly.Instance(wasmModule, this.imports(name));
    this.#plugins.set(name, { instance, abiVersion, inflight: 0 });
  }
  async callHook(name, hook, ...args) {
    const p = this.#plugins.get(name);
    p.inflight++;
    try { return await this.invoke(p, hook, args); }
    finally { p.inflight--; }
  }
  async hotSwap(name, newModule, meta) {
    const old = this.#plugins.get(name);
    if (old.inflight > 0) await waitForDrain(old);          // 等在途调用清零
    try {
      const inst = new WebAssembly.Instance(newModule, this.imports(name));
      this.#plugins.set(name, { instance: inst, abiVersion: meta.abiVersion, inflight: 0 });
    } catch (e) {
      warn(`热替换失败，保留旧实例: ${e.message}`);          // 回退旧实例
    }
  }
}
```
