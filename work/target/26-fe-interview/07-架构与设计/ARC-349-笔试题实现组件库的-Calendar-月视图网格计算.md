---
title: [ARC-349] 笔试题：实现组件库的 Calendar 月视图网格计算？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-349：笔试题：实现组件库的 Calendar 月视图网格计算？
**题目**：实现月视图网格：1) 计算某月 42 格（6 行×7 列）日期（含前后月补位）；2) weekStart 可配置（0 周日/1 周一）；3) 今天/选中/范围内样式计算；4) 上/下月切换跨年正确。
**评分点**：
- 网格计算正确（首日周偏移 + 前补位 + 后补齐到 42）。
- weekStart 处理正确（偏移换算 (d - weekStart + 7) % 7）。
- 跨月/跨年日期计算用 Date 自动进位（ setDate(0) 陷阱意识）。
- 样式判定纯函数。
```tsx
function monthGrid(year: number, month: number, weekStart = 1) {     // month: 0-11
  const first = new Date(year, month, 1);
  const offset = (first.getDay() - weekStart + 7) % 7;               // 2) 周起始偏移
  const start = new Date(year, month, 1 - offset);
  return Array.from({ length: 42 }, (_, i) => {                      // 1) 42 格补位
    const d = new Date(start); d.setDate(start.getDate() + i);       // Date 自动跨月进位
    return d;
  });
}
function Calendar({ value, weekStart, month, onChange, onPrev, onNext }) {
  const cells = useMemo(() => monthGrid(month.year, month.month, weekStart), [month, weekStart]);
  const same = (a: Date, b?: Date) => b && a.toDateString() === b.toDateString();
  return <div className="cal">
    <header>
      <button onClick={onPrev}>‹</button>
      <span>{month.year} 年 {month.month + 1} 月</span>
      <button onClick={onNext}>›</button>                             {/* 4) 跨年切换由 month 状态驱动 */}
    </header>
    <div className="grid">
      {['一','二','三','四','五','六','日'].slice(0).map(w => <span key={w} className="wk">{w}</span>)}
      {cells.map(d => (
        <span key={d.getTime()} className={[
          d.getMonth() !== month.month ? 'other' : '',                // 补位月置灰
          same(d, new Date()) ? 'today' : '',
          same(d, value) ? 'selected' : '',                           // 3) 状态样式
        ].join(' ')} onClick={() => onChange(d)}>{d.getDate()}</span>
      ))}
    </div>
  </div>;
}
```
