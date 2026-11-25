---
title: [RBL-295] Rspack 与 Module Federation 的构建协同细节
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-295：Rspack 与 Module Federation 的构建协同细节

**答**:
- MF 构建物：exposes（被消费的模块单独 chunk）+ shared（共享依赖版本仲裁 chunk）+ remote 入口——Rspack 完整支持且与 webpack MF 产物互通
- shared 仲裁构建期：版本配置（singleton/requiredVersion）决定运行时协商逻辑进产物；构建期错误（exposes 指向不存在模块）应 fail-fast
- 类型面：远程模块的 TS 类型用 @module-federation/enhanced 的类型下发（dts 联动构建）——类型缺失是 MF 开发体验最大痛点
- 协同实践：host 与 remote 构建版本对齐（shared 单例版本号一致），CI 校验 shared 依赖矩阵漂移

```javascript
new ModuleFederationPlugin({
  name: 'host',
  remotes: { shop: 'shop@http://cdn/remoteEntry.js' },
  shared: { react: { singleton: true, requiredVersion: deps.react } },
})
// CI 校验：各 MF 参与者 shared 版本矩阵一致性检查
```
