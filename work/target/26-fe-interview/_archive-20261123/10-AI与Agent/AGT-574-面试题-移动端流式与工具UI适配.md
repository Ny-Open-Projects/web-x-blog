---
title: [AGT-574] 移动端看 Agent 时间线/双栏对比这类复杂 UI，怎么适配？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 面试题, Agent]
type: 面试题
---

## AGT-574：移动端看 Agent 时间线/双栏对比这类复杂 UI，怎么适配

**答**：
- 信息密度降维：时间线在移动端折叠为单行摘要（"3 步完成 · 查看了 2 个文档"），展开才见全量；双栏对比改上下堆叠或 Tab 切换。
- 触控优先：展开/收起用整行点击区域（≥44px），批注浮层避开软键盘区；横向表格卡片化（列变行）而不是横向滚动长表。
- 性能兜底：低端移动机关闭打字机动效（直接文本更新），减少重排。

```javascript
const isMobile = matchMedia('(max-width: 640px)').matches;
function adapt(ans) {
  return {
    timeline: isMobile ? <TimelineSummary turns={ans.turns} /> : <Timeline turns={ans.turns} />,
    compare: isMobile ? <StackedCompare {...ans.dual} /> : <SideBySide {...ans.dual} />,
    typewriter: deviceTier === 'low' ? instant : animated,
    table: isMobile ? cardify : virtualTable,   // 横表竖排
  };
}
```

