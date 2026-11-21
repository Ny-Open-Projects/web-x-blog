---
title: [SCN-192] 多团队各自实现灰度标记（cookie、URL 参数、响应头都有），口径打架，如何统一？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-192：多团队各自实现灰度标记（cookie、URL 参数、响应头都有），口径打架，如何统一？
**答**：
- 灰度标记乱的本质是"身份与分流判定的实现分散"：统一为"网关侧判定 + 全链路透传"，各端只读不判。
- 标准化身份：统一的设备指纹 / uid 生成与下发（登录前匿名 id，登录后并轨），网关按身份 + 分流规则计算灰度命中，结果写入响应头 `X-Gray-Bucket`。
- 前端只做两件事：把响应头里的灰度标记写入统一 cookie（透传给后续请求与第三方监控），把标记附进所有上报（分析时能分桶）。
- 灰度判定永不放前端：前端 JS 做分流会导致刷新/多端不一致与被篡改，前端只消费结论。

```javascript
// 灰度标记统一：网关判定，前端只透传与上报
// nginx（网关侧）示例：按 uid 计算 bucket 并注入响应头
// upstream 里由分流服务判定，此处示意注入点
// location /api/ {
//   proxy_set_header X-Uid $cookie_uid;
//   add_header X-Gray-Bucket $upstream_http_x_gray_bucket always;  # 透传到浏览器
// }

// 前端统一入口：首请求响应头 -> 写标准 cookie -> 全链路透传
export function captureGrayBucket(response) {
  const bucket = response.headers.get('X-Gray-Bucket');
  if (!bucket) return;
  // 统一口径：单一 cookie，各团队禁止自造
  document.cookie = `gray_bucket=${bucket}; path=/; max-age=86400; samesite=lax`;
  report({ type: 'gray-bucket', bucket, ts: Date.now() });   // 监控/分析按此分桶
  window.__GRAY_BUCKET__ = bucket;
}

// 请求层透传：后续所有请求自动带上，后端不用重复判定
export function withGrayHeaders(headers = {}) {
  const bucket = document.cookie.match(/gray_bucket=([^;]+)/)?.[1];
  return bucket ? { ...headers, 'X-Gray-Bucket': bucket } : headers;
}

// 禁止各团队私搭灰度：SDK 层面收口，dev 环境直接报错
export function legacyGrayCheck(name) {               // 旧接口，发现即治理
  console.error(`[gray] 禁止前端自判灰度（${name}），请使用网关统一 bucket`);
  report({ type: 'gray-violation', name });
  return false;
}
```
