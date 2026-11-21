---
title: [DP-337] 笔试题：手写组件库 Story 参数化测试？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-337：笔试题：手写组件库 Story 参数化测试？
**题目**：实现 storyTest：1) 遍历组件 props 矩阵（type×size×disabled）生成用例；2) 每用例断言渲染类名与可访问性；3) 全组合与抽样模式（矩阵大时抽样防爆炸）；4) 失败输出组合标识。
**评分点**：
- 笛卡尔积生成正确。
- 抽样策略（均匀抽样保覆盖）。
- 断言基于契约（类名/aria）而非快照唯一。
- 失败信息含组合参数。
```tsx
function cartesian(...sets) {                              // 1) 笛卡尔积
  return sets.reduce((acc, set) => acc.flatMap(combo => set.map(v => [...combo, v])), [[]]);
}
function sampleN(cases, n = 20) {                          // 3) 均匀抽样
  const step = Math.ceil(cases.length / n);
  return cases.filter((_, i) => i % step === 0);
}
function storyTest(Comp, { matrix, full = false }) {
  const keys = Object.keys(matrix);
  const all = cartesian(...keys.map(k => matrix[k]))
    .map(combo => Object.fromEntries(keys.map((k, i) => [k, combo[i])));
  const cases = full ? all : sampleN(all, 20);
  test.each(cases.map(c => [JSON.stringify(c), c]))('%s renders', async (_, props) => {
    const { container } = render(<Comp {...props}/>);
    const el = container.firstChild;
    expect(el.className).toContain(`btn-${props.type ?? 'default'}`);
    expect(el.className).toContain(`btn-${props.size ?? 'md'}`);
    expect(await axe(container)).toHaveNoViolations();      // 2)
  });
}
// 失败输出：{ "type":"danger","size":"sm" } renders — 明确到组合（4）
```
