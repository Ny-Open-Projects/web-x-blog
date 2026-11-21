---
title: [AV-116] 录制与转推在 SFU 侧怎么做？前端要注意什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-116：录制与转推在 SFU 侧怎么做？前端要注意什么？（高频）
**答**：
- 两条路：服务端旁路录制（SFU 转 RTP 给 GStreamer/ffmpeg 合流落盘）与客户端本地合成（MediaRecorder）。
- 服务端合流：布局由服务端混流模板决定，客户端断线不影响成片；音画同步靠 RTCP SR 的 NTP/RTP 映射。
- 转推：把房间内容合成后转 RTMP 推给 CDN——"RTC 连麦 + CDN 大盘观众"融合直播的桥接点（关联 AV-036）。
- 前端注意：服务端录制的是"SFU 收到的流"，本地美颜/滤镜不在成片里；要一致就得把处理后的流推上来。
- 业务提示：录制/转推必须有全员可见的合规提示（AV-143）。

```bash
# SFU 旁路：接收 SFU 转出的 RTP（SDP 描述端口）并合成录制
# 两路视频左右拼接 + 两路音频混音，输出 mp4
ffmpeg -protocol_whitelist file,udp,rtp \
  -i video1.sdp -i video2.sdp -i audio1.sdp -i audio2.sdp \
  -filter_complex "[0:v]scale=640:360,pad=1280:360[v0];[1:v]scale=640:360[v1];[v0][v1]hstack[top];[2:a][3:a]amix=inputs=2:duration=longest[aout]" \
  -map "[top]" -map "[aout]" -c:v libx264 -preset veryfast -b:v 2000k \
  -c:a aac -b:a 128k meeting_record.mp4

# 合流结果转推 CDN（生产中由合流服务直接推流，避免二次转码）
ffmpeg -re -i meeting_record.mp4 -c copy -f flv rtmp://push.example.com/live/room42
```
