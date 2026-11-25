---
title: [RBL-908] 综合深水：小程序目标的构建约束——分包/双线程/包体积的特殊管线
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-908：综合深水：小程序目标的构建约束——分包与双线程的特殊管线

**答**:
- 小程序构建与 web 的三大差异：1) **包体积硬约束**（主包 2MB/总包 30MB——平台强制，超限无法上传：体积预算是硬门禁不是建议 RBL-662 的极端形态）；2) **分包结构**（主包 + 分包目录，分包间引用受限——chunk 分割被平台结构约束：入口页必须在主包、跨分包 import 有限制——分割算法要遵守平台规则 RBL-596 的平台特化）；3) **双线程渲染**（逻辑层 JS 与渲染层分离——WXS/Skyline 的特殊语法需要构建器支持，DOM API 全禁用）。
- 构建器的适配：1) 分包感知的 chunk 归属（页面路由 → 分包映射，闭包按分包切割——跨分包公共模块的放置决策：主包 or 分包副本）；2) 双线程语法处理（wxml/wxs 的编译管线独立于 JS——构建器多语言管线）；3) 环境守卫（window/document 在小程序逻辑层不存在——RBL-779 式边界审计：wx API 才是合法全局）。
- 预渲染与资源内联：小程序图片走网络（无本地文件系统）——静态资源 base64/CDN 决策的体积影响直接计入包体积。
- 追问钩子：为什么小程序的「平台结构约束」让通用 chunk 算法失效？——rollup 式算法假设「产物结构自由」（chunk 任意划分），小程序要求「分包=物理目录+加载边界+平台校验」——算法必须把平台约束作为硬边界（分包不可分割 SCC 的平台版）；这揭示构建器的通用规律：「产物结构的自由度」决定算法选择——自由度越低，算法越要「约束感知」。

```javascript
// 分包感知的 chunk 归属
const SUBPKG_RULES = {
  mainMaxKB: 2048, subMaxKB: 2048, totalMaxKB: 30720,
  entryMustBeMain: true,
};
function assignSubPackages(graph, routes, subpkgConfig) {
  const owner = new Map();
  for (const [route, pkgName] of Object.entries(subpkgConfig))
    for (const m of graph.closureOf(route))
      owner.set(m, pkgName);                             // 页面闭包归分包
  // 跨分包共享模块：引用计数决策（主包 or 复制）
  const refs = countRefs(owner);
  for (const [mod, count] of refs)
    if (count > 1) owner.set(mod, sizeOf(mod) > 30 ? 'main' : 'copy');
  // 硬校验：主包超限即失败（平台约束不可协商）
  const mainSize = sumBy(owner, 'main');
  if (mainSize > SUBPKG_RULES.mainMaxKB * 1024)
    fail(`主包 ${kb(mainSize)} 超平台上限——需下沉页面到分包`);
  return owner;
}
```
