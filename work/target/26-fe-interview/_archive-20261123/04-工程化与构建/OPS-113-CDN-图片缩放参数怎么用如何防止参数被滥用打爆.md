---
title: [OPS-113] CDN 图片缩放参数怎么用？如何防止参数被滥用打爆回源？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-113：CDN 图片缩放参数怎么用？如何防止参数被滥用打爆回源？
**答**：
- 原图只存一份，尺寸/格式/质量通过 URL 处理参数在边缘实时生成并缓存（OSS x-oss-process、七牛 imageView2、Cloudinary 转换串）。
- 与响应式布局配合：列表缩略图用小图参数，详情页中图，下载场景原图；webp/avif 按客户端能力协商，可再省 30-50% 体积。
- 处理参数也是缓存键的一部分：改参数等于新资源（自然填充新缓存），旧 key 不受影响。
- 必须收敛参数：用"样式名"替代裸参数（style_thumb300），或 CDN 层白名单允许的参数组合，否则攻击者可构造任意尺寸请求打爆回源带宽与计费。
- 监控"未命中缓存的新参数"请求量，异常激增即告警。

```bash
# CDN 图片处理参数实操
# 1. 列表缩略图：宽 300、质量 80、webp（原图只存一份）
curl -sI "https://img.example.com/product/12345.jpg?x-oss-process=image/resize,w_300/quality,q_80/format,webp" \
  | grep -Ei 'content-type|content-length|x-cache'

# 2. 生产实践：把参数收敛为样式名（OSS 控制台配置 style_thumb300 = resize,w_300,q_80,format,webp）
#    白名单化的好处：URL 不可构造任意参数，回源组合可控
curl -sI "https://img.example.com/product/12345.jpg?x-oss-process=style/style_thumb300" | head -5

# 3. 前端按能力协商格式：<picture> 内 source type=image/avif + webp + jpg 兜底
# 4. 滥用监控：统计新参数（未命中缓存的 key）请求数
awk -F'?' '/img.example.com/ {print $2}' access.log | sort -u | wc -l   # 独立参数组合数突增即告警
```
