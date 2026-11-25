---
title: [SCN-1171] SCADA 大屏的断电重启自恢复
date: 2026-11-22
categories: [场景实战]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## SCN-1171：SCADA 大屏的断电重启自恢复

**答**：
- 自恢复：大屏机器断电重启——开机自启浏览器（kiosk 模式）+ 自动重连 WS + 数据从断点续显。
- 校验：重启后数据完整性校验（最后时间戳对比）。
- 监控：大屏心跳（运维监控大屏本身在线）。

```javascript
// 断电自恢复
function kioskAutoRecover() {
  return {
    autostart: 'browser --kiosk http://scada.local',
    reconnect: exponentialBackoff(5_000),
    integrity: () => checkLastTs(),                    // 数据断点校验
    heartbeat: reportScreenAlive(),                    // 大屏心跳
  };
}
function exponentialBackoff(base) { return base; }
function checkLastTs() { return true; }
function reportScreenAlive() { return true; }
```
