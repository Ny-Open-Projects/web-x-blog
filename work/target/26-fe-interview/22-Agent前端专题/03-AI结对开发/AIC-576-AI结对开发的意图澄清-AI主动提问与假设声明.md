---
title: [AIC-576] AI 主动提问与假设声明
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-576：AI 主动提问与假设声明

**答**:
- AI 的"假设声明"机制：1) **模糊意图 → AI 做假设**（"帮我写个缓存" → AI 假设：LRU、内存缓存、100 条上限——这些假设可能不是用户想要的）；2) **假设声明 vs 静默假设**：好的 AI 会声明假设（"我假设你想要 LRU 内存缓存，上限 100 条，如需其他策略请说明"）；差的 AI 静默假设（不声明——用户不知道 AI 做了什么假设 → 验收时发现假设错误 → 重做）；3) **主动提问**：更好的 AI 会提问（"你需要什么缓存策略？LRU/LFU/FIFO？容量限制？"——问比猜好 RBL-506 意图精确性的 AI 侧反转）。
- 假设声明的工程价值：1) **减少迭代**（假设声明 → 用户确认/修正 → 一次到位；静默假设 → 用户发现错误 → 重新 prompt → 多轮迭代 RBL-509；2) **假设的文档化**：AI 的假设记录在代码注释中（"// ASSUMPTION: Using LRU cache with 100 entries limit"——验收时可审计 RBL-532 检查点）。
- 追问钩子：为什么「AI 的假设声明」能减少意图漂移（RBL-538）？——静默假设 = AI 的假设不在人的意识中（人验收时才发现假设错误——发现越晚修正成本越高）；声明假设 = 人立即看到 AI 的假设（确认或修正——在生成前校准意图）；「假设声明 = 意图的早期对齐」：生成前对齐意图 > 生成后发现偏差 > 生成后修正——假设声明把对齐点从"验收时"提前到"生成前"。

```typescript
// AI 的假设声明协议
interface AIAssumption {
  assumption: string;
  alternative: string;
  impact: string;
}
interface AIResponse {
  code?: string;
  assumptions: AIAssumption[];    // 声明的假设
  questions?: string[];            // 主动提问
}
// AI 输出示例
const aiResponse: AIResponse = {
  code: '// ASSUMPTION: LRU cache, 100 entries, in-memory\n' +
        'class Cache { /* LRU implementation */ }',
  assumptions: [
    { assumption: 'LRU eviction policy', alternative: 'LFU/FIFO/TTL',
      impact: '影响缓存命中率' },
    { assumption: '100 entries max', alternative: 'Unlimited/1000',
      impact: '影响内存占用' },
    { assumption: 'In-memory only', alternative: 'Redis/disk-backed',
      impact: '影响持久化' },
  ],
  questions: ['需要持久化吗？', '预计的缓存条目数？'],
};
```
