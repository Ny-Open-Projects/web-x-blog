---
title: [OPS-116] 视频与 HLS 分发在 nginx/CDN 层怎么配？m3u8 和 ts 的缓存策略为何不同？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-116：视频与 HLS 分发在 nginx/CDN 层怎么配？m3u8 和 ts 的缓存策略为何不同？
**答**：
- HLS 原理：视频切成 ts/fMP4 分片 + 一个 m3u8 播放列表索引；分片内容不可变可永久缓存，m3u8 会随直播推进/清晰度变化频繁更新，只给秒级缓存。
- 直播场景 m3u8 短 TTL + 每次回源校验；点播场景 m3u8 也基本静态，可适当放宽。
- ts 分片用 immutable 长缓存，命中后边缘直接吐，回源量随播放时长线性可控。
- 大文件注意：单连接限速防单用户吃满磁盘 IO；mp4 需要 http_mp4_module 才支持拖拽（range 请求）。
- 防盗链：Referer 白名单 + 有效期签名 URL（对 ts 也生效，防工具直接拉流）。

```nginx
# HLS 分发：m3u8 短缓存、ts 永久缓存
server {
    location ~ \.m3u8$ {
        root /data/vod;
        types { application/vnd.apple.mpegurl m3u8; }
        add_header Cache-Control "public, max-age=5";   # 播放列表秒级，新分片尽快可见
        add_header Access-Control-Allow-Origin "https://www.example.com";
    }

    location ~ \.ts$ {
        root /data/vod;
        types { video/mp2t ts; }
        add_header Cache-Control "public, max-age=31536000, immutable";  # 分片不可变
        limit_rate 8m;                                   # 单连接限速，防 IO 独占
    }

    location ~ \.mp4$ {
        root /data/vod;
        mp4;                                             # http_mp4_module，支持拖拽 range
        add_header Cache-Control "public, max-age=86400";
    }
}
```
