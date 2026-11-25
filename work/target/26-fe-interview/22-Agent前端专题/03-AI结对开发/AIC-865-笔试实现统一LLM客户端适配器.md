---
title: [AIC-865] 笔试：实现统一 LLM 客户端（多供应商 fallback + 重试）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-865：笔试：实现统一 LLM 客户端（多供应商 fallback + 重试 + 超限保护）
**答**：
- 核心需求：实现 `LLMClient`，构造时接收 `providers: { name, call, weight }[]`。`chat(prompt)` 按权重优先顺序尝试：每个供应商最多重试 `maxRetries` 次（指数退避），仍失败则切下一个；全部失败抛聚合错误。成功时返回 `{ text, provider, attempts }`。
- 边界：`providers` 为空抛错；weight 为 0 的供应商跳过；`call` 抛错视为失败；重试次数用尽后立即切换不做额外等待；聚合错误要列出每个供应商的失败原因。
- 退避：`baseDelay * 2 ** retry` 加上随机抖动（避免同步重试风暴，呼应 AIC-805）；测试用例中可通过注入 sleep 函数避免真实等待。
- 追问钩子：追问「fallback 到不同供应商，答案风格不一致怎么办」——能答出「这在平台层是通过能力声明 + 评测保证各供应商在该任务上达标，而不是要求输出完全一致」的候选人理解了统一的边界。

```typescript
type Provider = { name: string; call: (p: string) => Promise<string>;
  weight?: number };

class LLMClient {
  constructor(private providers: Provider[], private maxRetries = 2,
              private sleep: (ms: number) => Promise<void> = ms => new Promise(r => setTimeout(r, ms))) {
    if (!providers?.length) throw new Error('no providers');
  }
  async chat(prompt: string) {
    const ordered = [...this.providers].filter(p => (p.weight ?? 1) > 0)
      .sort((a, b) => (b.weight ?? 1) - (a.weight ?? 1));
    const errors: string[] = [];
    let attempts = 0;
    for (const p of ordered) {
      for (let r = 0; r <= this.maxRetries; r++) {
        attempts++;
        try {
          const text = await p.call(prompt);
          return { text, provider: p.name, attempts };
        } catch (e) {
          errors.push(`${p.name}#${r}: ${(e as Error).message}`);
          if (r < this.maxRetries) {
            const backoff = 100 * 2 ** r;
            await this.sleep(backoff + Math.random() * backoff); // 退避 + 抖动
          }
        }
      }
    }
    throw new Error('all providers failed: ' + errors.join(' | '));
  }
}
// 测试：注入立即返回的 sleep，避免真实等待
const client = new LLMClient([
  { name: 'A', call: async () => { throw new Error('down'); }, weight: 10 },
  { name: 'B', call: async (p: string) => 'ok:' + p, weight: 5 },
], 1, async () => {});
console.log(await client.chat('hi')); // { text:'ok:hi', provider:'B', attempts:3 }
```
**评分点**：
- 按权重排序，weight<=0 跳过；空 providers 抛错。
- 重试上限用 `r <= maxRetries`（含首次共 maxRetries+1 次），次数正确。
- 退避带随机抖动防重试风暴；sleep 可注入便于测试（可测性设计）。
- 聚合错误包含所有供应商与重试的失败原因，可排障。
- 返回 attempts 计数用于度量，体现可观测性。
