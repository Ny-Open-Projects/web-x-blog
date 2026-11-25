---
title: [RBL-699] 场景题：SSR 预渲染产物协同——同构双产物的构建期约束
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-699：场景题：SSR 预渲染产物协同——同构双产物的构建期约束

**答**:
- SSR 构建产出两份产物：server bundle（Node 运行，CJS/ESM，含数据获取）与 client bundle（浏览器，hash chunk + manifest）——两份产物的一致性约束在构建期可校验：1) **manifest 对齐**（client chunk map 是 SSR 注水路径的依据，server 渲染引用的 chunk 必须在 manifest 里）；2) **同构边界诊断**（模块同时被打入双包且用了 window/document → 诊断 guard 位置）；3) 环境条件分支（`typeof window` 静态化替换）。
- 构建期可防的典型事故：client bundle 更新但 server manifest 过期（双产物构建非原子）——约束「双产物原子产出」（同一构建任务产出两包，版本号一致）；server bundle 引用旧 chunk 名（冷缓存窗口）的排查靠 manifest hash 关联。
- 预渲染（SSG）的构建流程：构建后跑「预渲染 worker」（headless 环境执行 server bundle 渲染出静态 HTML）——预渲染是构建的延伸阶段，失败要阻断发布（预渲染产物与运行时渲染不一致 = SEO 内容错乱）。
- external 与同构：server bundle external 全 node_modules（RBL-604），但「依赖含浏览器代码」时（如某 UI 库入口 import window）需要 polyfill 垫层或 alias 到 node 版本——构建器要提供「server alias」通道（如 vite 的 ssr.noExternal/ssr.resolve 配置）。
- 追问钩子：为什么 SSR 的构建约束比 SPA 多？——SPA 只有一个运行环境（浏览器），SSR 有两个且互相咬合（server 渲染的 HTML 被 client 注水）；不一致的错误（水合 mismatch）只在运行时暴露，构建期能校验的部分要尽量前置。

```javascript
// 双产物一致性校验
async function buildSSR({ client, server }) {
  const [clientOut, serverOut] = await Promise.all([
    buildClient(client), buildServer(server),
  ]);
  // 1) manifest 对齐
  for (const chunk of serverOut.referencedChunks)
    if (!clientOut.manifest.has(chunk))
      throw new Error(`SSR 引用的 chunk ${chunk} 不在 client manifest——双产物版本不一致`);
  // 2) 同构边界诊断
  for (const mod of serverOut.modules)
    if (mod.usesBrowserGlobal && !mod.hasGuard)
      warn(`${mod.id} 使用 window/document 但无环境守卫——水合风险`);
  // 3) 预渲染（构建延伸）
  const htmls = await prerender(serverOut, clientOut.manifest);
  return { ...clientOut, server: serverOut, prerendered: htmls };
}
// 版本原子性：clientOut.buildId === serverOut.buildId（同一次构建产出）
```
