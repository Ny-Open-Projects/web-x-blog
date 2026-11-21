---
title: [AIC-004] 为什么说 Agent 模式下「人的角色从写代码变成审代码」？审什么、怎么审才不是走过场？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-004：为什么说 Agent 模式下「人的角色从写代码变成审代码」？审什么、怎么审才不是走过场？
**答**：
- Agent 产出的单位是「一批 diff」而不是一行补全，产出速度超过人写，瓶颈从编码转移到验证，所以人变成 reviewer。
- 审查清单化，避免肉眼扫过：① diff 范围是否越界（改了任务外文件）；② 业务逻辑是否真的满足需求（AI 最擅长「看起来对」）；③ 边界与错误处理；④ 是否偷偷引入依赖/全局副作用；⑤ 测试是否真实覆盖（AI 常写「永远通过」的假测试）。
- 有效的审法：逐文件看 diff、对照需求列验收点、让测试先跑、关键逻辑手动推一遍或补断点。
- 用工具辅助：`git diff --stat` 先看范围，再按文件细审；CI 门口挂 lint + 测试兜底。
- 追问钩子：能说出「假测试」识别（断言里没有业务断言、mock 了被测逻辑本身）是加分项。

```bash
# Agent 任务结束后的标准审查动作
git diff --stat              # 第一步：范围审查，是否改了任务外文件
git diff src/services/cart.ts | head -80   # 第二步：核心逻辑细读
pnpm test --run              # 第三步：全量测试，防「只跑过新测试」
npx depcheck                 # 第四步：是否偷引依赖
```

```typescript
// 识别「假测试」：没有任何业务断言，怎么写都能过
it('should work', () => {
  const wrapper = mount(GoodsList); // 只断言「能挂载」
  expect(wrapper.exists()).toBe(true);
});

// 合格测试：断言业务行为
it('按价格升序排序', () => {
  const { sorted } = useSortedList(goods, 'price');
  expect(sorted.value.map(g => g.price)).toEqual([10, 20, 30]);
});
```
