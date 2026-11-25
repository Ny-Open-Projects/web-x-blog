---
title: [PER-291] 用 Performance 面板定位一次"点击后 800ms 才响应"的完整流程是怎样的？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-291：用 Performance 面板定位一次"点击后 800ms 才响应"的完整流程是怎样的？

**答**：
- 复现录制：Performance 面板 + CPU 4x 降速（贴近用户设备）+ 勾选 Screenshots，点击"录制"，执行卡顿操作，停止录制。
- 定位交互：Interactions 轨道找到这次点击（黄色块，长度即交互总时长）；Events 轨道看事件派发时间。块右端的滞后部分 = input delay + processing + presentation。
- 三段拆解：点击块内看 Main 轨道——点击前是否被其他长任务占着（input delay 段）；事件 handler 的火焰图（processing 段，展开找到热点函数与自耗时）；handler 结束后的 Layout/Paint/Composite（presentation 段，看紫色 Layout 是否爆炸）。
- 归因后修复对照：input delay 长 → 找占用主线程的先行任务切片；processing 长 → 热点函数优化/挪 worker；presentation 长 → 查强制同步布局（Performance Mark "Recalculate Style" 前的 offsetWidth 读取）与大面积重绘。
- 验证：修改后重录同操作对比时间轴，交互块长度缩短到 <200ms 才算修完。

```text
Performance 面板定位步骤（800ms 点击卡顿示例）：
1. Interactions 轨道: click 812ms
2. Main 轨道展开:
   [0-300ms] 前置长任务 parseResponse —— 占住主线程 => input delay 300ms
   [300-680ms] onSearchClick 火焰图 → renderResults() 自耗时 350ms => processing
   [680-812ms] Recalculate Style + Layout 反复 => presentation 130ms
3. 证据链: renderResults 里读写交错（offsetHeight 后 set style）=> 强制同步布局
4. 修复: 读写分离（先批量读再批量写）+ 结果渲染切片 + 前置任务挪 worker
5. 复测: click 152ms（三段 30/80/42），达标
```
