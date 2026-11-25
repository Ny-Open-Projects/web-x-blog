---
title: [MP-072] 构建 npm 有哪些常见坑？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-072：构建 npm 有哪些常见坑？
**答**：
- 坑一：npm 包没提供构建产物（es 源码），小程序构建失败——选支持小程序的包（如 vant-weapp 本身带 dist）。
- 坑二：`packNpmManually` 配置了但 `miniprogramNpmDistDir` 指错，导致找不到 `@vant/weapp`。
- 坑三：CI 构建忘记 `packNpm` 步骤，预览包缺 miniprogram_npm；package.json 变更后必须重新构建。
- 坑四：包内引用 process.env/node 内置模块，小程序运行时不支持，需 polyfill 或换包。

```bash
# CI 中构建 npm：先 npm install 再 packNpm
npm install
npx miniprogram-ci pack-npm \
  --project-path ./miniprogram \
  --appid wx1234567890 \
  --robot 1
# 产物：miniprogram/miniprogram_npm/@vant/weapp/...
```
