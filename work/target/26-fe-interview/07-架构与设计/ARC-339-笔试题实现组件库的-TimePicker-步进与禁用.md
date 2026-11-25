---
title: [ARC-339] 笔试题：实现组件库的 TimePicker 步进与禁用？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-339：笔试题：实现组件库的 TimePicker 步进与禁用？
**答**：实现时间选择器核心逻辑：1) 步进 minuteStep/hourStep 生成的可选列表；2) 禁用时段（disabledHours/disabledMinutes 函数）从列表剔除；3) 键盘上下键在"合法"时间序列间移动（跳过禁用）；4) 输入解析与合法校验（'9:5' → 09:05）。
**评分点**：
- 步进生成正确（0, 15, 30, 45），与禁用函数求交后非空校验。
- 键盘移动跳过禁用项且循环。
- 输入解析健壮（补零、范围校验、非法输入不提交）。
- 受控 value 与展示格式（HH:mm）一致。
```tsx
function TimePicker({ value = '09:00', onChange, hourStep = 1, minuteStep = 15,
                     disabledHours = () => [], disabledMinutes = () => [] }) {
  const parse = (s: string) => {
    const m = s.match(/^(\d{1,2}):(\d{1,2})$/);
    if (!m) return null;
    const [h, min] = [Math.min(+m[1], 23), Math.min(+m[2], 59)];
    return `${String(h).padStart(2, '0')}:${String(min).padStart(2, '0')}`;   // 4) 补零校验
  };
  const options = useMemo(() => {                                            // 1)+2)
    const dh = new Set(disabledHours());
    const out: string[] = [];
    for (let h = 0; h < 24; h += hourStep) {
      if (dh.has(h)) continue;
      const dm = new Set(disabledMinutes(h));
      for (let m = 0; m < 60; m += minuteStep) {
        if (dm.has(m)) continue;
        out.push(`${String(h).padStart(2, '0')}:${String(m).padStart(2, '0')}`);
      }
    }
    return out;                                                              // 为空则 UI 提示"无可选时段"
  }, [hourStep, minuteStep, disabledHours, disabledMinutes]);
  const step = (dir: 1 | -1) => {                                            // 3) 跳禁用（options 已剔除）
    const i = options.indexOf(parse(value)!);
    const next = options[(i + dir + options.length) % options.length];
    onChange(next);
  };
  return <Picker options={options} value={value} onStep={step} onSubmit={s => parse(s) && onChange(parse(s))}/>;
}
```
