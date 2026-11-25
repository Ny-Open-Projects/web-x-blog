---
title: [AV-019] DASH 和 HLS 有什么区别？该怎么选？
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-019：DASH 和 HLS 有什么区别？该怎么选？
**答**：
- MPEG-DASH 是国际标准（非 Apple 私有），manifest 为 XML 的 MPD，支持 SegmentTemplate/SegmentTimeline 灵活描述分片。
- DASH 支持 per-Title 编码、按字节范围寻址、多轨道（多语言/字幕）表达更精细；HLS 生态与 CDN 兼容性更好。
- 低延迟：DASH 有 LL-DASH（chunked segment），HLS 有 LL-HLS；功能趋同。
- 选型：对外传播/苹果设备必带 HLS；drm 与多语言复杂场景 DASH 表达力强；国内直播基本 HLS+FLV 双出，点播 HLS 为主。
- 浏览器：Chrome/Edge/Firefox 原生支持 DASH（仍需 dash.js MSE 播放），Safari 只认 HLS（但可原生播）。

```xml
<!-- DASH MPD 关键片段：SegmentTemplate 模板化分片 -->
<MPD xmlns="urn:mpeg:dash:schema:mpd:2011" type="dynamic">
  <Period>
    <AdaptationSet contentType="video">
      <Representation id="1080p" bandwidth="3000000" width="1920" height="1080">
        <SegmentTemplate
          media="$RepresentationID$/seg-$Number$.m4s"
          initialization="$RepresentationID$/init.mp4"
          startNumber="1" duration="4" timescale="90000"/>
      </Representation>
      <Representation id="720p" bandwidth="1200000" width="1280" height="720">
        <SegmentTemplate media="$RepresentationID$/seg-$Number$.m4s"
          initialization="$RepresentationID$/init.mp4"
          startNumber="1" duration="4" timescale="90000"/>
      </Representation>
    </AdaptationSet>
  </Period>
</MPD>
```
