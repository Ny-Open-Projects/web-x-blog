---
title: [PER-248] 大促页面上线前，Web Vitals 验收清单应该包含哪些项？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-248：大促页面上线前，Web Vitals 验收清单应该包含哪些项？

**答**：
- 实验室验收（可复现）：Lighthouse CI 固定环境跑 LCP/CLS/TBT，预算卡口（LCP < 2.5s、CLS < 0.1、TBT < 200ms、JS 体积 < 预算）；DevTools 性能面板人工过一遍首屏时间轴确认无意外长任务。
- 真实验收（灰度）：小流量灰度开 RUM 采样，观察 24h p75 LCP/INP/CLS 与错误率；对比基线版本的同口径数据；INP 需要真实交互才能测，灰度期是唯一机会。
- 专项检查：首屏图片 fetchpriority 与尺寸声明；三方脚本清单收敛（禁新增同步脚本）；字体度量对齐；bfcache 适配（pageshow persisted 重置）；弱网（Slow 3G）与低端机模拟过一遍可交互路径。
- 回滚预案：RUM 指标恶化超阈值自动告警到值班群，并预设功能开关（性能开关：降级图片、关闭重三方）。

```text
上线验收 checklist（每项可勾选、有负责人）：
[ ] LH CI 卡口全绿（LCP/CLS/TBT/体积预算）
[ ] 性能面板首屏无 >200ms 长任务、无强制同步布局爆发
[ ] 灰度 24h：p75 LCP/INP/CLS 均不劣于基线版 5%
[ ] 首屏图 fetchpriority=high 且有 width/height
[ ] 三方脚本：全部异步/idle 触发，无新增同步 script
[ ] bfcache：pageshow persisted 路径手测通过
[ ] 弱网 + 4x CPU 模拟：核心路径可交互 < 5s
[ ] 回滚开关演练：性能降级开关生效验证
```
