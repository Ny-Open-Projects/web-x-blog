---
title: [RBL-038] 笔试：手写 manifest 生成插件（产物清单 + 体积统计）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-038：笔试：手写 manifest 生成插件（产物清单 + 体积统计）
**题目**：实现 Rspack 插件 BuildManifestPlugin：1) 在产物中生成 manifest.json，内容为 { "entryJs": [带 hash 的 js 文件名列表], "totalSize": js+css 总字节数 }；2) 只统计 .js/.css；3) 通过 compilation.getStats 拿入口信息或用 compilation.options.entry；4) 用 emitAsset 写入；5) 处理 entry 值为字符串/数组/对象三种形态。

```javascript
class BuildManifestPlugin {
  apply(compiler) {
    compiler.hooks.emit.tap('BuildManifestPlugin', (compilation) => {
      // 1) 归一化 entry 三种形态
      const entry = compilation.options.entry;
      const entryNames = typeof entry === 'string' || Array.isArray(entry)
        ? ['main'] : Object.keys(entry);

      const js = [], css = [];
      let totalSize = 0;
      for (const [name, asset] of Object.entries(compilation.assets)) {
        const isEntry = entryNames.some(n =>
          name === `${n}.js` || name.startsWith(`${n}.`));
        if (isEntry && name.endsWith('.js')) js.push(name);
        if (name.endsWith('.css')) css.push(name);
        if (/\.(js|css)$/.test(name)) totalSize += asset.size();
      }
      compilation.emitAsset('manifest.json', {
        source: () => JSON.stringify({ entryJs: js, css, totalSize }, null, 2),
        size: () => 0,
      });
    });
  }
}
module.exports = BuildManifestPlugin;
```
**评分点**：
- entry 三形态归一化（对象/字符串/数组）——边界完整。
- 钩子选 emit，此阶段 assets 已定型且还能 emitAsset。
- emitAsset 而非直接写文件（纳入构建产物体系）。
- 体积统计限定 .js/.css 并累加 size。
- 能说明 contenthash 文件名下 manifest 的用途（SSR/服务端渲染引用注入）。
