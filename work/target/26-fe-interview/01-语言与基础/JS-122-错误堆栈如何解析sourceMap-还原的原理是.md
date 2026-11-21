---
title: [JS-122] 错误堆栈如何解析？sourceMap 还原的原理是什么？
date: 2026-11-17
categories: [JavaScript]
tags: [前端面试, 面试题, 04]
type: 面试题
---

## JS-122：错误堆栈如何解析？sourceMap 还原的原理是什么？

**答**：
- 生产环境堆栈来自压缩产物：`app.min.js:1:2345` 这样的行列无法直接定位源码。
- sourceMap 的 mappings 字段用 Base64 VLQ 编码了"产物行列 → 源码行列"的映射表。
- 方案：构建时不发布 .map（防源码泄露），只上传到监控平台，上报后在平台侧查表还原。
- 运行时解析用 `error.stack` 的格式正则提取帧信息，再交给 SourceMapConsumer 查询。

```javascript
// 解析 V8 堆栈格式：at 函数名 (文件:行:列)
function parseStack(stack) {
  return stack.split('\n').slice(1)
    .map((line) => {
      const m = line.match(/at\s+(.+?)\s+\(?([^()\s]+?):(\d+):(\d+)\)?/);
      return m && { fn: m[1], file: m[2], line: +m[3], col: +m[4] };
    })
    .filter(Boolean);
}

const stack = `TypeError: Cannot read properties of undefined
    at fetchUser (https://cdn/app.min.js:1:2345)
    at render (https://cdn/app.min.js:2:100)`;
console.log(parseStack(stack));
// [{ fn:'fetchUser', file:'.../app.min.js', line:1, col:2345 }, ...]

// 还原流程（在监控平台执行，不在浏览器）：
// import { SourceMapConsumer } from 'source-map';
// const consumer = await new SourceMapConsumer(sourcemapJSON);
// const pos = consumer.originalPositionFor({ line: 1, column: 2345 });
// → { source: 'src/user.js', line: 120, column: 8, name: 'fetchUser' }
// 再拉取 src/user.js 第 120 行附近代码即可展示给开发者

// 工程配套：
// 1. 构建：webpack devtool: 'hidden-source-map'（产出但不带注释引用）
// 2. 上传：CI 阶段把 .map 与版本号一起传到私有存储
// 3. 关联：上报时附带版本号，还原时按版本匹配 .map
```
