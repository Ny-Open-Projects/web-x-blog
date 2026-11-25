---
title: [BLD-024] asset modules 是什么？四种类型怎么选？旧 url-loader/file-loader 怎么迁移？
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-024：asset modules 是什么？四种类型怎么选？旧 url-loader/file-loader 怎么迁移？
**答**：
- webpack 5 内建资源处理，不再需要 file-loader/url-loader/raw-loader；通过 module.rules 的 type 指定四种类型。
- asset/resource：文件输出为独立文件，返回 URL（对应 file-loader）。
- asset/inline：转 base64 Data URI 内联（对应 url-loader 无 limit）；asset/source：导出源码字符串（对应 raw-loader）。
- asset：自动模式，按 parser.dataUrlCondition.maxSize 在 resource 与 inline 间自动选择（对应 url-loader 的 limit），默认 4KB。
- 迁移注意：generator.filename 替代 file-loader 的 name（支持 [contenthash][ext]）；inline 大资源会让 js 体积膨胀且无法并行缓存。

```javascript
// webpack.config.js：asset modules 完整配置与迁移对照
module.exports = {
  module: {
    rules: [
      {
        test: /\.(png|jpe?g|gif|webp|avif)$/i,
        type: 'asset', // 自动模式
        parser: {
          dataUrlCondition: { maxSize: 8 * 1024 }, // 小于 8KB 内联 base64
        },
        generator: {
          filename: 'static/img/[name].[contenthash:8][ext]', // 替代 file-loader name
        },
      },
      {
        test: /\.(woff2?|eot|ttf|otf)$/i,
        type: 'asset/resource', // 字体必须独立文件 否则跨域与缓存不利
        generator: { filename: 'static/font/[name].[contenthash:8][ext]' },
      },
      {
        test: /\.svg$/i,
        type: 'asset/source', // 导出源码字符串 便于内联 svg 做染色
      },
      // 旧写法迁移对照：
      // url-loader + limit 8192            -> type: 'asset' + dataUrlCondition
      // file-loader + name '[name].[hash]' -> type: 'asset/resource' + generator.filename
      // raw-loader                          -> type: 'asset/source'
    ],
  },
};
```

## 第四章 Tree-shaking 与作用域（BLD-025 ~ BLD-030）
