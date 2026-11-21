---
title: [AGT-066] Agent 记忆系统的三层结构（短期窗口 + 长期向量库 + 摘要压缩）如何实现？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-066：Agent 记忆系统的三层结构（短期窗口 + 长期向量库 + 摘要压缩）如何实现？
**答**：
- 三层分工：短期 = 最近对话原文窗口（受 token 限制）；中期 = 滚动摘要（把旧轮次压缩成摘要保留在上下文）；长期 = 向量库（跨会话事实与偏好，按需检索注入）。
- 写入策略：不是每句话都进长期记忆——由模型抽取「值得记住的事实」（偏好、项目背景），去重后入库并带时间戳。
- 压缩时机：窗口将满时触发，摘要做更新式合并（新摘要包含旧摘要要点），保留最近 N 轮原文。
- 读取策略：每次请求检索 top-k 相关记忆 + 永久偏好直接注入 system。

```typescript
import { z } from 'zod';

// 三层记忆系统
class AgentMemory {
  private summary = '';                   // 中期层：滚动摘要
  private turns: ChatMessage[] = [];      // 短期层：最近原文轮次
  private static MAX_TURNS_TOKENS = 2000;

  constructor(private vectorStore: VectorStoreLike, private llm: typeof chatOnce) {}

  async addUserTurn(content: string) {
    this.turns.push({ role: 'user', content });
    await this.maybeCompress();
    await this.extractFacts(content);      // 异步抽取长期记忆
  }

  private async maybeCompress() {
    if (countTokens(this.turns.map((t) => t.content).join('')) <= AgentMemory.MAX_TURNS_TOKENS) return;
    const old = this.turns.slice(0, this.turns.length - 6);      // 压缩旧轮次，保留最近 3 轮原文
    this.summary = await this.llm([
      { role: 'user', content: `把以下对话压缩成要点摘要，与已有摘要合并：\n旧摘要：${this.summary}\n对话：${JSON.stringify(old)}` },
    ]);
    this.turns = this.turns.slice(-6);
  }

  private async extractFacts(content: string) {
    const facts = await structuredLLM(
      [{ role: 'user', content: `从这句话中提取值得长期记住的用户事实与偏好，没有则输出空数组：${content}` }],
      z.array(z.string()),
    );
    for (const f of facts) {
      await this.vectorStore.upsert({ text: f, vector: await embed(f), ts: Date.now() });
    }
  }

  async buildContext(query: string): Promise<ChatMessage[]> {
    const related = await this.vectorStore.search(await embed(query), 5); // 长期层按需注入
    const msgs: ChatMessage[] = [];
    if (this.summary) msgs.push({ role: 'system', content: `此前对话摘要：${this.summary}` });
    if (related.length) msgs.push({ role: 'system', content: `相关长期记忆：\n${related.map((r) => `- ${r.text}`).join('\n')}` });
    msgs.push(...this.turns);
    return msgs;
  }
}
```
