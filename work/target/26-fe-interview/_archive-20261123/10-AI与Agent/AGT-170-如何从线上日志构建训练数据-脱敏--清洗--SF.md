---
title: [AGT-170] 如何从线上日志构建训练数据（脱敏 → 清洗 → SFT 样本）？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-170：如何从线上日志构建训练数据（脱敏 → 清洗 → SFT 样本）？
**答**：
- 数据来源与配比：线上「好会话」（正反馈 + 任务完成）是天然 SFT 种子；人工补写覆盖长尾；模型合成增强（对种子做改写/扰动）要明确标记防止污染评测集。
- 脱敏是硬前置：PII 检测（正则 + NER 模型双引擎）→ 替换为格式一致的占位符（保数据分布：手机号换假手机号而不是换 [MASK]）→ 抽检管线（人抽 1% 验证漏检率 < 0.1%）→ 通过后才出受控数据区。
- 清洗与配对：会话切分为「上下文 → 理想回复」样本，过滤条件包括质量分（judge 打分阈值）、长度分布、去重（输入指纹相似度）；工具调用样本要严格保 tool_call/result 配对完整。
- 全流程可审计：每条样本记录来源会话 id、脱敏版本、清洗规则版本——出问题能定位是哪批数据引入的。

```typescript
// 线上日志 → SFT 数据管道：脱敏 + 清洗 + 配对
import { z } from 'zod';

const SftSample = z.object({
  messages: z.array(z.object({ role: z.enum(['system', 'user', 'assistant', 'tool']), content: z.string() })),
  sourceSessionId: z.string(), desensVersion: string0(), cleanRulesVersion: string0(),
});
function string0() { return z.string(); }
type SftSample = z.infer<typeof SftSample>;

const PII_PATTERNS: [RegExp, (m: string) => string][] = [
  [/1[3-9]\d{9}/g, () => fakePhone()],                                  // 手机号 → 格式一致假号
  [/\d{17}[\dXx]/g, () => '11010119900101001X'.replace(/\d(?=.{3})/g, '8')], // 身份证
  [/[\w.+-]+@[\w-]+\.[\w.]+/g, () => 'user@example.com'],
];

export function desensitize(text: string, seed: number): string {
  let out = text;
  for (const [p, replace] of PII_PATTERNS) out = out.replace(p, replace);
  return out;
}
function fakePhone() { return '138' + String(Math.floor(Math.random() * 1e8)).padStart(8, '0'); }

export async function buildSftDataset(sessions: RawSession[], judgeThreshold = 4.2): Promise<SftSample[]> {
  const samples: SftSample[] = [];
  for (const s of sessions) {
    const score = await judge(s);                                        // 质量门槛：只收好会话
    if (score < judgeThreshold || s.negativeFeedback) continue;
    const messages = s.messages.map((m) => ({ ...m, content: desensitize(m.content, s.id.length) }));
    const paired = validateToolPairs(messages);                          // 工具轮必须成对完整
    if (!paired) { metrics.inc('sft.drop.toolpair'); continue; }
    if (isDup(messages)) { metrics.inc('sft.drop.dup'); continue; }      // 输入指纹去重
    samples.push(SftSample.parse({ messages, sourceSessionId: s.id, desensVersion: 'v3', cleanRulesVersion: 'v5' }));
  }
  await humanSpotCheck(samples, 0.01);                                   // 1% 人工抽检验证漏检率
  return samples;
}
type RawSession = { id: string; messages: { role: any; content: string }[]; negativeFeedback?: boolean };
async function judge(s: RawSession) { void s; return 4.5; }
function validateToolPairs(msgs: any[]): boolean { return msgs.every((m, i) => m.role !== 'tool' || msgs[i - 1]?.role === 'assistant'); }
function isDup(msgs: any[]) { return false; }
async function humanSpotCheck(s: SftSample[], r: number) { void s; void r; }
const metrics = { inc: (n: string) => { void n; } };
```
