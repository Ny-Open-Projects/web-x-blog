---
title: [OPT-104] GIF 转视频的收益怎么量化？怎么落地自动转换？
date: 2026-11-17
categories: [性能优化]
tags: [前端面试, 面试题, 12]
type: 面试题
---

## OPT-104：GIF 转视频的收益怎么量化？怎么落地自动转换？

**答**：
- 同画面 GIF vs MP4/WebM：体积差 10-30 倍（GIF 每帧全量存储 + 256 色 + 无帧间压缩），且 GIF 解码在主线程、视频解码走硬件管线，CPU 差一个量级。
- 落地：构建期/上传期用 ffmpeg 把 .gif 转成 `mp4(H.264, 无音轨)` 或 `webm(VP9)`，页面用 `<video autoplay muted loop playsinline>` 无缝替换，观感与 GIF 一致。
- 兜底：不支持 video 循环的极端场景极少了，可忽略；真正要注意的是**移除音轨**（`-an`），否则自动播放策略可能拦住。
- 量化方法：转码前后文件体积对比 + Performance 面板看 GIF 帧解码的 Script/Raster 占用消失。

```bash
# 一一对应：GIF 转视频的 ffmpeg 命令与体积收益核对
# 输入 demo.gif 12MB；转 H.264 MP4 无音轨，与 GIF 同帧率
ffmpeg -i demo.gif \
  -movflags faststart \      # moov box 前置：边下边播，首帧提前
  -an \                      # 去音轨：满足 muted 自动播放 + 省体积
  -vf "fps=24,scale=640:-2:flags=lanczos" \ # 限制帧率与宽度，-2 保证偶数高
  -c:v libx264 -crf 26 \     # crf 26：动图场景画质无感，体积再减半
  -pix_fmt yuv420p \         # 兼容所有播放器的像素格式
  demo.mp4
# WebM 备选（更小但编码慢，iOS 老版本兼容注意）：
ffmpeg -i demo.gif -an -c:v libvpx-vp9 -crf 34 -b:v 0 -vf fps=24,scale=640:-2 demo.webm

# 批量转换 + 体积报告（构建脚本用）：
# for f in assets/*.gif; do
#   ffmpeg -y -i "$f" -movflags faststart -an -vf fps=24,scale=640:-2 -c:v libx264 -crf 26 -pix_fmt yuv420p "${f%.gif}.mp4"
# done
# du -h assets/*.gif assets/*.mp4 | sort
# 典型输出：demo.gif 12M -> demo.mp4 680K，体积 -94%，解码走硬件管线

# 页面替换规则（与 OPT-018 facade 一致）：
# <video autoplay muted loop playsinline poster="demo-poster.avif">
#   <source src="demo.webm" type="video/webm"><source src="demo.mp4" type="video/mp4">
# </video>
```
