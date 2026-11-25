---
title: [AV-177] WebRTC 项目实战复盘：一次跨国会议的延迟与卡顿优化。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-177：WebRTC 项目实战复盘：一次跨国会议的延迟与卡顿优化。（高频）
**答**：
- 背景：中美双方参会，国内端看美国端画面频繁卡顿，connectionState 时连时断。
- 定位：getStats 显示 relay 占比 100%（全走 TURN）、RTT 300ms+、丢包 8%；根因是 TURN 单点部署在美国西部，亚洲端绕美。
- 措施一：TURN 多区域就近部署（香港/法兰克福），RTT 降到 90ms、丢包降到 1%。
- 措施二：simulcast 从 2 档加到 3 档 + SFU 按订阅端网络选层；弱网端 jitterBufferTarget 调到 150ms 保音频优先。
- 结果与沉淀：卡顿率 12% → 1.8%；沉淀"跨国会议 checklist"（TURN 拓扑、编码档位、地区维度监控基线）。

```text
# 复盘时间线与归因（模板）
T0  反馈: 跨国会议画面频繁卡顿
T1  采样 getStats: candidateType=relay 100% RTT 280-340ms 丢包 6-9%
T2  根因: TURN 单点部署在美国 亚洲端绕美 路径劣化
T3  措施A: TURN 多区域部署 按用户地理位置就近接入
T4  措施B: simulcast 增加低档 SFU 按订阅端网络选层
T5  措施C: 弱网端 jitterBufferTarget=150ms 音频优先
T6  结果: RTT<100ms 卡顿率 12% 到 1.8%
checklist 沉淀
  1 TURN 节点必须按区域就近部署
  2 跨国场景必开 simulcast 三档
  3 getStats 定时上报 建立地区维度基线
```
