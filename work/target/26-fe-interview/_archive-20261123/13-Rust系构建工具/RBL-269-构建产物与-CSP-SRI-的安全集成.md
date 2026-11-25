---
title: [RBL-269] 构建产物与 CSP/SRI 的安全集成
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-269：构建产物与 CSP/SRI 的安全集成

**答**:
- SRI（子资源完整性）：构建期对产物计算 hash 注入 html `<script integrity="sha384-...">`——CDN 劫持防护；hash 必须与最终部署内容一致（压缩后计算）
- CSP nonce/hash：动态生成的行内脚本（html 注入的 runtime）需要 CSP nonce 或 hash——构建工具与部署方协作生成 CSP 头
- 构建期供应链：lockfile 锁版本 + CI 安装校验（pnpm audit）+ 产物依赖树审计（license 检查）——安全左移到构建
- 工程要点：integrity 属性随 contenthash 变化重新计算；html 注入脚本与外部 chunk 分开处理

```javascript
// html 插件注入 SRI
compilation.hooks.processAssets.tap({ name: 'SRI', stage: 1000 }, (assets) => {
  const html = assets['index.html'].source().toString()
  const withSRI = html.replace(/<script src="(main\.[^"]+\.js)"/g, (_m, f) => {
    const hash = sha384(assets[f].source().buffer())
    return `<script src="${f}" integrity="sha384-${hash}"`
  })
  compilation.updateAsset('index.html', new RawSource(withSRI))
})
```
