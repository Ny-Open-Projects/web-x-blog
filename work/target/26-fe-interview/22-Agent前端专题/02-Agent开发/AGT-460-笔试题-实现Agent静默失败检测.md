---
title: [AGT-460] 笔试题——实现静默失败检测（心跳超时+无进展判定+自动恢复）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-460：手写静默失败检测：心跳窗口、进度指纹、超时分级处置

**需求与边界**：
- 输入：事件流监控器、心跳间隔、恢复动作；输出：异常检测与恢复触发。
- 边界要求：① 心跳超时（>N 秒无任何事件）触发告警；② "有事件但无进展"（长工具运行正常 vs 假活）区分——进度指纹检测；③ 分级处置：重连→降级轮询→告知用户；④ 恢复后状态对齐（seq 续传）。

**答**：
```javascript
class SilentFailDetector {
  constructor({ heartbeatMs = 15000, onTimeout, onProgressStall }) {
    this.heartbeatMs = heartbeatMs;
    this.handlers = { onTimeout, onProgressStall };
    this.reset();
  }
  reset() {
    this.lastEvent = Date.now();
    this.lastFingerprint = '';
    this.stallCount = 0;
    clearTimeout(this.timer);
    this.timer = setTimeout(() => this.check(), this.heartbeatMs);
  }
  onEvent(ev) {
    this.reset();                                  // 任何事件重置心跳
    // 进度指纹：delta 长度+工具状态变化
    const fp = `${ev.type}:${ev.payload?.len ?? ''}`;
    if (fp === this.lastFingerprint && ev.type === 'tool_status')
      this.stallCount++;
    else this.stallCount = 0;
    this.lastFingerprint = fp;
  }
  check() {
    const silent = Date.now() - this.lastEvent;
    if (silent > this.heartbeatMs * 2) {           // 心跳超时
      // 分级：先重连，再轮询，最后告知
      this.handlers.onTimeout({ silentMs: silent,
        recover: async () => {
          const r = await reconnect();             // 1. SSE 重连
          if (!r.ok) r = await pollFullState();    // 2. 降级轮询
          if (!r.ok) this.handlers.onTimeout({ escalate: true }); // 3.
          if (r.seq != null) seek(r.seq);          // seq 对齐恢复
        } });
      return;
    }
    if (this.stallCount >= 3) {                    // 有事件但假活
      this.handlers.onProgressStall({
        note: '工具状态长时间未变化',
        action: '提示用户"任务可能卡住，可取消重试"' });
    }
    this.timer = setTimeout(() => this.check(), this.heartbeatMs);
  }
  dispose() { clearTimeout(this.timer); }
}
```

**评分点**:
- 心跳超时与"有事件无进展"两类检测分开（真静默 vs 假活）。
- 分级恢复链：重连→轮询→告知用户，seq 对齐续传不丢内容。
- 进度指纹与 stallCount 阈值防误报。
- dispose 清理定时器（组件卸载无泄漏）。
