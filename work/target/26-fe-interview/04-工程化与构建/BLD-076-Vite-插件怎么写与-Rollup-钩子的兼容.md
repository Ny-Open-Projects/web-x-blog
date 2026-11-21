---
title: [BLD-076] Vite 插件怎么写？与 Rollup 钩子的兼容、enforce pre/post、Vite 独有钩子有哪些？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-076：Vite 插件怎么写？与 Rollup 钩子的兼容、enforce pre/post、Vite 独有钩子有哪些？
**答**：
- 兼容性：Vite 插件是 Rollup 插件超集——resolveId/load/transform 等通用钩子直接可用；但部分 Rollup 钩子（outputOptions 等）在 dev 不生效（dev 不是 Rollup 在跑）。
- 位置控制：enforce: 'pre'（在 Vite 内核插件之前，常用于替换行为、注入拦截）、'post'（在内部插件之后，如最终改 HTML）。
- Vite 独有钩子：config（读改最终配置）、configResolved（只读配置）、configureServer（dev 中间件注入）、transformIndexHtml（改 index.html）、handleHotUpdate（自定义 HMR 模块失效逻辑）。
- apply: 'build' | 'serve' 控制插件只在某侧启用。

```javascript
// my-vite-plugin.js：混合钩子完整示例
const fs = require('fs');
const path = require('path');

export default function myPlugin({ inject = true } = {}) {
  return {
    name: 'my-vite-plugin',
    enforce: 'pre',
    apply: 'serve', // 只在 dev 生效
    // Vite 独有：读改配置
    config(config, env) {
      config.define = { ...config.define, __PLUGIN__: '"on"' };
    },
    configResolved(resolved) {
      console.log('root =', resolved.root);
    },
    // Vite 独有：注入 dev 中间件
    configureServer(server) {
      server.middlewares.use('/__status', (_req, res) => {
        res.end(JSON.stringify({ ok: true, modules: Object.keys(server.moduleGraph.urlToModuleMap).length }));
      });
    },
    // Rollup 兼容：转换
    transform(code, id) {
      if (!id.endsWith('.svg')) return null;
      return { code: `export default ${JSON.stringify(fs.readFileSync(id, 'utf-8'))}`, map: null };
    },
    // Vite 独有：改 index.html
    transformIndexHtml(html) {
      return inject ? html.replace('</head>', '<script src="/monitor.js"></script></head>') : html;
    },
    // Vite 独有：自定义 HMR 失效范围
    handleHotUpdate({ file, server, modules }) {
      if (file.endsWith('.env')) {
        server.config.logger.info('env 变化 全页刷新');
        server.ws.send({ type: 'full-reload' });
        return []; // 清空默认更新列表
      }
      return modules;
    },
  };
}
```
