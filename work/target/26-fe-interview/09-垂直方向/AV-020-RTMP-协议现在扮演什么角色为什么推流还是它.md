---
title: [AV-020] RTMP 协议现在扮演什么角色？为什么推流还是它？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-020：RTMP 协议现在扮演什么角色？为什么推流还是它？
**答**：
- RTMP（基于 TCP）浏览器已无法原生播放（Flash 死亡），但仍是推流事实标准：OBS/手机推流 SDK → 源站 → 转协议分发 HLS/FLV。
- 优势：生态成熟（各云厂商 ingest 端点都是 rtmp://）、推流端抗抖动、鉴权/录制链路完备；延迟 1~3s。
- 替代趋势：SRT（抗弱网、加密）、RTSP（安防）、WHIP（WebRTC 推流，亚秒延迟）都在吃 RTMP 的份额，但存量巨大短期不倒。
- URL 结构：`rtmp://host/app/streamName?sign=xxx`，streamName 即流 ID，主播端以此鉴权。
- 面试口径：RTMP 在前端的存在感主要是"推流地址的生成与鉴权"、"OBS 参数调优"、"服务端转封装理解"。

```bash
# 用 OBS / ffmpeg 推流到云厂商 RTMP 接入点
ffmpeg -re -i input.mp4 \
  -c:v libx264 -preset veryfast -tune zerolatency -g 50 \  # GOP=2s(25fps)
  -c:a aac -b:a 128k \
  -f flv "rtmp://push.example.com/live/room123?txSecret=abc&txTime=5f123456"

# 服务端将 RTMP 流转成 HLS / HTTP-FLV 分发（nginx-rtmp 配置示意）
```

```nginx
rtmp {
  server {
    listen 1935;
    application live {
      live on;
      hls on;
      hls_path /data/hls;       # 转出 HLS
      hls_fragment 2s;
      record off;
      exec_push ffmpeg -i rtmp://localhost/live/$name -c copy -f flv rtmp://localhost/hls/$name;
    }
  }
}
```
