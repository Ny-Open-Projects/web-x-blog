---
title: [AGT-419] 笔试题——实现 badcase 自动归因分类器（多信号分级归因）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-419：手写 badcase 归因：规则信号优先、LLM 分类兜底、人工抽检队列

**需求与边界**：
- 输入：badcase {trace, userFeedback, scores}；输出：归因 {category, confidence, needsHuman}。
- 边界要求：① 确定性信号优先（引用越界/超时/工具异常——程序可判不调 LLM）；② LLM 分类带类别定义与 few-shot；③ 低置信强制入人工队列；④ 类别枚举封闭（检索/工具/幻觉/格式/时效/其他）。

**答**：
```javascript
const CATEGORIES = ['retrieval','tool_error','hallucination',
  'format','stale','other'];
function ruleSignals(caseData) {
  if (caseData.trace.toolError) return { category: 'tool_error',
    confidence: 1, needsHuman: false };
  if (caseData.trace.citationInvalid) return { category: 'hallucination',
    confidence: 0.95, needsHuman: false };
  if (caseData.trace.timeout) return { category: 'tool_error',
    confidence: 0.9, needsHuman: false };
  if (caseData.trace.sources?.every(s => s.ts < STALE_MS))
    return { category: 'stale', confidence: 0.85, needsHuman: false };
  return null;                                    // 规则不定 → LLM
}
async function attribute(caseData, { llmJudge }) {
  const rule = ruleSignals(caseData);
  if (rule) return withQueue(rule);
  const r = await llmJudge({
    prompt: `归因到唯一类别：${CATEGORIES.join('/')}
      定义：retrieval=该召回未召回或召回不相关；
      tool_error=工具选择/传参/异常；hallucination=编造事实；
      format=输出结构违规；stale=信息过时；other=其他。
      输出 {category, confidence, reason}，附 few-shot 示例 ×3`,
    case: caseData });
  const result = { ...r,
    needsHuman: r.confidence < 0.7 || r.category === 'other' };
  return withQueue(result);
}
function withQueue(r) {
  return { ...r,
    queue: r.needsHuman ? 'human_review' : 'auto_fix' };
}
// 校验 category 在枚举内，越界归 other+人工。
```

**评分点**:
- 确定性信号（trace 硬证据）优先归因，LLM 仅兜底——省钱且稳定。
- LLM 分类带封闭枚举定义与 few-shot，输出越界有兜底（other+人工）。
- 低置信（<0.7）与 other 类强制进人工队列，不自动修复。
- 归因结果分流入 auto_fix / human_review 两条队列。
