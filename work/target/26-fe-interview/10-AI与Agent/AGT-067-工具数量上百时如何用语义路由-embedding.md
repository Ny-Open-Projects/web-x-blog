---
title: [AGT-067] 工具数量上百时如何用语义路由（embedding 匹配）缩小候选集？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-067：工具数量上百时如何用语义路由（embedding 匹配）缩小候选集？
**答**：
- 工具全量塞给模型的代价：tools 定义吃掉大量 token，且候选越多选择准确率越低。
- 语义路由：离线把每个工具的「名称+描述+示例问题」向量化；运行时对用户请求向量化，取 top-k 候选工具，只把候选给模型。
- 类目优先两级路由更稳：先路由到大类（检索/写操作/通信），类内再精排。
- 必须有兜底：路由置信度低于阈值时回退全量工具列表，宁可贵一点也不能选错工具。

```typescript
// 工具语义路由：embedding 召回候选，再交给模型精选
class ToolRouter {
  private index: { name: string; vector: number[] }[] = [];

  async buildIndex(tools: { name: string; description: string; sampleQueries: string[] }[]) {
    this.index = await Promise.all(tools.map(async (t) => ({
      name: t.name,
      // 描述与示例问题一起编码，召回更准
      vector: await embed(`${t.name} ${t.description} ${t.sampleQueries.join(' ')}`),
    })));
  }

  async route(query: string, k = 8, threshold = 0.35): Promise<string[]> {
    const qv = await embed(query);
    const ranked = this.index
      .map(({ name, vector }) => ({ name, score: cosine(qv, vector) }))
      .sort((a, b) => b.score - a.score);
    const top = ranked.slice(0, k).filter((r) => r.score >= threshold);
    return top.length ? top.map((r) => r.name) : []; // 空数组 = 置信不足，调用方回退全量
  }
}

// 主循环接入：候选工具受限，token 省且选择更准
const candidates = await router.route(userInput);
const toolsForLLM = candidates.length
  ? allTools.filter((t) => candidates.includes(t.function.name))
  : allTools;
```
