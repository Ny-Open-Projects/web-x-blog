---
title: [WEB-186] 混合 App 的"离线包"是怎么实现请求拦截的？
date: 2026-11-17
categories: [Web协议与浏览器]
tags: [前端面试, 面试题, 01]
type: 面试题
---

## WEB-186：混合 App 的"离线包"是怎么实现请求拦截的？
**答**：
- 原理：把 H5 静态资源打成 zip 提前下发并校验 md5，运行时把对 CDN 的请求劫持到本地文件——"网络请求"变成"读磁盘"。
- 端上机制：Android 用 WebViewClient.shouldInterceptRequest 按映射表返回本地 WebResourceResponse；iOS 用 WKURLSchemeHandler 或本地 HTTP 服务。
- 更新闭环：版本清单接口 → 差量下载 → 解压校验 → 原子切换映射表；未命中兜底回源 CDN。
- 关键设计：URL 指纹（hash）是映射表的键，命中失败必须无感回退网络，MIME 与编码头要与线上一致。

```javascript
// 离线包映射与拦截（示意：端上由 shouldInterceptRequest 或 WKURLSchemeHandler 执行同一张表）
const pkg = {
  version: '2026.11.05-3',
  base: 'https://cdn.example.com/h5/app/',
  map: { 'js/app.a3f9.js': 'pkg/js/app.a3f9.js', 'css/app.8c2d.css': 'pkg/css/app.8c2d.css' },
};
function intercept(requestUrl) {
  const path = requestUrl.replace(pkg.base, '');
  if (!pkg.map[path]) return null;                     // 未命中，走网络
  const local = readLocalFile(pkg.map[path]);          // 命中，读离线包文件
  return local ? { body: local, mime: guessMime(path) } : null; // 读不到也回退网络
}
```
