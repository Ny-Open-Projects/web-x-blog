---
title: [AIC-710] 结对开发中如何让 AI 建议变成可撤销的安全变更
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-710：结对开发中如何让 AI 建议变成可撤销的安全变更

**答**：
- 结论先行：可撤销性 = 每个 AI 变更都能「一句话回滚」且不引入二次损害；实现手段是「快照 + 事务式应用 + 变更清单」，让采纳 AI 建议像 git revert 一样安全。
- 三个要件：1) 应用前对受影响文件做快照；2) 把 AI 的多文件改动作为一个事务（要么全成要么全退）；3) 生成变更清单（改了哪些文件、哪些行），供回滚时精确定位。
- 反常识：不要只在内存里「撤销」——真正的安全来自版本控制里的可追溯提交，出问题时能跨会话回滚。
- 追问钩子：为什么「AI 自动 fix 循环」必须带回滚阈值？——连续自动修复可能越修越偏，超过阈值应停止并回退到最近稳定快照。

```javascript
// 事务式应用 AI 变更：失败整体回滚
function applyWithRollback(files, changeFn, snapshotFn) {
  const backup = snapshotFn(files);          // 应用前快照
  try {
    const next = changeFn(files);
    if (!validate(next)) throw new Error('invalid');
    return next;                             // 全成
  } catch (e) {
    return backup;                           // 全退
  }
}
function validate(f) { return f.every(x => x != null); }
const files = ['a.ts', 'b.ts'];
console.log(applyWithRollback(files, f => [...f, 'c.ts'], f => [...f])); // 3 文件
console.log(applyWithRollback(files, () => [null], f => [...f]));       // 回滚为 2 文件
```
