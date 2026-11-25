---
title: [RBL-684] 场景题：SDK 产物分发策略——一份源码五种环境形态的构建矩阵
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-684：场景题：SDK 产物分发策略——一份源码五种环境形态的构建矩阵

**答**:
- SDK（埋点/支付/客服组件）要同时服务五种形态：1) ESM bundle（现代 SPA，minified + hash）；2) UMD/IIFE（传统页面 + CDN script 直引，全局变量挂载）；3) CJS（Node 服务端调用）；4) AMD/require（老系统）；5) es5 降级包（老 WebView 兜底）。构建矩阵 = 格式 × 目标语法 × 副作用策略，由构建器矩阵驱动（一个 config 数组循环产出）。
- 矩阵的关键差异配置：external 策略（UMD 全内联自包含 vs ESM external peer 依赖，RBL-604/605）；minify（CDN 包开、npm 包关——让下游 bundle 工具再处理）；sourcemap（CDN 包开且上传监控平台；npm 包关省体积）。
- 版本与分发通道：npm 包 semver 治理（外部开发者）+ CDN 固定版本 URL（内部页直引——URL 带 patch 版本实现「锁定发布」）；「latest」别名 URL 的灰度窗口（发布后先只对白名单租户解析到新版本）。
- 一致性验证：矩阵产物必须行为一致（RBL-655 E2E）——同一测试集对五种形态各跑一遍；差异仅允许在降级包（es5 语法路径不同但语义同）。
- 追问钩子：为什么 UMD 包选择「全内联」而 ESM 选择 external？——UMD 的使用场景是「script 直引、无打包工具」，external 无意义且会造成运行时全局查找失败；ESM 的使用者有 bundle 工具，external 让版本由宿主决定（防多实例）。形态决定策略，不是统一配置。

```javascript
// SDK 构建矩阵
const MATRIX = [
  { format: 'esm', target: 'es2019', external: ['react'], minify: true, sourcemap: 'external' },
  { format: 'iife', target: 'es2019', external: [], minify: true, sourcemap: 'external' }, // UMD 全内联
  { format: 'cjs', target: 'es2019', external: [], minify: false, sourcemap: false },
  { format: 'esm', target: 'es5', external: [], minify: true, sourcemap: false },          // 降级包
];

async function buildSDK() {
  const outputs = [];
  for (const variant of MATRIX) {
    outputs.push(await build({
      input: 'src/index.ts',
      format: variant.format,
      target: variant.target,
      external: variant.external,
      minify: variant.minify,
      sourcemap: variant.sourcemap,
      globals: variant.format === 'iife' ? { react: 'React' } : undefined,
      outDir: `dist/${variant.format}-${variant.target}`,
    }));
  }
  await verifyMatrixConsistency(outputs);                // 五形态行为一致
  await uploadSourcemaps(outputs.filter(o => o.sourcemap)); // 监控平台版本绑定
}
```
