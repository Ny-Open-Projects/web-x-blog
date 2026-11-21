---
title: [BLD-170] 产物完整性：SRI 的生成、fallback 与 CI 集成。
date: 2026-11-17
categories: [构建工具]
tags: [前端面试, 面试题, 18]
type: 面试题
---

## BLD-170：产物完整性：SRI 的生成、fallback 与 CI 集成。
**答**：
- **SRI（Subresource Integrity）**：`<script src crossorigin="anonymous" integrity="sha384-<base64(sha256)>">`，浏览器校验资源哈希，防 CDN 篡改与劫持注入——第三方 CDN/公共库场景的标配安全项。
- 生成时机：构建后由插件计算每个 hash 产物的完整性值并写入 HTML（`webpack-subresource-integrity` 插件 / vite 用 `vite-plugin-sri`），**必须在 contenthash 定稿之后**（processAssets 末段）。
- 限制：`crossorigin="anonymous"` 要求 CDN 正确返回 CORS 头（`Access-Control-Allow-Origin`），否则资源被浏览器拒绝加载——上线前必须验证；**动态 import 的 chunk 也能覆盖**（webpack 插件给 loadScript 加 integrity 属性）。
- CI 集成：发布后爬取 HTML 校验 integrity 与实际产物哈希一致（防发布流程错位），作为上线卡口之一。

```javascript
// webpack：SRI 全链路配置
const HtmlWebpackPlugin = require('html-webpack-plugin');
const { SubresourceIntegrityPlugin } = require('webpack-subresource-integrity');

module.exports = {
  output: {
    crossOriginLoading: 'anonymous',     // SRI 前置条件：脚本必须带 crossorigin
    hashFunction: 'sha256',              // webpack5 支持 sha256/sha384/sha512
  },
  plugins: [
    new SubresourceIntegrityPlugin({
      hashFuncNames: ['sha384'],
      enabled: process.env.NODE_ENV === 'production',
      // 动态 chunk 同样注入 integrity（loadScript 时读取）
    }),
    new HtmlWebpackPlugin({ template: './index.html' }),
    // 产物 HTML 示例：
    // <script src="//cdn.example.com/main.3f2a91.js"
    //         crossorigin="anonymous"
    //         integrity="sha384-x8R2v8kQbJ0mJz5S7gV1uP9rWqLmN4TzYb2cA1eD5fGhIjKlMnOpQrStUvWxYz01="></script>
  ],
};
```

```bash
# CI 上线卡口：校验 HTML 里的 SRI 与产物实际哈希一致（scripts/check-sri.sh）
#!/usr/bin/env bash
set -euo pipefail
CDN_BASE="https://cdn.example.com"
fail=0
for tag in $(grep -oP 'src="[^"]+" integrity="sha384-[^"]+"' dist/index.html | sed 's/src="//;s/" integrity="/ /;s/"$//'); do
  url=$(echo "$tag" | cut -d' ' -f1); expect=$(echo "$tag" | cut -d' ' -f2)
  actual="sha384-$(curl -fsSL "$CDN_BASE/$url" | openssl dgst -sha384 -binary | openssl base64 -A)"
  if [ "$actual" != "$expect" ]; then
    echo "[FAIL] SRI 不匹配: $url"; fail=1
  fi
done
# 同时校验 CORS 头（SRI 生效前提）：
curl -sI "$CDN_BASE/js/main.js" | grep -qi 'access-control-allow-origin' || { echo "[FAIL] CDN 缺 CORS 头"; fail=1; }
exit $fail
```

## 十九章 工程化与协作（BLD-171 ~ BLD-178）
