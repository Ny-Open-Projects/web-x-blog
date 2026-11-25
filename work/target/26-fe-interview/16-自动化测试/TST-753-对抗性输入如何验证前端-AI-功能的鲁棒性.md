---
title: [TST-753] 对抗性输入如何验证前端 AI 功能的鲁棒性
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 面试题, TST]
type: 面试题
---

## TST-753：对抗性输入如何验证前端 AI 功能的鲁棒性

**答**：
- 结论：对抗测试要覆盖「语义保持但扰动」的输入，验证输出稳定——同义改写、错别字、注入指令、极端长度。
- 前端场景特有：XSS 注入经过 AI 输出是否过滤、Prompt 注入是否能诱导绕过 UI 约束。
- 鲁棒性用「扰动前后输出一致性」度量，不一致率超阈值判失败。
- 追问钩子：对抗测试发现了模型漏洞，但短期无法换模型，前端能做什么缓解？

```javascript
// 对抗扰动：同义/大小写/空白扰动，检查输出稳定性
function perturb(text) {
  return [
    text,
    text.toUpperCase(),
    text.replace(/\s+/g, ' ').trim(),
    text.split('').reverse().join(''), // 极端扰动
  ];
}
function stability(fn, text) {
  const outputs = perturb(text).map(fn);
  const consistent = outputs.every(o => o === outputs[0]);
  return { consistent, variants: outputs.length };
}
console.log(stability(s => (s.toLowerCase().includes('refund') ? '退款' : '其他'), 'Can I get a REFUND?'));
```
