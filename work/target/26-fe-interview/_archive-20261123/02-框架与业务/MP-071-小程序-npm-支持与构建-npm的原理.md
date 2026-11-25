---
title: [MP-071] 小程序 npm 支持与"构建 npm"的原理？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-071：小程序 npm 支持与"构建 npm"的原理？
**答**：
- 小程序**不能直接 require node_modules**：构建 npm 把 npm 包的构建产物复制/整理到 `miniprogram_npm/` 目录，代码里 require 时按 `miniprogram_npm` 优先查找。
- 机制：识别 package.json 的 `miniprogram` 字段（或 packNpmManually 指定）作为包入口，只复制构建产物不复制源码。
- 项目结构：根目录 package.json（devDependencies + 构建）与 miniprogramRoot 分离，开发者工具「工具-构建 npm」或 `miniprogram-ci.packNpm`。

```json
{
  "miniprogramRoot": "miniprogram/",
  "setting": {
    "packNpmManually": true,
    "packNpmRelationList": [
      {
        "packageJsonPath": "./package.json",
        "miniprogramNpmDistDir": "./miniprogram/"
      }
    ]
  }
}
```
