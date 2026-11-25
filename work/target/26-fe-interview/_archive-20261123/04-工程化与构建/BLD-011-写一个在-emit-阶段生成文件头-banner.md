---
title: [BLD-011] 写一个在 emit 阶段生成文件头 banner 和产物清单 manifest.json 的插件。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-011：写一个在 emit 阶段生成文件头 banner 和产物清单 manifest.json 的插件。
**答**：
- 用 compiler.hooks.emit（tapAsync），此时 compilation.assets 已就绪但尚未写盘，是"最后修改产物"的时机。
- 遍历 assets 生成 { 文件名: { size, hash } } 清单，用 compilation.emitAsset 新增 manifest.json，并给 js 文件头部插入 banner 注释。
- 改资源用 compilation.updateAsset，新增用 emitAsset（webpack 5 推荐，代替直接赋值 assets 对象）。
- 插件要接 options 参数，写清 name 并在每个 tap 传插件名便于调试。

```javascript
// banner-manifest-plugin.js：完整生产可用
class BannerManifestPlugin {
  constructor(options = {}) {
    this.banner = options.banner || '/* build by my-team */';
    this.manifestName = options.manifestName || 'manifest.json';
  }

  apply(compiler) {
    const pluginName = 'BannerManifestPlugin';
    compiler.hooks.emit.tapAsync(pluginName, (compilation, callback) => {
      const manifest = {};

      // 1 给所有 js 产物加 banner
      for (const [name, source] of Object.entries(compilation.assets)) {
        manifest[name] = { size: source.size() };
        if (name.endsWith('.js')) {
          const content = `${this.banner}\n${source.source()}`;
          compilation.updateAsset(name, compilation.compiler.webpack.sources.RawSource(content));
        }
      }

      // 2 追加产物清单
      compilation.emitAsset(
        this.manifestName,
        compilation.compiler.webpack.sources.RawSource(JSON.stringify(manifest, null, 2)),
      );
      callback();
    });
  }
}

module.exports = BannerManifestPlugin;

// webpack.config.js
// const BannerManifestPlugin = require('./banner-manifest-plugin');
// module.exports = { plugins: [new BannerManifestPlugin({ banner: '/* v1.2.0 app */' })] };
```
