---
title: [ENG-017] 如何写一个自定义 webpack loader？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-017：如何写一个自定义 webpack loader？
**答**：
- loader 就是一个函数：接收源码，返回转换结果，this 上有丰富的上下文（query、async 等）。
- 同步 loader 直接 return；需要异步时调用 this.async() 拿到 callback。
- this.getOptions() 读取配置项；可以用 loader-utils 校验参数。
- 在 webpack 配置里用 resolveLoader 或路径引用注册。

```javascript
// loaders/replace-loader.js
module.exports = function (source) {
  // 同步 loader：替换源码中的占位符
  return source.replace(
    /__BUILD_TIME__/g,
    JSON.stringify(new Date().toISOString())
  );
};

// 异步 loader 的写法
module.exports.asyncLoader = function (source) {
  const callback = this.async();
  someAsyncWork(source)
    .then((result) => callback(null, result))
    .catch((err) => callback(err));
};
```
