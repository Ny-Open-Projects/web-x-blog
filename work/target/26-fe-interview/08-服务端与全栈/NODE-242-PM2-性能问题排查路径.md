---
title: [NODE-242] PM2 性能问题排查路径？
date: 2026-11-19
categories: [Node.js与BFF]
tags: [前端面试, 面试题, 20]
type: 面试题
---

## NODE-242：PM2 性能问题排查路径？
**答**:
- 排查漏斗：现象（P95 高/错误率升）→ 进程指标（pm2 monit CPU/内存/restarts）→ 单进程内诊断（clinic NODE-083）→ 代码热点。
- restart 频繁：max_memory_restart 触发（泄漏）或异常崩溃（看 err log）——先分类再深挖。
- CPU 打满：确认是否事件循环阻塞（NODE-209 ELU 指标）→ 热点是否 CPU 密集任务未卸载（NODE-226）→ worker 池补位。
- 实例间差异：某 worker P95 异常高（长连接偏差 NODE-240 / 数据倾斜）——按 worker id 拆分指标。

```bash
# 排查链路
pm2 monit                     # 1) 进程级 CPU/内存/重启
pm2 logs api --err --lines 200  # 2) 错误日志
# 3) 单进程深挖：指定 worker 开 inspector
clinic doctor -- node dist/server.js    # 本地复现
# 4) 生产采样：--inspect 临时开启 → Chrome DevTools / heap snapshot 对比
# 5) worker 级指标拆分：log 里带 process.env.pm_id（PM2 注入的实例 id）
```
