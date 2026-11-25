---
title: [AIC-032] temperature 等采样参数对编码任务有什么影响？哪些任务该调 0，哪些不适合？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-032：temperature 等采样参数对编码任务有什么影响？哪些任务该调 0，哪些不适合？
**答**：
- temperature 控制采样随机性：越低越确定、越可复现；编码任务的主体（bugfix、重构、格式转换、结构化输出）都应设 0~0.2，追求「同一输入同一输出」。
- 高随机适合的场景：命名头脑风暴、创意方案发散、测试用例的边界枚举——这些任务「多样性」本身有价值，可设 0.7~1.0。
- top_p 与 temperature 二选一调即可，同时调大两个会导致输出漂移失控；工程上固定 temperature=0 + top_p=1 最省心。
- CI/自动化里必须用 0：评审机器人、单测生成、批量迁移如果结果不可复现，回归对比就失去意义。
- 追问钩子：调 0 不是完全确定——服务端 batching、模型版本更新仍会漂移，关键产出要落盘成快照做回归。

```javascript
// 按任务类型选择采样参数（统一封装避免散落魔法数）
const SAMPLING = {
  bugfix:      { temperature: 0 },
  refactor:    { temperature: 0 },
  jsonOutput:  { temperature: 0, response_format: { type: 'json_object' } },
  unitTest:    { temperature: 0.2 },
  naming:      { temperature: 0.8, n: 5 },   // 多候选命名
  brainstorm:  { temperature: 1.0 },
};
function sampleParams(kind) {
  const p = SAMPLING[kind];
  if (!p) throw new Error(`unknown sampling kind: ${kind}`); // 禁止裸调 LLM
  return p;
}
```
