---
title: [BAS-172] Referer 和 Referrer-Policy 是什么关系？
date: 2026-11-17
categories: [前端基础速答]
tags: [前端面试, 面试题, 10]
type: 面试题
---

## BAS-172：Referer 和 Referrer-Policy 是什么关系？
**答**：
- 请求头拼写就是 Referer（少个 r，历史遗留），而标准属性叫 Referrer-Policy——这本身就是考点。
- 现代默认 strict-origin-when-cross-origin：同源带完整 URL，跨域只带 origin，HTTPS→HTTP 不带。
- 作用是控制 URL 泄漏面：隐私路径、内网地址、token 参数不该发给第三方；`<meta name="referrer">` 或响应头可设置。

```http
Referer: https://old.example.com/page?q=secret   # 拼写就是少个 r

# 策略响应头或 meta 控制
Referrer-Policy: strict-origin-when-cross-origin  # 现代浏览器默认
# no-referrer：一律不发
# same-origin：仅同源请求带完整 URL
# 防 URL 里的 token 与内网路径泄漏给第三方站点
```

## 十九、浏览器与渲染补充
