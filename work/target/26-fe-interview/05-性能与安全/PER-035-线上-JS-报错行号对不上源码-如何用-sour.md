---
title: [PER-035] 线上 JS 报错行号对不上源码，如何用 sourcemap 还原？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-035：线上 JS 报错行号对不上源码，如何用 sourcemap 还原？

**答**：
- 生产构建生成 `.map` 文件但**不上传到 CDN**，只上传到监控平台或内部日志系统，避免源码泄露。
- 监控 SDK 上报压缩后的堆栈；还原端从堆栈文本解析出文件名、行、列。
- 用 `source-map` 库的 `originalPositionFor` 把压缩位置映射回源码的文件、行、列、函数名。
- 还原后再按"源码文件 + 行号 + message"聚合错误指纹，便于归组和去重。

```javascript
// restore-stack.js —— 用 sourcemap 还原线上压缩代码的报错位置
// npm i source-map
const { SourceMapConsumer } = require('source-map');
const rawSourceMap = require('./app.min.js.map'); // 构建产出的 map 文件

async function main() {
  const consumer = await new SourceMapConsumer(rawSourceMap);
  // 从上报堆栈中解析出的压缩代码位置
  const position = consumer.originalPositionFor({
    line: 1,      // app.min.js 中报错的行号
    column: 2345  // 报错的列号
  });
  console.log(position);
  // => { source: 'src/utils/request.js', line: 42, column: 10, name: 'request' }
}
main();
```
