---
title: [RBL-219] Rolldown 插件开发的钩子模型（Rollup 兼容面）
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-219：Rolldown 插件开发的钩子模型（Rollup 兼容面）

**答**:
- 兼容 Rollup 钩子模型：resolveId（解析路径）/load（返回源码）/transform（转换）/renderChunk（产物级转换）/generateBundle（最终产物）
- 执行顺序：resolveId→load→transform（每模块），renderChunk（每 chunk），generateBundle（一次）；enforce pre/post 控制与内置插件的先后
- Rust 侧的差异化：高频钩子（transform）跨边界有成本，Rolldown 支持 Rust 插件（native plugin）承接超高频转换
- 开发建议：先用 JS 插件（生态成熟），profiling 显示 transform 热点再下沉 Rust 插件

```javascript
export default function myPlugin() {
  return {
    name: 'my-plugin',
    enforce: 'pre',
    transform(code, id) {
      if (!id.endsWith('.svg')) return null            // null = 不处理
      return { code: `export default ${JSON.stringify(svgToComponent(code))}`, map: null }
    },
    renderChunk(code, chunk) { return code.replace(/__VERSION__/g, version) },
  }
}
```
