---
title: [RBL-420] 笔试：手写 Runner 资源画像采集
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-420：手写 Runner 资源画像采集
**答**：实现 `profileProcess(child)`：1) 采集子进程 CPU/内存：定时采样（pidstat 不可用时 /proc 读取——Linux）或 process.report（Node 子进程内嵌上报）；2) 峰值内存/CPU/时长记录；3) 资源画像输出：{ peakRssMB, cpuPercent, durationMs, samples }；4) 采样频率自适应（短任务 500ms、长任务 2s）；5) 跨平台降级：非 Linux 用 Node 内建 process.memoryUsage（子进程内上报 IPC）；6) 画像用于调度决策（内存预算 × 并发度）。

```javascript
import fs from 'node:fs'

export function profileProcess(child, { baseInterval = 500 } = {}) {
  const samples = []
  let timer = null, stopped = false
  let interval = baseInterval

  function sampleLinux(pid) {
    try {
      const stat = fs.readFileSync(`/proc/${pid}/stat`, 'utf8').split(' ')
      const rssPages = +stat[23]
      const utime = +stat[13], stime = +stat[14]
      return { rssMB: (rssPages * 4096) / 1024 ** 2, cpuTicks: utime + stime }
    } catch { return null }                          // 进程已退出
  }

  function start() {
    const tick = () => {
      if (stopped) return
      const s = child.platform === 'linux' ? sampleLinux(child.pid) : child.ipcSample?.()
      if (s) samples.push({ at: Date.now(), ...s })
      // 自适应：总时长超 30s 降频
      if (samples.length > 60) interval = 2000
      timer = setTimeout(tick, interval)
    }
    tick()
    return new Promise((resolve) => {
      child.on('exit', (code) => {
        stopped = true; clearTimeout(timer)
        const peakRss = Math.max(0, ...samples.map((s) => s.rssMB ?? 0))
        resolve({ peakRssMB: +peakRss.toFixed(1),
          cpuPercent: cpuOf(samples), durationMs: Date.now() - child.startAt, samples })
      })
    })
  }

  function cpuOf(samples) {
    if (samples.length < 2) return 0
    const first = samples[0], last = samples[samples.length - 1]
    const ticks = last.cpuTicks - first.cpuTicks
    const wallMs = last.at - first.at
    return +((ticks * 10 / wallMs) * 100).toFixed(1)   // tick=10ms（假设 100Hz）
  }

  return { start }
}
```
**评分点**：
- 双通道采集（/proc 外部采样 + IPC 内嵌上报跨平台降级）
- 峰值口径（samples 取 max）；CPU 百分比换算（ticks→wall 比例）
- 采样自适应降频（长任务不爆采样量）
- 用途闭环：画像驱动并发度（内存预算 × 并发）——采集要能被调度消费
