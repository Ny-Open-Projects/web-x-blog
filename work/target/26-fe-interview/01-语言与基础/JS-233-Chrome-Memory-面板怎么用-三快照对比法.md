---
title: [JS-233] Chrome Memory 面板怎么用：三快照对比法
date: 2026-11-19
categories: [JavaScript]
tags: [前端面试, 面试题, 排查SOP]
type: 面试题
---

## JS-233：Chrome Memory 面板：三快照对比法

**答**：
- 步骤：① 操作前拍快照 ② 执行可疑操作 N 次（如打开/关闭弹窗 10 次）③ 再拍快照 ④ 用 Comparison 视图对比
- 对比维度：按「Delta」排序找新增最多的 Constructor；重点关注数组/字符串/自定义类/Detached 节点
- Retainers 视图：点中可疑对象看「谁在引用它」——从引用链定位泄漏源（定时器/全局数组/闭包）
- 关键技巧：强制 GC（垃圾桶按钮）后再拍第二张，排除「还没来得及回收」的干扰
- 常见结论模板：某数组每操作一次 +N 元素 → 找 push 它的代码路径

```text
Memory 面板操作路径：
Heap snapshot → Snapshot 1 → 执行操作 → Snapshot 2 →
选 Snapshot 2 → 下拉切 Comparison → 与 Snapshot 1 对比 →
按 Delta 降序 → 点开对象 → Retainers 面板看引用链
```
