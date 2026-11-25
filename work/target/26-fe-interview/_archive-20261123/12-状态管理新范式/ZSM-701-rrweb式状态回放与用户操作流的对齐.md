---
title: [ZSM-701] rrweb 式回放：把用户操作流与状态变更流对齐到同一时间轴
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-701：rrweb 式回放：把用户操作流与状态变更流对齐到同一时间轴

**答**：
- 回放排查「用户点了什么导致状态错了」需要两条流合一：**DOM 流**（rrweb 的 MutationObserver 快照，可视化用户看到什么）与**状态流**（store 探针的变更事件）。对齐方案：两条流都用 `performance.now()` 时间戳记录，回放时在 DOM 时间轴上叠加状态事件标记（点击某按钮 → 3ms 后 cart/addItem → 12ms 后 Badge 重渲）。
- 采集成本控制：DOM 流全量录制很贵——只录「问题会话」（错误上报触发后开始录环形缓冲最后 30s + 后续实时），或采样 1%。状态流本身轻（元数据），可全量。
- 时间基线坑：rrweb 用自身 timestamp，状态探针用 Date.now/performance.now——统一基线必须在录制开始时打点对齐（`startTs = Date.now()` 与 rrweb 的 events[0].timestamp 绑定）。
- 回放交互：时间轴 scrub 时状态面板跟随——「拖到任意时刻显示当时 store 快照 + 接下来 1s 的变更预告」，这需要快照重建（从初始状态重放事件到目标时刻，ZSM-553/562 的重放器复用）。
- 追问钩子：隐私裁剪——rrweb 的 `maskAllInputs/obfuscate` 配合状态流的「只记字段名不记值」，保证回放不含 PII。

```javascript
// 双流采集与对齐
class ReplayCollector {
  #stateEvents = []    // { ts, action, keys }
  #domRecorder        // rrweb record 实例
  #startTs = 0

  start() {
    this.#startTs = Date.now()
    this.#domRecorder = rrweb.record({
      emit: (e) => { /* rrweb 事件自带 timestamp */ },
      maskAllInputs: true,
      sample: { mousemove: false, input: 'last' },   // 降采样
    })
    storeProbe.subscribe((e) => {
      this.#stateEvents.push({ ts: Date.now(), ...e })   // 状态流用 Date.now 与基线一致
    })
  }

  stop() {
    return {
      startTs: this.#startTs,
      dom: this.#domRecorder.getEvents?.() ?? [],
      state: this.#stateEvents,
    }
  }
}

// 回放叠加：rrweb-player 的 timeupdate 钩子
player.on('finish', () => {})
player.addEventListener('ui-update-current-time', (e) => {
  const t = replay.startTs + e.detail   // rrweb 时间 → 绝对时间
  // 找到该时刻附近的状态事件 → 面板显示快照
  const near = replay.state.filter((s) => Math.abs(s.ts - t) < 500)
  statePanel.render(near, buildSnapshotAt(t))   // 重放器重建快照
})

function buildSnapshotAt(t) {
  // 从初始快照重放 t 之前的状态事件
  let snap = replay.initial
  for (const e of replay.state) {
    if (e.ts > t) break
    snap = applyChange(snap, e)
  }
  return snap
}
```
