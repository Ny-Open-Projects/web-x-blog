---
title: [SCN-166] 在线答题 PK 双人同屏竞技，倒计时必须双方一致，如何对抗网络延迟与时钟偏差？
date: 2026-11-17
categories: [场景实战]
tags: [前端面试, 面试题, 11]
type: 面试题
---

## SCN-166：在线答题 PK 双人同屏竞技，倒计时必须双方一致，如何对抗网络延迟与时钟偏差？
**答**：
- 展示时钟必须锚定服务器时间：开局时服务端下发 `startAt（服务器时间戳）+ duration`，前端按"服务器时间 - 本地时间"偏移计算剩余，而不是自己起 setInterval。
- 服务器时间偏移用 NTP 式三采样取最小 RTT 那次的偏移（RTT 最小 = 最准）。
- 判定权在服务端：答题提交带客户端本地耗时仅作参考，服务端按收到时间判定是否超时，前端倒计时到 0 只是锁 UI。
- 网络抖动的补偿：倒计时与对方答题推送用同一时钟基准展示；掉线重连后立即重新对时 + 拉题目状态快照。

```javascript
// 答题 PK 计时：服务器时间锚定 + 三采样取最优 + 服务端判定
export async function calibrateNTP(fetchTime) {
  let best = null;
  for (let i = 0; i < 3; i++) {                        // 三次采样，取 RTT 最小的
    const t0 = Date.now();
    const { serverTime } = await fetchTime();
    const rtt = Date.now() - t0;
    const offset = serverTime - t0 - rtt / 2;
    if (!best || rtt < best.rtt) best = { rtt, offset };
  }
  return best.offset;
}

export class PkTimer {
  constructor({ serverStartAt, durationMs, offset }) {
    this.startAt = serverStartAt;                      // 服务器开考时间
    this.durationMs = durationMs;
    this.offset = offset;
    this.finished = false;
  }
  remainMs() {
    const serverNow = Date.now() + this.offset;        // 一切以服务器时钟为准
    return Math.max(0, this.startAt + this.durationMs - serverNow);
  }
  start(onTick, onEnd) {
    const loop = () => {
      const remain = this.remainMs();
      onTick(remain);
      if (remain <= 0 && !this.finished) { this.finished = true; onEnd(); return; }
      this.raf = requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }
}

// 提交：带本地耗时仅作参考，超时与否由服务端收到时间判定
export async function submitAnswer(questionId, choice, timer) {
  const localCost = timer.durationMs - timer.remainMs();
  try {
    return await api.submitAnswer({ questionId, choice, localCost, clientTs: Date.now() });
  } catch (e) {
    if (e.code === 'TIMEOUT') return { accepted: false, reason: '已超时' }; // UI 锁死但服务端裁决
    throw e;
  }
}
```
