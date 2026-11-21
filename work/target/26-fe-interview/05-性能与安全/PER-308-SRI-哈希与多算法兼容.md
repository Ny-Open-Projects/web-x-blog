---
title: [PER-308] SRI 的 integrity 值怎么算？多算法哈希（sha384+sha512）为什么要写多个？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-308：SRI 的 integrity 值怎么算？多算法哈希（sha384+sha512）为什么要写多个？

**答**：
- 计算方式：对**响应的原始字节**（不是文件内容的转义/规范化版本）做哈希，`integrity="sha384-<base64>"`。坑点：CDN/构建管线对文件做了任何字节级改动（gzip 后解压不一致、BOM 头、换行符转换、尾部空行）都会导致校验失败——所以 integrity 必须与"最终线上字节"严格一致。
- 多算法的意义：浏览器采用列表中**最强的共同支持算法**；写 `sha384-xxx sha512-yyy` 两个值是面向未来的迁移姿势——老浏览器用 sha384 校验，新浏览器用 sha512；只要有一个匹配即通过。单算法被"未来破解"时多算法提供迁移缓冲。
- 生成工具：`openssl dgst -sha384 -binary FILE | openssl base64 -A`；构建插件在产物上传 CDN 后回读真实字节计算，避免"本地算的哈希 ≠ 线上字节"。
- 覆盖范围：script/stylesheet/link(rel=preload as=script/style 等)；ESM 动态 import 在现代浏览器也支持 integrity（配合 importmap 的静态声明）。worker 的 importScripts 不支持 integrity，需 CSP 兜底。

```bash
# 生成 integrity 值（对最终上传 CDN 的那个文件）
openssl dgst -sha384 -binary app.8f3c.js | openssl base64 -A
# => "CTkZ8Wqk9p..." 前缀写 sha384-
```
```html
<script src="https://cdn.example.com/app.8f3c.js"
        integrity="sha384-CTkZ8Wqk9p+abc... sha512-Lx0pQk9Zdef..."
        crossorigin="anonymous"></script>
<!-- crossorigin=anonymous 必须配：带 integrity 的跨域请求需要 CORS 模式才能读到字节做校验，漏写直接不加载 -->
```

**评分点**：
- 对"响应原始字节"计算哈希，并能指出构建/CDN 管线字节不一致是失败主因。
- 多算法列表语义（取最强共同支持，任一匹配通过）与迁移用途。
- crossorigin="anonymous" 与 integrity 必须同配。
- openssl 生成命令或构建期自动化方案。
