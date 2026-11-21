---
title: [BLD-013] loader 和 plugin 之间如何通信？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-013：loader 和 plugin 之间如何通信？
**答**：
- 方式一：webpack 官方机制 NormalModule 的 loaderContext 上挂自定义属性，plugin 在 normalModuleLoader 钩子里往 loaderContext 注入，loader 里用 this.xxx 读取（tapable 上下文思想）。
- 方式二：模块级 WeakMap 以模块资源路径为 key 存状态，plugin 写、loader 读，注意避免闭包引用阻碍 GC。
- 方式三：plugin 在 compiler 上挂共享命名空间对象（compiler.__myPluginData），loader 通过 this._compiler 拿到（webpack 5）。
- 注意方向是"plugin 通知 loader"，loader 无法直接 tap 钩子；跨 compilation 不要复用可变状态。

```javascript
// webpack.config.js：plugin 向 loader 注入上下文
const inject = (compilation) => (loaderContext, module) => {
  loaderContext.__buildId = compilation.hash;              // 注入自定义字段
  loaderContext.__i18nDict = { 首页: 'Home', 关于: 'About' };
};

class LoaderBridgePlugin {
  apply(compiler) {
    compiler.hooks.compilation.tap('LoaderBridgePlugin', (compilation) => {
      compilation.hooks.normalModuleLoader.tap('LoaderBridgePlugin', inject(compilation));
    });
  }
}

// my-loader.js：loader 侧读取
module.exports = function (source) {
  if (this.__i18nDict) {
    for (const [zh, en] of Object.entries(this.__i18nDict)) {
      source = source.split(zh).join(en);
    }
  }
  return source;
};

// webpack.config.js
// module.exports = { plugins: [new LoaderBridgePlugin()],
//   module: { rules: [{ test: /\.js$/, use: ['./my-loader'] }] } };
```
