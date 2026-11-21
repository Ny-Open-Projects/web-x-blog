---
title: [BLD-194] 构建侧如何支持 A/B 多版本同时在线？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-194：构建侧如何支持 A/B 多版本同时在线？
**答**：
- 需求形态：两个实验版本（旧版 checkout / 新版 checkout v2）**同时可访问**且可随时切流——构建侧要保证两版本产物共存、资源不互相覆盖、切换零发布。
- 核心手段：**版本化发布目录**（`/static/v1/... /static/v2/...` 而非互相覆盖的 hash 目录）+ 入口路由层（BFF/网关）按用户分桶返回对应 `index.html`；静态资源因 contenthash 天然共存。
- 构建侧配置：多入口或多编译器（BLD-112 的多编译器模式复用）各产一份 manifest；实验开关编译期注入（feature flag 版本归属）。
- 陷阱：localStorage/接口 schema 跨版本兼容（构建侧无法解决，需协议设计）；实验版本也要全套产物质量校验（不能"实验就不测"）。

```javascript
// webpack.multi-experiment.config.js：多编译器产出两套可共存产物
const experiments = [{ id: 'v1', flag: false }, { id: 'v2', flag: true }];
module.exports = experiments.map(({ id }) => ({
  name: id,
  entry: { main: `./src/experiments/${id}/main.tsx` },
  output: {
    path: path.resolve(__dirname, `dist/static/${id}`),     // 版本目录：共存不覆盖
    filename: '[name].[contenthash].js',
    publicPath: `/static/${id}/`,                            // 各版本独立前缀
  },
  plugins: [
    new webpack.DefinePlugin({ __EXP_VARIANT__: JSON.stringify(id) }), // 实验归属编译期定
    new HtmlWebpackPlugin({ filename: `../html/${id}/index.html` }),   // html 也分版本目录
    new (require('webpack-manifest-plugin').WebpackManifestPlugin)({
      fileName: `manifest.${id}.json`,
    }),
  ],
}));
// 服务端（BFF）：
// const variant = abService.assign(userId, 'checkout');        // 分桶
// const html = await renderTemplate(`html/${variant}/index.html`, { variant });
// res.send(html);                                              // 同库多版本，切流=改分桶，零发布
```
