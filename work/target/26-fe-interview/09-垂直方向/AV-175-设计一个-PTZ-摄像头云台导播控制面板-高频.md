---
title: [AV-175] 设计一个 PTZ 摄像头云台导播控制面板。（高频）
date: 2026-11-17
categories: [音视频RTC]
tags: [前端面试, 面试题, 26]
type: 面试题
---

## AV-175：设计一个 PTZ 摄像头云台导播控制面板。（高频）
**答**：
- PTZ = Pan/Tilt/Zoom，控制协议 ONVIF/VISCA-over-IP：前端发指令 → 控制服务 → 摄像头执行。
- UI：方向舵（按住连发松开停）、变焦滑杆、预置位存/调、巡航路径编辑。
- 联动导播：说话人检测驱动自动跟踪（AI 找人脸 → 云台转向），人工指令优先级最高。
- 时延控制：显示控制链路 RTT，慢时降低指令频率防"过冲"（云台惯性）。
- 多机位：预置位集按场景组织，一键场景宏（机位 + 预置位 + 导播切换绑定）。

```typescript
// PTZ 控制指令节流与预置位管理
class PtzController {
  private timer?: number;
  constructor(private ws: WebSocket) {}
  move(dir: 'pan-left' | 'pan-right' | 'tilt-up' | 'tilt-down', speed = 5) {
    if (this.timer) return;                 // 按住连发但限频 防过冲
    this.send({ cmd: dir, speed });
    this.timer = window.setTimeout(() => (this.timer = undefined), 120);
  }
  stop() {                                  // 松手即停
    if (this.timer) { clearTimeout(this.timer); this.timer = undefined; }
    this.send({ cmd: 'stop' });
  }
  recallPreset(i: number) { this.send({ cmd: 'preset-goto', id: i }); }
  savePreset(i: number) { this.send({ cmd: 'preset-set', id: i }); }
  private send(p: object) { this.ws.send(JSON.stringify({ type: 'ptz', ...p })); }
}
// 方向键 keydown 触发 move keyup 触发 stop
```
