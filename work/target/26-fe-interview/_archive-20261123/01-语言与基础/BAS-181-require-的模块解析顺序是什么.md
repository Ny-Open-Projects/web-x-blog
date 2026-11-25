---
title: [BAS-181] require 的模块解析顺序是什么？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-181：require 的模块解析顺序是什么？
**答**：
- 顺序：require 缓存（require.cache）→ Node 核心模块（fs/path 等）→ 相对或绝对路径 → 裸模块名去 node_modules 逐级向上找。
- 路径解析细节：先按文件名，依次补 .js/.json/.node 后缀；是目录则读 package.json 的 main，没有再找 index.js。
- 模块首次加载后会缓存，二次 require 拿的是同一实例。

```javascript
// require('util') 的查找顺序
// 1. 缓存命中：require.cache 里直接返回同一实例
// 2. 核心模块：fs、path、http 等
// 3. 相对路径：./file → 尝试 file.js / file.json / file.node
//    是目录则读 package.json 的 main，再不行找 index.js
// 4. 裸模块名：从当前目录 node_modules 逐级向上查找
const path = require('path');   // 核心模块，最快
```
