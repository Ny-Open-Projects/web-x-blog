---
title: [WCN-815] 大型组织落地 WC 的「技术布道（evangelism）」体系怎么搭？
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 面试题, WCN]
type: 面试题
---

## WCN-815：大型组织落地 WC 的「技术布道（evangelism）」体系怎么搭？

**答**：
- 结论先行：布道不是开会宣讲，而是「降低试用门槛 + 制造成功口碑 + 建立大使网络」——让业务方自己用起来并主动传播，比平台王婆卖瓜有效得多。
- 降低门槛：提供可复制的脚手架、开箱即用的 demo、5 分钟接入指南、沙盒环境；让「试一下」的成本接近零。
- 制造口碑：打造 2~3 个标杆案例并量化收益（省工时、提转化），用同行分享会而非平台自夸；内部文档站展示「谁在用、效果如何」。
- 大使网络：在每个 BU 招募「组件大使」，给予培训、早期体验、署名认可，让他们成为平台在各团队的触点与反馈源。
- 持续运营：办 Office Hour、答疑频道、定期 newsletter 同步路线图与新特性，让平台保持「存在感」。
- 追问钩子：面试官会问「布道和强推的边界在哪」——答：布道靠价值吸引、强推靠行政命令；健康做法是「先布道建立采用，再用轻量治理（红线门禁）兜底」，避免一上来就强推引发抵触。

```javascript
// 布道体系的三层杠杆：门槛 ↓、口碑 ↑、大使网络扩散
function evangelism({ tryCost, cases, ambassadors }) {
  const reach = ambassadors * 30;          // 每个大使约触达 30 人
  const adoptionPotential = (cases * 20 + reach) / (1 + tryCost);
  return { reach, adoptionPotential: Math.round(adoptionPotential), focus: tryCost > 3 ? '先降门槛' : '扩口碑与大使' };
}
console.log(evangelism({ tryCost: 1, cases: 3, ambassadors: 6 }));
```
