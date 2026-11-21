---
title: [BLD-020] loader 的异步处理与缓存机制怎么用？this.async 和 this.cacheable 详解。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-020：loader 的异步处理与缓存机制怎么用？this.async 和 this.cacheable 详解。
**答**：
- 同步 loader：return 结果或 this.callback(null, content, sourceMap, meta)；有第二输出（如 sourceMap）时必须用 this.callback。
- 异步 loader：const callback = this.async()，处理完调 callback(null, result)，webpack 会等待；不调 async 时 loader 是同步的，阻塞但开销小。
- 缓存：默认 loader 结果可缓存（等价 this.cacheable()）；调用 this.cacheable(false) 表示"输出可能依赖外部状态（时间、随机、远端）"，每次重编译都重跑。
- this.addDependency(file) 声明额外输入依赖（loader 内读了别的文件时必须加，否则该文件变化不会触发重编译）。

```javascript
// async-loader.js：异步读远端 schema + 声明本地依赖
const fs = require('fs');

module.exports = function (source) {
  const callback = this.async(); // 声明为异步 loader
  const options = this.getOptions();

  // 声明额外依赖 依赖文件变化也会触发本模块重编译
  this.addDependency(options.schemaPath);
  this.cacheable(true); // 输出只依赖 source 与 schemaPath 可缓存

  fs.readFile(options.schemaPath, 'utf-8', (err, schema) => {
    if (err) return callback(err); // 异步错误走 callback 第一参数
    try {
      const result = source.replace('__SCHEMA__', JSON.stringify(JSON.parse(schema)));
      callback(null, result); // callback(null, content, sourceMap?, meta?)
    } catch (e) {
      callback(e);
    }
  });
};

// webpack.config.js
// module.exports = { module: { rules: [
//   { test: /form\.js$/, use: [{ loader: './async-loader',
//     options: { schemaPath: './src/form-schema.json' } }] },
// ] } };
```
