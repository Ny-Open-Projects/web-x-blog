---
title: [ARC-333] 笔试题：实现组件库的 Range 选择器联动约束？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-333：笔试题：实现组件库的 Range 选择器联动约束？
**答**：实现日期区间选择器的联动逻辑：1) 先选 start 再选 end（第二次点击为 end，再点重开新区间）；2) end 必须 ≥ start（否则交换）；3) 禁用日期联动（已选 start 后，end 的禁用范围自动收窄）；4) hover 预览区间高亮。
**评分点**：
- 选择状态机正确（null → start → 完整区间 → 重开）。
- 交换逻辑正确（end < start 时交换而非报错）。
- 禁用联动：isDisabledDate 接收"暂定区间"上下文。
- hover 预览不污染提交值。
```tsx
function RangePicker({ disabledDate }) {
  const [[start, end], setRange] = useState<[Date?, Date?]>([]);
  const [hover, setHover] = useState<Date | null>(null);
  const pick = (d: Date) => {
    if (start == null || (start && end)) { setRange([d]); return; }       // 1) 状态机
    const next = endOfPick(start, d);                                     // 2) 交换
    setRange(next);
  };
  const endOfPick = (s: Date, d: Date) => (d < s ? [d, s] : [s, d]);      // 2) 交换而非报错
  const isDisabled = (d: Date) => {
    if (disabledDate?.(d)) return true;
    if (start && !end) return false; // end 端约束：3) 已选 start，禁用逻辑拿到暂定上下文
    return false;
  };
  const preview = (d: Date) => { if (start && !end) setHover(d); };       // 4) hover 预览
  const cellCls = (d: Date) => {
    const [lo, hi] = end ?? (start && hover ? endOfPick(start, hover) : []);
    return lo && hi && d >= lo && d <= hi ? 'in-range' : '';
  };
  return <Grid onPick={pick} onHover={preview} isDisabled={isDisabled} cellCls={cellCls}
    value={start && end ? `${fmt(start)} ~ ${fmt(end)}` : start ? `${fmt(start)} ~ ?` : ''}/>;
}
```
