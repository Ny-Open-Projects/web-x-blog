---
title: [AV-103] 一条 FFmpeg 转码命令长什么样？关键参数分别什么意思？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-103：一条 FFmpeg 转码命令长什么样？关键参数分别什么意思？（高频）
**答**：
- 转码管线：demux 解封装 → decode 解码 → filter 处理 → encode 编码 → mux 再封装，FFmpeg 一条命令串起来。
- 必会参数：-i 输入、-c:v/-c:a 指定编码器、-b:v 码率、-vf 滤镜（缩放/水印）、-g GOP、-preset 速度与压缩率权衡、-f 输出格式。
- 直播转码典型需求：源转多档 ABR ladder，GOP 与分片时长对齐（2s 分片配 48 帧 GOP@24fps）。
- 前端要懂到能自测：排查"上传的视频播不了"时自己转一版标准参数验证，是快速二分问题位置的手段。

```bash
# 点播转 HLS：1080p 源转 720p 一档，GOP 与 2 秒分片对齐
ffmpeg -i input.mp4 \
  -vf "scale=-2:720" -c:v libx264 -preset medium -b:v 2500k -maxrate 2750k -bufsize 5000k \
  -g 48 -keyint_min 48 -sc_threshold 0 \
  -c:a aac -b:a 128k \
  -hls_time 2 -hls_list_size 0 -hls_playlist_type vod \
  master_720.m3u8

# 抽查码流信息：分辨率、编码、码率、帧率
ffprobe -v error -show_streams -show_format master_720.m3u8

# 直播推流联调（-re 按原速读文件，常用于压测与端到端联调）
ffmpeg -re -stream_loop -1 -i loop_source.mp4 -c:v libx264 -preset veryfast \
  -b:v 2000k -g 50 -c:a aac -f flv rtmp://push.example.com/live/stream001
```
