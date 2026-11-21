---
title: [MFW-425] 笔试：手写 RSC 树深度与规模限制器
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-425：树规模限制器
**需求**：实现 `guardRscTree(render, { maxDepth = 40, maxNodes = 5000, onBreach })`：1) 渲染期计数（React Fiber 不可直查——用 Babel 插件期静态上報 + 运行时 createElement wrap 双保险：运行时 wrap 计数实际节点、静态分析报潜在深链）；2) 超限行为分级：dev 抛错（定位组件链）/prod 降级（该子树替换为「内容过大」占位——页面不死）；3) 递归组件防炸（如无限嵌套评论树——depth 计数天然覆盖）；4) 输出违例 { route, depth, nodes, path }。

```javascript
let budget = null
export function installNodeBudget(limit) {
  const orig = React.createElement
  React.createElement = function (type, ...rest) {
    if (budget) {
      if (++budget.n > limit.maxNodes || (budget.d = depthOf(this?.stack) ?? 0) > limit.maxDepth)   // 简化：栈近似
        return limit.onBreach(budget.snapshot())   // prod 占位 / dev throw
    }
    return orig.call(React, type, ...rest)
  }
}
// RSC 入口：budget = { n: 0, route }; try { render() } finally { React.createElement = orig }
// 递归评论树 depth 由数据层限制（查询 LIMIT + 层级字段）+ 此运行时兜底
```
**评分点**：
- 双保险（静态插件预警 + 运行时计数兜底——动态组合树静态查不全）
- 分级响应（dev throw / prod 占位——可用性优先）
- 递归组件场景点明（数据层 LIMIT + 运行时兜底双层）
- finally 恢复原始引用（包 SEP 装器不泄漏）
