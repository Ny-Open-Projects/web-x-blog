---
title: [PER-016] HTTP/2 时代还需要域名分片和 CSS Sprite 吗？如何开启 HTTP/2？
date: 2026-11-17
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-016：HTTP/2 时代还需要域名分片和 CSS Sprite 吗？如何开启 HTTP/2？

**答**：
- HTTP/1.1 时代同域名连接数有限，需要域名分片、雪碧图、内联小图等"合请求"技巧。
- HTTP/2 **多路复用**让同域名下请求并行不排队，头部压缩（HPACK）进一步降低开销；域名分片反而增加 TLS 握手与连接数，应放弃。
- Sprite 图失去了合并请求的意义，且不利于单图缓存与按需加载，一般不再需要。
- 雪碧图与分片被替代，但"减少关键资源数量"的思想仍然有效。

```nginx
server {
    listen 443 ssl http2;
    server_name example.com;

    # HTTP/2 多路复用后同域名请求不再排队，
    # 旧时代的域名分片反而增加 TLS 握手次数，应当放弃
    location / {
        root /var/www/html;
    }
}
```

## 三、渲染性能
