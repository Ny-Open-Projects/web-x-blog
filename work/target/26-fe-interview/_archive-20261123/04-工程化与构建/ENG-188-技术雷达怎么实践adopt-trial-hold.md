---
title: [ENG-188] 技术雷达怎么实践？adopt trial hold 怎么运转？
date: 2026-11-17
categories: [工程化]
tags: [前端面试, 面试题, 08]
type: 面试题
---

## ENG-188：技术雷达怎么实践？adopt trial hold 怎么运转？
**答**：
- 四象限（技术 平台 工具 语言框架）× 四环（adopt 主力 trial 试点 assess 观察 hold 收缩），半年一版全员评审。
- 关键动作是移动：新进 trial 要配试点报告；trial 升 adopt 需数据支撑；进 hold 的要有迁移指引。
- 雷达对齐资源：hold 环停止新项目引入，存量排迁移计划；trial 环给试点团队配 mentor。
- 组织意义：让用什么技术成为公开决策而非小圈子默契，跨团队协作有共同语言。

```json
// radar/2026-h2.json —— 技术雷达数据
{
  "edition": "2026-H2",
  "quadrants": ["techniques", "platforms", "tools", "languages-frameworks"],
  "rings": ["adopt", "trial", "assess", "hold"],
  "entries": [
    { "name": "pnpm workspace", "quadrant": "tools", "ring": "adopt", "since": "2024-H2" },
    { "name": "vite", "quadrant": "tools", "ring": "adopt", "since": "2025-H1" },
    { "name": "module-federation", "quadrant": "platforms", "ring": "trial", "note": "三个月试点报告后再评审" },
    { "name": "react-server-components", "quadrant": "languages-frameworks", "ring": "assess" },
    { "name": "moment.js", "quadrant": "languages-frameworks", "ring": "hold", "note": "停止新引入 存量迁移中" }
  ]
}
```
