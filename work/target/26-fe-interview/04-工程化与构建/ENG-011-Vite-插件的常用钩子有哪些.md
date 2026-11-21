---
title: [ENG-011] Vite 插件的常用钩子有哪些？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-011：Vite 插件的常用钩子有哪些？
**答**：
- Vite 插件是 Rollup 插件的超集：transform、resolveId 等 Rollup 钩子直接可用。
- Vite 特有钩子：configResolved 读取最终配置、configureServer 自定义 dev server 中间件、transformIndexHtml 注入 HTML。
- enforce: 'pre'/'post' 控制插件相对内置插件的执行顺序。
- 按 apply: 'serve'/'build' 限定插件只在 dev 或构建阶段生效。

```javascript
// my-vite-plugin.js
export default function myPlugin() {
  return {
    name: 'my-plugin',
    // Vite 特有：拿到最终配置
    configResolved(config) {
      console.log('command:', config.command);
    },
    // Rollup 兼容：转译模块源码
    transform(code, id) {
      if (id.endsWith('.svg')) {
        return `export default ${JSON.stringify(id)}`;
      }
      return null;
    },
    // Vite 特有：改写入口 HTML
    transformIndexHtml(html) {
      return html.replace('</head>', '<script src="/inject.js"></script></head>');
    },
  };
}
```
