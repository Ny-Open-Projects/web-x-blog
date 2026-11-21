---
title: [AV-124] 直播时移与回看（DVR）怎么实现？（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-124：直播时移与回看（DVR）怎么实现？（高频）
**答**：
- DVR 本质：服务端把直播分片保留 N 小时并维护滚动/持续增长的 m3u8（EXT-X-PLAYLIST-TYPE: EVENT 不删旧分片），观众可 seek 到过去任意时刻。
- 时移播放 = seek 到"直播边缘 - offset"；播放器要识别"追上边缘后回到直播模式"。
- 进度条特殊化：直播页进度条映射"最近 N 小时"，右端是 LIVE 红点，拖走后显示"回到直播中"按钮。
- m3u8 带 EXT-X-PROGRAM-DATE-TIME 时可按真实时间定位（回看上午 10 点的比赛）。
- 工程要点：长 DVR 的 m3u8 变大要分段清理；seek 后要做 buffer 裁剪避免内存膨胀（关联 AV-182）。

```text
#EXTM3U
#EXT-X-VERSION:6
#EXT-X-TARGETDURATION:2
#EXT-X-PLAYLIST-TYPE:EVENT
#EXT-X-MEDIA-SEQUENCE:0
#EXT-X-PROGRAM-DATE-TIME:2026-11-08T10:00:00.000+08:00
#EXTINF:2.000,
seg_00000.ts
#EXT-X-PROGRAM-DATE-TIME:2026-11-08T10:00:02.000+08:00
#EXTINF:2.000,
seg_00001.ts
... 保留 4 小时即 7200 个分片 播放器按 PDT 定位后顺序拉取
#EXT-X-ENDLIST 只在直播结束时写入
```
