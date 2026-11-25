---
title: [RBL-892] 场景题：Web 安全头与构建的协同——CSP nonce/COOP/COEP 的产物注入
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-892：场景题：Web 安全头与构建的协同——CSP/COOP/COEP 注入

**答**:
- 安全头与构建产物的耦合点：1) **CSP**（nonce/MD5 hash 方式：script-src 'sha256-xxx'——hash 来自产物内容！产物变了 CSP 要重生成——构建器输出「每个脚本的 hash 清单」给网关注入 CSP；nonce 方式则要求 SSR 动态 RBL-791）；2) **COOP/COEP**（启用 crossOriginIsolated 的前提：所有资源带 CORP/COEP 头——含第三方脚本 RBL-882，SharedArrayBuffer 场景）；3) SRI（subresource integrity：script 的 integrity 属性 = 产物 hash——构建器生成）。
- 构建器的 CSP-hash 输出：manifest 里每个 js/css 的 sha256 → 网关模板生成 `script-src 'self' 'sha256-h1' 'sha256-h2'`——产物与 CSP 原子发布（RBL-694 顺序：CSP 更新后产物才能更新，否则被自己的 CSP 拦截——先宽后窄的切换窗口）。
- SRI 的边界：hash 文件名产物不需要 SRI（URL 即内容寻址）；跨域第三方 CDN 资源需要 SRI（完整性）——构建器按资源来源决策 SRI 注入。
- COEP 的兼容审计：启用 COEP = 所有子资源必须 CORP——第三方脚本不支持就挂——构建器审计第三方资源的 COEP 兼容清单（逐步收紧策略：report-only 先行）。
- 追问钩子：为什么「CSP hash 方式」要求产物与 CSP 原子切换？——hash 白名单指向具体产物内容：先发产物（新 hash 不在 CSP 中）= 脚本被拦白屏；先发 CSP（旧 hash 移除）= 旧产物被拦——顺序必须是「先宽 CSP（新旧 hash 都含）→ 发产物 → 收窄 CSP」；安全策略与产物的耦合是「发布顺序契约」的安全版（RBL-694），构建器输出 hash 清单是这套协议的数据基础。

```javascript
// 构建器生成 CSP hash 清单
function emitCspList(manifest) {
  const hashes = manifest.files
    .filter(f => /\.(js|css)$/.test(f.name) && !f.hash)   // 非 hash 文件名才需要 CSP hash
    .map(f => `'sha256-${sha256(f.content)}'`);
  return { 'script-src': ["'self'", ...scriptHashes], 'style-src': ["'self'", ...styleHashes] };
}
// 原子切换协议（宽→发→窄）
async function cspAwareDeploy(manifest, gateway) {
  const wide = cspUnion(oldCsp, newCsp);                 // 新旧 hash 并集
  await gateway.setCsp(wide);                            // 1. 放宽
  await deployArtifacts(manifest);                       // 2. 发产物（RBL-694 顺序）
  await gateway.setCsp(newCsp);                          // 3. 收窄
}
// SRI 注入决策
const sri = (f) => isCrossOrigin(f) ? { integrity: `sha256-${f.hash}`, crossorigin: 'anonymous' } : {};
// COEP 审计
function auditCoep(thirdParties) {
  return thirdParties.filter(t => !t.corp).map(t =>
    `${t.name} 无 CORP 头——COEP 启用后将被拦截（先 report-only 验证）`);
}
```
