---
title: [RBL-412] 笔试：手写 Loader 链执行器（管道 + sourceMap 链）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-412：手写 Loader 链执行器
**需求**：实现 `runLoaderChain(loaders, { resource, code, map })`：1) loaders 按倒序执行（webpack 语义：数组末尾先执行）；2) 每个 loader 签名 `loader(code, map, meta)` 返回 code/map；3) sourcemap 链：loader 返回新 map 时与上游 map 级联（remap），未返回时保持上游 map；4) pitch 阶段支持（loader.pitch 先于正文，pitch 返回值短路后续 loader 与源文件读取）；5) meta 透传；6) 异常传播带 loader 名称。

```javascript
import SourceMap from 'source-map'   // 简化：假设 remap 工具可用

export async function runLoaderChain(loaders, ctx) {
  const { resource } = ctx
  let state = { code: ctx.code, map: ctx.map ?? null, meta: {} }
  const chain = [...loaders].reverse()                       // 末尾先执行

  for (const loader of chain) {
    // pitch 阶段：正序执行，返回值短路
    if (loader.pitch) {
      const pitched = await loader.pitch(state.meta, resource)
      if (pitched !== undefined) return pitched
    }
  }
  for (const loader of chain) {
    try {
      const result = await loader.call({ resource, data: state.meta }, state.code, state.map, state.meta)
      if (result === null || result === undefined) continue   // 返回空：保持上游
      if (typeof result === 'string') state = { ...state, code: result }
      else if (typeof result === 'object')
        state = {
          code: result.code ?? state.code,
          map: result.map ? remap(state.map, result.map) : state.map,   // 级联
          meta: state.meta,
        }
    } catch (e) {
      const err = new Error(`loader ${loader.name ?? 'anonymous'} failed: ${e.message}`)
      err.cause = e
      throw err
    }
  }
  return state
}

function remap(prevMap, newMap) {
  if (!prevMap) return newMap
  // 简化：实际用 remapping 库做两级 map 级联
  return newMap   // 占位：注明真实实现需 remapping
}
```
**评分点**：
- 倒序执行语义（webpack loader 数组末尾先跑）
- pitch 正序 + 短路语义（pitch 返回值跳过后续与源读取）
- sourcemap 链级联意识（remap 两级合并——实现可简化但必须点出）
- 错误包装带 loader 名（定位友好）；meta 跨 loader 透传（this.data）
