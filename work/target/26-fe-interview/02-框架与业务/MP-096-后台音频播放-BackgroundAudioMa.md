---
title: [MP-096] 后台音频播放 BackgroundAudioManager 怎么用？
date: 2026-11-17
categories: [小程序]
tags: [前端面试, 面试题, 19]
type: 面试题
---

## MP-096：后台音频播放 BackgroundAudioManager 怎么用？
**答**：
- `wx.getBackgroundAudioManager()`：全局单例，**必须设置 title** 才能后台播放（iOS 要求）；系统通知栏/锁屏由平台接管。
- 事件：onPlay/onPause/onEnded/onNext（锁屏控制）；seek 用 currentTime 赋值。
- 与 InnerAudioContext 区分：inner 用于短音效（不能后台），background 用于播客/音乐场景；注意 obeyMuteSwitch 与音频焦点差异。

```javascript
const bgm = wx.getBackgroundAudioManager()
bgm.title = '第 12 期播客'        // 必填，否则不播放
bgm.epname = '前端夜谈'
bgm.src = 'https://cdn.example.com/ep12.mp3'
bgm.onEnded(() => this.playNext())   // 播完自动连播
bgm.onNext(() => this.playNext())    // 锁屏下一首
```
