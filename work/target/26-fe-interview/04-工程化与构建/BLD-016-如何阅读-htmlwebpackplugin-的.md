---
title: [BLD-016] 如何阅读 html-webpack-plugin 的源码？核心流程是什么？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-016：如何阅读 html-webpack-plugin 的源码？核心流程是什么？
**答**：
- 阅读路径：入口 index.js（apply → 钩子注册）→ childCompilationTemplatePlugin（用 child compilation 把模板编译成 HTML）→ emit 阶段的 alterAssetTagGroups / beforeEmit 拿到编译结果和资源注入点 → includeScripts 按 inject 位置插入 entry chunks。
- 核心技巧：它利用 compiler.hooks.make 里 tapAsync 创建 child compilation（compilation.addInclude），模板本身也被 loader（如 html-loader/ejs）链处理，体现"一切皆模块"。
- 钩子链：html-webpack-plugin-beforeHtmlGeneration → afterTemplateExecution → beforeEmit → afterEmit，第三方插件（如 favicon、pwa）都挂这四个钩子。
- 学到三条：child compilation 机制、基于阶段的钩子设计、选项校验用 schema-utils。

```javascript
// html-webpack-plugin 核心流程伪代码精简（阅读时对照真实源码）
class HtmlWebpackPlugin {
  constructor(options) { this.options = { inject: true, ...options }; }

  apply(compiler) {
    const N = 'HtmlWebpackPlugin';
    compiler.hooks.make.tapAsync(N, (compilation, cb) => {
      // 1 用 child compilation 独立编译模板（不污染主模块图）
      this.compileTemplate(compilation, this.options.template, (err, html) => {
        compilation.hooks.processAssets.tap({ name: N, stage: PROCESS_ASSETS_STAGE_OPTIMIZE },
          () => {
            // 2 收集本次 entry 产出的 js/css
            const scripts = Object.keys(compilation.assets).filter((f) => f.endsWith('.js'));
            // 3 按 inject 位置拼装 head/body 标签
            const tags = scripts.map((s) => `<script defer src="${s}"></script>`);
            // 4 发出最终 html
            compilation.emitAsset(this.options.filename, new RawSource(html.replace('</body>', `${tags.join('')}</body>`)));
          });
        cb();
      });
    });
  }
}

// webpack.config.js
// const HtmlWebpackPlugin = require('html-webpack-plugin');
// module.exports = { plugins: [new HtmlWebpackPlugin({
//   template: 'public/index.html', filename: 'index.html', inject: true,
//   minify: { collapseWhitespace: true, removeComments: true },
// })] };
```

## 第三章 Loader 开发与常用 loader 原理（BLD-017 ~ BLD-024）
