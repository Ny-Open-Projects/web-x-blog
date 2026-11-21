---
title: [MFW-398→MFW-398] 万模块仓库的 HMR 稳定性治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW→MFW-398：万模块 HMR

**答**:
- 症状族：偶发 full-reload（本应热更）、内存缓慢上涨（数小时 dev 挂）、特定文件类型改动必炸——万模块下从「偶发」变「每小时」
- 治理三线：①范围收窄（watch 忽略生成物/大目录；虚拟模块依赖声明精确——误伤即 full-reload）②泄漏定位（dev 进程 heap 对比：1h vs 起点——定位到 loader/插件闭包持有；RBL-473 思路进 dev 服务器）③边界隔离（monorepo 按域拆 dev server 进程——Turbo/隔离 dev，B 团队改动不进 A 的图）
- 度量：HMR 成功率/平均耗时/full-reload 率——三指标周报（dev 体验 SLO：full-reload <2%）
- 底线方案：持续性不稳的域用「快速可靠 full-reload」（状态持久化到 sessionStorage+秒级重载——体验可接受的中转站）

```text
三线：watch/虚拟模块范围收窄 / dev heap 对比定位插件泄漏 / 按域拆 dev 进程
SLO：HMR 成功率/full-reload <2% 周报
底线：不稳域 → 状态持久化+秒级可靠重载中转
```
