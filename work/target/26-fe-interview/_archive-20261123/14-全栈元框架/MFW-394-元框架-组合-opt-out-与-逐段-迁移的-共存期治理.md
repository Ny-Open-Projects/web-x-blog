---
title: [MFW-394→MFW-394] 逐段迁移共存期的双重语义治理
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-394：共存期治理

**答**:
- 场景：Pages Router 老路由与新 App Router 共存（官方支持但语义两套：数据获取/缓存/特殊文件全不同）——共存期是「规则双色球」，评审与事故归因都要分桶
- 治理三件：①路由归属清单（每个路由标注 renderer: pages|app——蓝图字段，build 输出核对）②共享层最小化（两栈只共享：鉴权工具/设计 token/DTO——数据层与缓存层各玩各的，禁止跨栈 import 私有件）③迁移看板（周迁 N 条 + 汇合点预估——共存期有.endDate 而非永久）
- 高危交叉点：同 URL 两栈历史版本冲突（CDN 缓存键、SEO 收录——迁移时 301 表 + purge 联动 MFW-368）；全局 CSS/Provider 重复注入（双 ReactDOM root 边界——layout 层级审慎设计）
- 退出标准：app 占比 > 95% 且 30 天无 pages 回归 bug → 删 pages 目录（共存期 deadline 写进 OKR）

```text
三件：路由归属蓝图字段 / 共享层白名单（鉴权·token·DTO） / 迁移看板带 endDate
高危：同 URL 双栈缓存键与 SEO / 双 Provider 注入
退出：>95% 且 30 天净 → 删旧栈
```
