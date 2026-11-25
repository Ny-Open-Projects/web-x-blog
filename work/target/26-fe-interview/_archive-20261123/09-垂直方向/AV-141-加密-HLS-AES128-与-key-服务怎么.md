---
title: [AV-141] 加密 HLS（AES-128）与 key 服务怎么搭？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-141：加密 HLS（AES-128）与 key 服务怎么搭？（高频）
**答**：
- 原理：分片用 AES-128-CBC 加密，m3u8 里 `#EXT-X-KEY:METHOD=AES-128,URI="key接口"`，播放器先取 key 再解密分片。
- key 服务：校验播放令牌（token 绑定用户/设备/时效）后才返回 16 字节密钥；可做 per-user key 与定期轮换（m3u8 中 EXT-X-KEY 换版）。
- 安全层级：不加密 < Referer/Token < AES-128（抓包拿到 ts 也解不开）< DRM（防录屏级）。
- 坑：key 接口必须 no-store 不缓存；CORS 要配好；Safari 原生 HLS 自持解密但 key 请求带不走自定义 header。
- 实操：ffmpeg 一条命令产出加密分片 + keyinfo，联调方便。

```bash
# 生成密钥与 IV，写 keyinfo 交给 ffmpeg 加密转 HLS
openssl rand 16 > enc.key
openssl rand -hex 16 > enc.iv.hex

cat > keyinfo <<EOF
https://api.example.com/hlskey?token=PLAYBACK_TOKEN
./enc.key
IV_HEX_VALUE
EOF
# keyinfo 三行: 第一行是播放器请求密钥的URI 第二行本地密钥文件 第三行IV

ffmpeg -i input.mp4 -c:v libx264 -c:a aac \
  -hls_time 4 -hls_playlist_type vod \
  -hls_key_info_file keyinfo \
  -hls_segment_filename 'seg_%03d.ts' index.m3u8
# 产出: index.m3u8 内含 EXT-X-KEY 指向 key 接口 + 加密分片
# key 服务逻辑: 校验 PLAYBACK_TOKEN 有效性后才返回密钥字节
```
