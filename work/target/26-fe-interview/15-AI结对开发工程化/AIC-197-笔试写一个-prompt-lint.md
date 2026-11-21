---
title: [AIC-197] 笔试：实现一个 Prompt Lint：约束密度、正向指令改写建议、模糊措辞检测与长度预算？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-197：笔试：实现一个 Prompt Lint：约束密度、正向指令改写建议、模糊措辞检测与长度预算？
**需求**：实现 `lintPrompt(text)`：
- 约束密度：约束行（`-` 开头/「禁止」「必须」）超过 12 条警告「规则密度过高，中段约束易被忽略」；
- 负面指令检测：「不要 X」且未跟随正向替代时，给出改写建议（从改写表查）；
- 模糊措辞检测：「尽量」「适当」「好看」「优雅」等词 → 建议量化；
- 长度预算：超过 2000 token 警告裁剪；输出 `{issues: [{rule, line, msg, suggestion}]}`。

```javascript
const NEGATIVE_RE = /(不要|禁止|避免|别)\s*([^\n，。;；]{2,20})/;
const VAGUE = ['尽量', '适当', '好看', '优雅', '合理', '一些'];
const REWRITE = {
  '使用 css in js': '样式统一 Tailwind 原子类',
  '写 any': '标注精确类型，不确定用 unknown + 收窄',
};
function tokensOf(s) {
  const cjk = (s.match(/[\u4e00-\u9fa5]/g) || []).length;
  return Math.ceil(cjk / 1.5 + (s.length - cjk) / 4);
}

function lintPrompt(text) {
  const lines = text.split('\n');
  const issues = [];
  const isConstraint = (l) => /^\s*[-*]\s/.test(l) || /(禁止|必须|不要)/.test(l);
  const constraints = lines.map((l, i) => ({ l, i })).filter(x => isConstraint(x.l));

  if (constraints.length > 12) {
    issues.push({ rule: 'constraint-density', line: 0,
      msg: `约束 ${constraints.length} 条超阈值：中段约束容易被模型忽略`,
      suggestion: '按优先级裁剪到 12 条内，关键红线放首尾' });
  }
  for (const { l, i } of constraints) {
    const m = l.match(NEGATIVE_RE);
    if (m && !/统一|改用|代替|改为/.test(l)) {   // 负面无正向替代
      const key = Object.keys(REWRITE).find(k => m[2].includes(k.split(' ')[1] ?? k));
      issues.push({ rule: 'negative-only', line: i + 1, msg: `纯负面约束「${m[2]}」`,
        suggestion: REWRITE[key] ?? `改为正向表述：具体说明「应该怎么做」` });
    }
  }
  lines.forEach((l, i) => {
    const hit = VAGUE.find(v => l.includes(v));
    if (hit) issues.push({ rule: 'vague-word', line: i + 1,
      msg: `模糊措辞「${hit}」`, suggestion: '改为可判定标准（数值/示例/枚举）' });
  });
  const t = tokensOf(text);
  if (t > 2000) issues.push({ rule: 'length-budget', line: 0,
    msg: `约 ${t} tokens 超预算 2000`, suggestion: '裁剪示例与背景，长上下文走附件检索' });

  return { issues, tokens: t, ok: !issues.length };
}

// 测试
const p = `# 约束
- 不要使用 css in js
- 尽量让代码优雅
${'- 禁止方案A\n'.repeat(14)}`;
console.log(lintPrompt(p).issues.map(i => `${i.rule}@${i.line}`));
// negative-only / vague-word / constraint-density
```

**评分点**：
1. 约束密度阈值与「中段易忽略」的原理说明（注意力分布）；
2. 负面指令检测区分「有正向替代」（不要X→统一Y 合法）与「纯否定」；
3. 模糊词清单可扩展，建议必须可执行（改写表 vs 泛泛建议）；
4. 长度预算用中英文分估 token；
5. 追问：lint 规则应可配置并进 CI（prompt as code 的检查环节，AIC-040）。
