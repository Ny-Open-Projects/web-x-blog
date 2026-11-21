---
title: [AV-130] 清晰度与码率怎么平衡？VMAF 是什么？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-130：清晰度与码率怎么平衡？VMAF 是什么？（高频）
**答**：
- 码率↑画质↑但带宽成本线性涨；用户感知的是主观画质，PSNR/SSIM 与人眼相关性差。
- VMAF：Netflix 开源的主观画质评价指标（0-100），转码服务的目标是"每档码率下 VMAF 最高"的编码参数。
- ABR 档位表应是"VMAF 意义上的阶梯"：相邻档画质差可感知（ΔVMAF > 5），否则切档没有意义。
- 实操：转码上线前用测试序列扫参（CRF × preset），找出该内容类型的甜点参数；直播用固定模板 + 定期复核。
- 排查思路：高码率仍模糊 → 多半是多次转码代际损失或源片分辨率不足，不是码率问题。

```bash
# 用 libvmaf 对比转码输出与源片：输出 vmaf.json 的均值即画质分
ffmpeg -i transcoded_720p.mp4 -i source_1080p.mp4 \
  -lavfi "[0:v]setpts=PTS-STARTPTS[dist];[1:v]scale=1280:720,setpts=PTS-STARTPTS[ref];[dist][ref]libvmaf=log_path=vmaf.json:log_fmt=json:feature=name=psnr" \
  -f null -

# 分数解读: >93 优秀 85-93 良好 <80 明显劣化
# 扫参找甜点：同一源转 CRF 18/21/24，取 VMAF 分数与码率的平衡点
for crf in 18 21 24; do
  ffmpeg -y -i source.mp4 -c:v libx264 -crf $crf -preset slow -an out_$crf.mp4
done
```
