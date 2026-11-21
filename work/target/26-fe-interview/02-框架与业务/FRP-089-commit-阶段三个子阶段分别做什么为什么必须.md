---
title: [FRP-089] commit 阶段三个子阶段分别做什么？为什么必须拆成 beforeMutation / mutation / layout？
date: 2026-11-17
categories: [框架原理]
tags: [前端面试, 面试题, 13]
type: 面试题
---

## FRP-089：commit 阶段三个子阶段分别做什么？为什么必须拆成 beforeMutation / mutation / layout？

**答**：
- **beforeMutation**：变更前的最后准备——类组件 `getSnapshotBeforeUpdate` 在这里执行（拿到"DOM 改动前"的快照，如滚动位置，供 componentDidUpdate 第三参使用）；还有 useEffect 的 destroy 批量标记等。
- **mutation**：真正改 DOM——按 flags 执行 Placement（appendChild/insertBefore）、Update（commitWork 更新文本/属性）、Deletion（先 unmount 递归调用 componentWillUnmount/useEffect destroy，再移除 DOM）；函数组件 ref 置 null。
- **layout**：DOM 已更新、**paint 尚未发生**——类组件 componentDidMount/DidUpdate、函数组件 useLayoutEffect 执行、ref 赋值、passive effect（useEffect）被调度到 paint 后异步 flush。
- 拆分的原因：**时序契约**——getSnapshotBeforeUpdate 必须看到旧 DOM（mutation 前），useLayoutEffect 必须看到新 DOM 但不闪烁（mutation 后 paint 前），useEffect 必须不阻塞绘制（paint 后）。三个子阶段就是三个时间契约的实现载体。

```javascript
// 简化实现，帮助理解 commit 三子阶段的执行顺序与各契约
function commitRoot(effectList) {
  const log = [];
  // ===== 阶段 1：beforeMutation（改动前快照）=====
  effectList.filter((f) => f.isClass).forEach((f) => {
    log.push(`getSnapshotBeforeUpdate: scrollY = ${window.scrollY}`); // 读旧 DOM 快照
  });
  // ===== 阶段 2：mutation（真实 DOM 变更）=====
  effectList.forEach((f) => {
    if (f.flags === 'Placement') log.push(`mutation: appendChild ${f.tag}`);
    if (f.flags === 'Update') log.push(`mutation: commitUpdate ${f.tag}`);
    if (f.flags === 'Deletion') {
      log.push(`mutation: componentWillUnmount / passive destroy for ${f.tag}`);
      f.stateNode?.remove();
    }
  });
  // ===== 阶段 3：layout（paint 前同步执行）=====
  effectList.forEach((f) => {
    if (f.isClass) log.push(`componentDidMount/Update ${f.tag}`);
    if (f.layoutEffects) log.push(`useLayoutEffect ${f.tag}`);
    if (f.ref) log.push(`attach ref ${f.tag}`);
    if (f.passiveEffects) schedulePassive(f); // useEffect 排队到 paint 后
  });
  return log;
}
function schedulePassive(fiber) {
  Promise.resolve().then(() => console.log(`passive: useEffect ${fiber.tag} (after paint)`));
}

const effectList = [
  { tag: 'header', flags: 'Placement', layoutEffects: true, passiveEffects: true },
  { tag: 'List', flags: 'Update', isClass: true, passiveEffects: true },
];
commitRoot(effectList).forEach((l) => console.log(l));
Promise.resolve().then(() => console.log('=== paint ==='));
// 输出顺序：快照 -> DOM 变更 -> layout -> paint -> passive
```
