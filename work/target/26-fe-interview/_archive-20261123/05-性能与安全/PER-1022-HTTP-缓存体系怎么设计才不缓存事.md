---
title: [PER-1022] HTTP 缓存体系怎么设计才不"缓存事故"
date: 2026-11-22
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-1022：HTTP 缓存体系怎么设计才不"缓存事故"

**答**：
- 分层：强缓存（Cache-Control max-age/immutable，适合带 hash 的静态资源）→ 协商缓存（ETag/Last-Modified，适合 HTML 与 API）。
- 关键铁律：HTML 不强缓存（no-cache 协商），静态资源文件名带内容 hash + 一年 immutable——发布即失效。
- CDN 层：Cache-Control s-maxage 与浏览器 max-age 分离；purge 机制兜底；Vary 头控制缓存维度（Origin/压缩格式）。
- 事故预防：缓存键变更演练（新版本发布后抽样验证）、灰度期新旧资源并存、回滚预案（旧 hash 仍在线上可回切）。

```javascript
# Nginx 缓存策略模板
location ~* \.(js|css|png|avif)$ {
  # 带 hash 的文件：一年强缓存
  add_header Cache-Control "public, max-age=31536000, immutable";
}
location = /index.html {
  # HTML：协商缓存，每次校验
  add_header Cache-Control "no-cache";
  add_header ETag '"build-123456"';
}
location ~* ^/api/ {
  add_header Cache-Control "no-store";   # API 默认不缓存
}
// 前端验证：performance 资源 entry 的 transferSize === 0 即命中缓存
```
