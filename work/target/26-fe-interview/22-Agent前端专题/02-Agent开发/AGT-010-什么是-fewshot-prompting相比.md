---
title: [AGT-010] 什么是 few-shot prompting？相比 zero-shot 什么时候必须用？
date: 2026-11-17
categories: [Agent开发]
tags: [前端面试, 面试题, 14]
type: 面试题
---

## AGT-010：什么是 few-shot prompting？相比 zero-shot 什么时候必须用？
**答**：
- few-shot 是在上下文里放几组「输入 -> 期望输出」示例对，让模型模仿格式与判断标准。
- zero-shot 靠描述就能做的任务（翻译、总结）不必加示例；输出格式精细、分类边界模糊、领域黑话多的任务 few-shot 明显更稳。
- 示例要覆盖边界情况（易混淆的类目），且与真实输入分布一致。
- 代价是示例占 token，每轮请求都会重复计费；示例多时可考虑缓存前缀。

```typescript
// few-shot：用示例对压住分类标准，示例覆盖了最易混淆的边界情况
const FEW_SHOT: ChatMessage[] = [
  { role: 'system', content: '将用户输入分类为 bug、feature 或 question，只输出英文单词。' },
  { role: 'user', content: '列表滚动到底部偶尔白屏' },
  { role: 'assistant', content: 'bug' },
  { role: 'user', content: '希望支持导出 Excel' },
  { role: 'assistant', content: 'feature' },
  { role: 'user', content: 'useEffect 的第二个参数是什么意思' },
  { role: 'assistant', content: 'question' },
  { role: 'user', content: '希望导出功能能跑，现在一点就报错' }, // 边界：既是 feature 又含 bug
  { role: 'assistant', content: 'bug' },
];

async function classify(input: string): Promise<string> {
  const data = await fetchCompletion([...FEW_SHOT, { role: 'user', content: input }]);
  return data.choices[0].message.content.trim();
}
```
