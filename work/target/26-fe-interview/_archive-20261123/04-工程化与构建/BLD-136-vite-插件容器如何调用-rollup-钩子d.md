---
title: [BLD-136] vite 插件容器如何调用 rollup 钩子？dev 下哪些钩子生效？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-136：vite 插件容器如何调用 rollup 钩子？dev 下哪些钩子生效？
**答**：
- vite 把 rollup 钩子容器化为 `pluginContainer`（源码 `pluginContainer.ts`）：按 `enforce: 'pre' | normal | 'post'` 排序插件，钩子统一支持"函数 / 对象带 handler+order"两种写法，调用逆序/顺序与 rollup 一致。
- dev 生效的钩子：**resolveId、load、transform**（每个请求都走）、transformIndexHtml（vite 扩展）、configureServer、handleHotUpdate（vite 扩展）；**不生效**：buildStart 部分生效? 实际 createServer 时也会调一遍 options/buildStart（模拟），但 **generateBundle/outputOptions/renderChunk 等产物期钩子只在 build 跑**——这是"插件 dev 正常 build 出错"的根因。
- 钩子返回值约定：resolveId 返回 null 表示不接管、返回 false 表示 external；transform 返回 `{ code, map }`，map 可为 null（丢失 sourcemap 会 warn）。
- 双插件体系（dev 用容器直调，build 交 rollup）的兼容写法：钩子写成 `{ handler, order: 'pre' }` 对象形式，两个引擎都能识别。

```javascript
// 一个"dev 与 build 双兼容"插件的完整骨架：标注每个钩子在两个模式下的生效时机
function myPlugin() {
  return {
    name: 'my-plugin',
    enforce: 'pre',                        // 排序：pre 插件最先 resolve/load/transform
    // ── vite 扩展钩子 ──
    configResolved(config) { console.log('config 定稿:', config.command); }, // dev/build 都跑
    configureServer(server) {              // 仅 dev：可挂自定义中间件
      server.middlewares.use('/__mock', (req, res) => res.end('{}'));
    },
    transformIndexHtml(html) { return html.replace('</head>', '<script src="/__mock"></script></head>'); }, // 仅 dev（build 用 transformIndexHtml 的 rollup 版亦可）
    handleHotUpdate({ file, server }) {    // 仅 dev：自定义 HMR 触发
      if (file.endsWith('.lang.json')) server.ws.send({ type: 'custom', event: 'lang-update' });
    },
    // ── rollup 生命周期钩子 ──
    buildStart() { this.info?.('build start'); },           // build 全量跑；dev 冷启动模拟跑一次
    resolveId(source) {                      // dev：每请求一次；build：每模块一次
      if (source === 'virtual:config') return '\0virtual:config';
      return null;                           // null = 不接管
    },
    load(id) {
      if (id === '\0virtual:config') return 'export default window.__CFG__';
    },
    transform(code, id) { return { code, map: null }; },     // 两模式都跑（最常用）
    renderChunk() { if (this.environment?.config.command === 'build') {/* 仅 build */} }, // 仅 build！
    generateBundle(_, bundle) { /* 仅 build：改产物唯一正位 */ },
  };
}
// 面试口诀：dev 只认 resolveId/load/transform + vite 扩展四件套；产物期钩子 build 专属。
```
