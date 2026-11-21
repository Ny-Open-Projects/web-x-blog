---
title: [PER-247] 怎么用 CrUX 做竞品性能对标？对比时要注意哪些口径陷阱？
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-247：怎么用 CrUX 做竞品性能对标？对比时要注意哪些口径陷阱？

**答**：
- 对标姿势：对竞品 origin（或竞品核心 URL）拉 CrUX 同口径数据（p75、28 天、formFactor=PHONE），比自己与竞品在同一张表上的 CWV 达标情况；Search Console/PSI 界面同样可查竞品（无需对方授权，CrUX 是公开数据集）。
- 陷阱一：页面构成不同——竞品首页流量占比可能远高于你，origin 级数据不反映同模板对比；尽量选双方"功能对等"的具体 URL。
- 陷阱二：流量与设备结构不同——竞品用户 iOS/桌面占比高会天然好看；只比 formFactor=PHONE 的 Chrome 用户口径。
- 陷阱三：业务差异——竞品首屏图少/信息密度低，不是技术差距；对标结论要写清"同口径、同模板、同设备"三个前提，否则误导决策。
- 用途排序：定目标（超越竞品 p75）> 找差距（哪个指标差多少）> 定期追踪（季度对标报告）。

```javascript
// 竞品对标脚本核心：并发拉多家 origin，输出同口径对比表
async function benchmark(origins, apiKey) {
  const rows = await auditCrUX(origins, apiKey);      // 复用 PER-238 的巡检函数
  const base = rows.find(r => r.origin === 'https://www.mysite.com');
  return rows.map(r => ({
    origin: r.origin,
    lcpGap: +(r.largest_contentful_paint.p75 - base.largest_contentful_paint.p75),
    inpGap: +(r.interaction_to_next_paint.p75 - base.interaction_to_next_paint.p75),
    clsGap: +(r.cumulative_layout_shift.p75 - base.cumulative_layout_shift.p75),
  }));  // 正 gap = 竞品更慢；负 gap = 我方落后，进优化清单
}
```
