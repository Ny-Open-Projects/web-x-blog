---
title: [R19-347] 笔试：手写仪表盘的多 Suspense 编排（关键/次要数据分层）
date: 2026-11-19
categories: [React19]
tags: [前端面试, 笔试题, 07]
type: 笔试题
---

## R19-347：笔试：手写仪表盘的多 Suspense 编排
**答**：仪表盘数据：核心指标（必须快，阻塞渲染）、图表（独立边界）、消息流（独立边界可失败）。实现 Dashboard 布局：核心数据 RSC 直接 await；图表/消息流各自 Suspense + ErrorBoundary；消息流失败显示重试按钮不影响其他区域。

```javascript
// Dashboard.server.js
export default async function Dashboard() {
  const kpi = await getKpiData() // 核心数据：阻塞渲染（页面骨架期）
  return (
    <div className="grid">
      <KpiCards data={kpi} />
      <Suspense fallback={<ChartSkeleton />}>
        <ErrorBoundary fallback={ChartError}>
          <Charts />   {/* 内部自行 await getCharts() */}
        </ErrorBoundary>
      </Suspense>
      <Suspense fallback={<FeedSkeleton />}>
        <ErrorBoundary fallback={({ retry }) => <button onClick={retry}>重试消息流</button>}>
          <MessageFeed />
        </ErrorBoundary>
      </Suspense>
    </div>
  )
}
```
**评分点**：
- 核心数据 await 阻塞 vs 次要数据 Suspense 并行的分层决策。
- 图表/消息流独立边界（互不阻塞）。
- ErrorBoundary 与 Suspense 成对出现（等待 + 失败两个态）。
- 重试入口在错误 fallback 内。
