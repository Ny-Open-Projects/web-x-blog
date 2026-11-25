---
title: [AV-123] 播放器错误恢复矩阵怎么设计？网络错、解码错、DRM 错分别怎么处理？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-123：播放器错误恢复矩阵怎么设计？网络错、解码错、DRM 错分别怎么处理？（高频）
**答**：
- 分类才有策略：网络类（manifest/frag 失败）、媒体类（demux/decode 失败）、DRM 类（license 失效）、业务类（URL 过期/区域限制）。
- 错误必须带上下文上报：code、url、当前 level、buffer 水位、重试次数——没有上下文线上无法归因。
- 恢复阶梯：原地重试 → 降清晰度 → 换协议（FLV→HLS→MP4）→ 换 CDN → 重建播放器实例 → 提示用户。
- 重试要退避 + 上限：指数退避 1s/2s/4s，同一错误连续 3 次失败升级到下一级策略。
- 体验原则：恢复中显示"重连中"不黑屏，恢复成功无缝续播（记住 currentTime）。

```json
{
  "error-recovery-matrix": {
    "network.manifest.timeout": { "retry": 3, "backoff": "exp", "next": "switchCdn" },
    "network.frag.404":        { "retry": 1, "next": "skipFragment", "note": "直播直接跳过过期分片" },
    "media.decode.failed":     { "retry": 0, "next": "recoverMediaError", "then": "lowerLevel" },
    "media.buffer.stalled":    { "retry": 0, "next": "nudgeSeek", "note": "seek 当前时间戳踢活解码器" },
    "drm.license.expired":     { "retry": 0, "next": "refreshLicense", "note": "静默续期不重启播放" },
    "drm.unsupported":         { "retry": 0, "next": "fallbackUrl", "note": "切无DRM或软解方案" },
    "business.url.expired":    { "retry": 0, "next": "refreshToken", "note": "重新签名后重建实例" }
  },
  "report-fields": ["errCode", "errDetail", "url", "level", "bufferSec", "retryCount", "currentTime", "networkType"]
}
```
