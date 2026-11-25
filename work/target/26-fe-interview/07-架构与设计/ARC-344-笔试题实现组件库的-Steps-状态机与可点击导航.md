---
title: [ARC-344] 笔试题：实现组件库的 Steps 状态机与可点击导航？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 笔试题, 17]
type: 笔试题
---

## ARC-344：笔试题：实现组件库的 Steps 状态机与可点击导航？
**答**：实现 Steps：1) 状态推导（done/current/wait 按 currentIndex 计算）；2) 可点击导航（点击已完成步骤回跳，点击未到步骤禁止——除非 allowClickAll）；3) 垂直/水平布局与连接线；4) 错误步骤状态（current 显示 error 图标）。
**评分点**：
- 状态推导纯函数正确（i < cur → done，= cur → current，> cur → wait）。
- 点击权限逻辑正确（只允许回跳已完成的）。
- status 覆盖逻辑（error 优先于 current 展示）。
- aria 属性（aria-current="step"）。
```tsx
function Steps({ steps, current, status, onChange, allowClickAll = false, direction = 'horizontal' }) {
  const stateOf = (i: number) => {                       // 1) 纯函数推导
    if (status === 'error' && i === current) return 'error';   // 3) error 覆盖
    return i < current ? 'done' : i === current ? 'current' : 'wait';
  };
  const clickable = (i: number) => allowClickAll || i < current;  // 2) 只能回跳
  return (
    <ol className={`steps steps-${direction}`}>
      {steps.map((s, i) => (
        <li key={i} className={`step step-${stateOf(i)}`}
          aria-current={i === current ? 'step' : undefined}
          onClick={() => clickable(i) && onChange?.(i)}>
          <span className="dot">{stateOf(i) === 'done' ? '✓' : i + 1}</span>
          <span className="label">{s.title}</span>
        </li>
      ))}
    </ol>
  );
}
// 连接线：CSS .step::after { content:''; border-top: 1px solid; } + done 态变色，垂直方向旋转 90°
```
