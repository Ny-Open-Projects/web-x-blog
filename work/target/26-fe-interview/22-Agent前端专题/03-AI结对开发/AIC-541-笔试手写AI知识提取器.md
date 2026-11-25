---
title: [AIC-541] 笔试：手写 AI 知识提取器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-541：笔试：手写 AI 知识提取

**答**：实现 `extractKnowledge(interactions, { minOccurrences })`。interactions: `{ prompt, output, action, userId }[]`。规则：1) **prompt 模式提取**：normalize prompt（去变量/去空白 → 模式串），相同模式的 accepted ≥ minOccurrences → goodPattern；2) **拒绝模式**：rejected 的 prompt 分类（"模糊 prompt" / "超出能力" / "幻觉"）；3) **FAQ 候选**：goodPattern 的最佳 output（accepted 最多的）；4) 返回 `{ goodPatterns: Array<{ pattern, count, bestOutput }>, rejectPatterns: Record<type, count>, faqs: Array<{ q, a }> }`。边界：interactions 空（空知识库）；全部 rejected（无 goodPattern）；minOccurrences=1（任何 accepted 都算——过于宽松但允许测试）。

```javascript
function extractKnowledge(interactions = [], { minOccurrences = 3 } = {}) {
  // normalize: 去变量/去空白
  const normalize = (p) => p.replace(/\$\{[^}]+\}/g, '${VAR}').replace(/\s+/g, ' ').trim().slice(0, 100);
  // 1) prompt 模式分组
  const byPattern = new Map();
  for (const i of interactions) {
    const key = normalize(i.prompt);
    (byPattern.get(key) || byPattern.set(key, []).get(key)).push(i);
  }
  // 2) 高接受率模式
  const goodPatterns = [];
  for (const [pattern, items] of byPattern) {
    const accepted = items.filter(i => i.action === 'accepted');
    if (accepted.length >= minOccurrences) {
      const best = accepted.reduce((a, b) =>
        (b.output.length > a.output.length ? b : a));
      goodPatterns.push({ pattern, count: accepted.length, bestOutput: best.output });
    }
  }
  // 3) 拒绝分类
  const rejectPatterns = { vague: 0, capability: 0, hallucination: 0 };
  for (const i of interactions.filter(i => i.action === 'rejected')) {
    if (i.prompt.split(' ').length <= 3) rejectPatterns.vague++;
    else if (/架构|设计|性能/.test(i.prompt)) rejectPatterns.capability++;
    else rejectPatterns.hallucination++;
  }
  // 4) FAQ
  const faqs = goodPatterns.map(p => ({ q: p.pattern, a: p.bestOutput }));
  return { goodPatterns, rejectPatterns, faqs };
}

// 自测
const interactions = [
  { prompt: '写一个 ${name} hook', output: 'good hook', action: 'accepted', userId: 'u1' },
  { prompt: '写一个 ${name} hook', output: 'good hook 2', action: 'accepted', userId: 'u2' },
  { prompt: '写一个 ${name} hook', output: 'good hook 3', action: 'accepted', userId: 'u3' },
  { prompt: 'fix', output: 'unclear', action: 'rejected', userId: 'u1' },
  { prompt: '优化架构设计', output: 'generic', action: 'rejected', userId: 'u2' },
];
let r = extractKnowledge(interactions, { minOccurrences: 3 });
console.log(r.goodPatterns.length === 1);
console.log(r.goodPatterns[0].count === 3);
console.log(r.faqs.length === 1);
console.log(r.rejectPatterns.vague === 1);               // 'fix' = 3 词以内
console.log(r.rejectPatterns.capability === 1);         // '优化架构设计'

// minOccurrences 过滤
r = extractKnowledge(interactions, { minOccurrences: 5 });
console.log(r.goodPatterns.length === 0);               // 只 3 次 < 5

// 空
r = extractKnowledge([], {});
console.log(r.goodPatterns.length === 0 && r.faqs.length === 0);
```

**评分点**：
- prompt 模式 normalize（去变量 → 模式串——相同模板的归并）；Rule of three
- 拒绝分类三型（vague/capability/hallucination——不同原因不同治理）；FAQ 自动生成
- 边界（空/全 rejected/minOccurrences 过滤）；bestOutput 的选择（最长的 accepted）
- 能说清「AI 交互日志是知识库的数据源：Rule of three 触发自动沉淀——高频 prompt = 团队的 AI 使用模式」属于加分
