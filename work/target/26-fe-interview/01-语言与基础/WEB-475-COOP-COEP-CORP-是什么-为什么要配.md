---
title: [WEB-475] COOP/COEP/CORP 是什么，为什么要配
date: 2026-11-19
categories: [WEB与网络]
tags: [前端面试, 面试题, 安全]
type: 面试题
---

## WEB-475：COOP/COEP/CORP 是什么，为什么要配

**答**：
- 三兄弟一句话：COOP 隔离「窗口关系」（opener），COEP 强制「所有子资源声明可跨域加载」，CORP 声明「我的资源允许谁加载」
- COOP：`Cross-Origin-Opener-Policy: same-origin`，新窗口与原窗口断开 opener，防 Spectre 类侧信道与 tabnabbing
- COEP：`require-corp` / `credentialless`，页面要求所有 iframe/script/图片带上 CORP 或 CORS 授权，否则不加载
- 最大实战影响：开启 COEP+COOP 后才能用 SharedArrayBuffer（高精度计时、WASM 多线程、Safari 里的大文件优化）
- 排障提示：开 COEP 后常见「图片/接口突然全 404」——它们没带 CORP/CORS 头，需要逐个资源补 `Cross-Origin-Resource-Policy` 或改 CORS

```http
Cross-Origin-Opener-Policy: same-origin
Cross-Origin-Embedder-Policy: require-corp
Cross-Origin-Resource-Policy: cross-origin   # 资源方加
```
