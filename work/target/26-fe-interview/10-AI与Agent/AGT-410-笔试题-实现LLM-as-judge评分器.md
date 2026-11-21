---
title: [AGT-410] 笔试题——实现 LLM-as-judge 评分器（防位置/长度偏差）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-410：手写 judge 评分器：rubric 结构化、交换顺序去偏差、双人投票

**需求与边界**：
- 输入：样本 {query, output, baseline}、rubric（维度+分值+锚定示例）；输出：各维度分数+胜出判定。
- 边界要求：① A/B 交换顺序各评一次取均值（去位置偏差）；② rubric 含长度惩罚项（去长度偏差）；③ 两个异源 judge 取中位；④ 输出含分数依据（不可只给分）。

**答**：
```javascript
async function judge({ query, output, baseline, rubric, judges }) {
  async function oneJudge(J, a, b, posA) {
    const r = await J({ prompt: `按 rubric 逐维度打分(1-5)并给依据。
      rubric: ${JSON.stringify(rubric)}
      注意：答案长度不作为加分项（rubric 已含简洁维度）。
      问题: ${query}\n答案A: ${a}\n答案B: ${b}`,
      temp: 0 });
    // 校验输出格式与依据存在
    const parsed = parseScores(r);
    if (!parsed.every(s => s.reason)) throw new Error('缺少依据');
    return parsed;
  }
  // 交换顺序评两次
  const [ab, ba] = await Promise.all([
    oneJudge(judges[0], output, baseline, true),
    oneJudge(judges[0], baseline, output, false)]);
  const first = swapMerge(ab, ba);                 // 位置均值
  const second = await oneJudge(judges[1], output, baseline, true); // 异源
  // 双 judge 中位
  const dims = rubric.map(d => d.name);
  const final = Object.fromEntries(dims.map(dim => {
    const a = first[dim], b = second[dim];
    return [dim, (a + b) / 2];
  }));
  const win = Object.values(final).reduce((s, x) => s + x, 0) / dims.length;
  return { scores: final, win: win > 3 ? 'output' : 'baseline',
    audit: { swapped: true, judges: judges.length } };
}
// rubric 示例：[{name:'事实性',desc:'...'},{name:'简洁性',
//   desc:'冗长扣分：超过需求篇幅酌情-1'}]
```

**评分点**:
- 交换顺序双评+合并去位置偏差；rubric 显式含长度惩罚去长度偏差。
- 双异源 judge 取均值/中位，judge 输出强制带依据（缺依据报错）。
- rubric 结构化（维度+锚定），分数可按维度归因。
- 温度 0 与输出格式校验，工程化意识完整。
