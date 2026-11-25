---
title: [RBL-411] 笔试：手写 WASM 插件的 JS 侧加载器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-411：手写 WASM 插件的 JS 侧加载器
**答**：实现 `loadWasmPlugin(wasmPath, allowedCaps)`：1) 实例化 wasm 模块（imports 注入宿主能力：白名单 fs.read/env.get——未声明能力调用即抛错）；2) 按插件导出的 hooks 列表生成 JS 插件对象（transform 等方法桥接到 wasm 导出）；3) 数据传递：code 写入 wasm 线性内存（exports.alloc + memory.write）→ 调用 hook → 读回结果（ptr+len）；4) 超时保护（同步 wasm 调用无法 abort——用 hook 级时间统计告警）；5) capabilities 元数据导出（插件声明的能力清单供审计）。

```javascript
import fs from 'node:fs'

export async function loadWasmPlugin(wasmPath, allowedCaps) {
  const { instance } = await WebAssembly.instantiate(fs.readFileSync(wasmPath), {
    host: {
      read_file: (pathPtr, len) => {
        if (!allowedCaps.includes('fs.read')) throw new Error('cap fs.read not granted')  // 能力白名单
        const p = readString(instance, pathPtr, len)
        return writeString(instance, fs.readFileSync(p).toString())
      },
      env_get: (keyPtr, len) => {
        if (!allowedCaps.includes('env')) throw new Error('cap env not granted')
        return writeString(instance, process.env[readString(instance, keyPtr, len)] ?? '')
      },
    },
  })
  const hooks = (instance.exports.__hooks ?? 'transform,renderChunk').split(',')
  const plugin = { name: instance.exports.__name?.() ?? 'wasm-plugin' }
  for (const hook of hooks) {
    plugin[hook] = (input) => {
      const t0 = performance.now()
      const inPtr = writeString(instance, JSON.stringify(input))
      const outPtr = instance.exports[`hook_${hook}`](inPtr)     // wasm 内返回 (ptr<<32|len) 或导出 getter
      const result = JSON.parse(readString(instance, outPtr >> 32, outPtr & 0xffffffff))
      const ms = performance.now() - t0
      if (ms > 1000) console.warn(`wasm hook ${hook} slow: ${ms}ms`)   // 超时告警
      return result
    }
  }
  plugin.capabilities = JSON.parse(instance.exports.__caps?.() ?? '[]')  // 能力审计
  return plugin
}

function writeString(inst, s) {
  const bytes = new TextEncoder().encode(s)
  const ptr = inst.exports.alloc(bytes.length)
  new Uint8Array(inst.exports.memory.buffer, ptr, bytes.length).set(bytes)
  return (ptr << 32) | bytes.length
}
function readString(inst, ptr, len) {
  return new TextDecoder().decode(new Uint8Array(inst.exports.memory.buffer, ptr, len))
}
```
**评分点**：
- 能力白名单在宿主注入层强制（未授权调用即抛错——能力安全的核心实现点）
- 线性内存读写协议（alloc + ptr/len 编码）与字符串编解码正确
- 同步 wasm 调用不可 abort 的诚实处理（超时只能告警——指出 wasm 限制是加分项）
- capabilities 元数据导出供审计（供应链插件审能力清单）
