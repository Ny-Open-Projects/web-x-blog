---
title: [ZSM-295] 状态比较总是 false 的对象身份陷阱有哪些
date: 2026-11-20
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-295：状态比较总是 false 的对象身份陷阱有哪些

**答**:
- 四大陷阱：selector 里返回 `.filter()` 新数组（每次新引用）、默认参数 `{}`/`[]`（每次新对象）、useEffect 依赖里用内联对象、浅合并把嵌套对象整个替换导致下游全炸
- 解法对应：selector 配 shallow 比较、默认值提为模块常量、依赖改为原始值/JSON 字符串、嵌套更新用归一化或 immer
- 判断工具：React DevTools Profiler 看非必要重渲染、zustand 的 useShallow、React Compiler 自动 memo 化（未来减轻但不免除责任）
- 根因认知：引用相等是 React 订阅模型的基石，「产出引用的位置」就是性能的责任点

```javascript
// ❌ 每次 filter 新数组 → 浅比较失效 → 每次渲染
const done = useStore((s) => s.items.filter((i) => i.done))
// ✅ shallow
const done = useStore(useShallow((s) => s.items.filter((i) => i.done)))
// ✅ 或在 select 层缓存
const EMPTY = []
const done = useStore((s) => s.doneIds.length ? s.doneIds : EMPTY)
```
