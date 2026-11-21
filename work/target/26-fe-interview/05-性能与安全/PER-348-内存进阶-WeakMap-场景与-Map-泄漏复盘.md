---
title: [PER-348] 一个真实的 Map 泄漏事故复盘：从内存告警到定位到修复的完整链路？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-348：一个真实的 Map 泄漏事故复盘：从内存告警到定位到修复的完整链路？

**答**：
- 症状：长驻客服工作台 SPA，用户挂机 4 小时后页面卡顿、报"内存不足"。heap baseline 监控显示 jsHeap 从 80MB 阶梯涨到 700MB 不回落（版本对比发现新版本引入，发版时间轴对上）。
- 定位：三快照法（PER-264）——反复打开/关闭"工单列表"标签页，Comparison 显示 `TicketCache` 类实例 + 数千条 detached div。Retainers 链：detached DOM ← 数据节点 ← 全局 `window._ticketMap`（模块级 Map，只 set 不 delete）。
- 根因：新版本加了"工单预取"，把每张工单的完整 DOM 快照（含引用）塞进模块级 Map 做缓存，无上限、无 TTL；用户切换标签页越多积累越多。
- 修复：① 缓存改 LRU（容量 50）+ TTL 10 分钟（PER-268 模式）；② 缓存里只存序列化数据不存 DOM 引用；③ 加上线内存回归监控（PER-278 detectLeak 进 CI 冒烟）防复发。
- 复盘产出：全局缓存审批制度（新全局缓存必须声明容量与淘汰策略）、内存基线纳入版本对比看板。

```text
事故时间轴（复盘模板）：
T+0h   用户反馈卡顿 → heap baseline 告警（版本 v2.3.1 内存 +60%）
T+0.5h 三快照复现：TicketCache +3 个/操作，retained 120MB/个
T+1h   Retainers 定位：window._ticketMap（v2.3.1 新增代码）
T+1.5h 修复 PR：LRU(50)+TTL(10min)+去 DOM 引用
T+2h   CI 内存冒烟接入（detectLeak）；看板加"内存版本对比"卡片
T+4h   灰度 10% 验证 24h 基线回落 → 全量
复盘产出：全局缓存审批制度 + 案例库归档（tags: [Map泄漏, 全局缓存, 长驻SPA]）
```
