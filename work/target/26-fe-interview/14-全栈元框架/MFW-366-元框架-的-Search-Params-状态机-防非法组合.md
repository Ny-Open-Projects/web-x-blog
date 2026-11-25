---
title: [MFW-366→MFW-366] searchParams 状态机（非法组合防御性归一）
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-366：searchParams 状态机

**答**:
- 问题：URL 可任意构造（RBL-358 信任边界）——组合非法（tab=chart&export=csv&deep=500 互相矛盾）直接进查询 = DoS 与语义混乱
- 状态机归一：合法状态集显式枚举（模式互斥表：view ∈ {list,chart}；export 仅 list 态合法）→ 解析函数「先判模式再取参」——非法组合归一到最近合法态（不是 500 是纠正）
- 纠错 UX：被丢弃的参数给一次性提示（「已忽略导出参数：图表视图不支持」——透明而非静默吞）；归一后的 URL replaceState 回写（书签分享得到合法形态）
- 测试：组合模糊测试（随机参数对 → 断言输出 ∈ 合法集——状态机正确性的自动验证）

```javascript
function normalizeFilters(search) {
  const s = parse(search)
  const mode = MODES.has(s.view) ? s.view : 'list'
  const cleaned = mode === 'chart' ? dropKeys(s, ['export', 'page']) : clampPage(s)  // 模式互斥裁剪
  if (dropped.length) toastOnce(`已忽略：${dropped}`)
  history.replaceState(normalizeUrl(cleaned))          // 书签合法化
  return typed(cleaned)                                // schema 出口
}
// 属性测试：randomPairs → out ∈ LEGAL_SET
```
