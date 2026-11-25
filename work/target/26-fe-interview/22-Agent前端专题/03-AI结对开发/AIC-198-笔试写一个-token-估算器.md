---
title: [AIC-198] 笔试：实现一个 Token 估算器：中英文混合密度、代码块特殊计价与误差校准系数？
date: 2026-11-18
categories: [AI结对开发]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-198：笔试：实现一个 Token 估算器：中英文混合密度、代码块特殊计价与误差校准系数？
**答**：实现 `estimate(text)`：
- 中文按 ~1.5 字符/token、英文按 ~4 字符/token，混合文本分段计算；
- 代码块内 token 密度不同（符号多、空格多 → ~3 字符/token）；
- 支持校准系数：用真实 tokenizer 的历史样本校准（estimate × k 趋近真实值）；
- 输出 `{tokens, breakdown: {cjk, latin, code}}`。

```javascript
const F = '\u0060'.repeat(3);   // 围栏用码点构造，避免源码内出现字面围栏
function estimate(text, { calibrate = 1 } = {}) {
  // 先剥离代码块单独计价
  let code = '', prose = text;
  const codeMatches = [...text.matchAll(new RegExp(F + '[\\w]*\\n([\\s\\S]*?)' + F, 'g'))];
  for (const m of codeMatches) { code += m[1]; prose = prose.replace(m[0], ''); }

  const cjk = (prose.match(/[\u4e00-\u9fa5\u3000-\u303f\uff00-\uffef]/g) || []).length;
  const latin = prose.replace(/[\u4e00-\u9fa5\u3000-\u303f\uff00-\uffef]/g, '').length;

  // 代码块内部：符号与标识符密度近似 3 字符/token
  const codeTokens = Math.ceil(code.length / 3);

  const t = Math.ceil((cjk / 1.5 + latin / 4 + codeTokens) * calibrate);
  return { tokens: t, breakdown: { cjk: Math.ceil(cjk / 1.5), latin: Math.ceil(latin / 4), code: codeTokens } };
}

// 校准：用历史样本拟合系数（真实 token 数 / 估算值 的均值）
function calibrateFrom(samples) { // [{text, realTokens}]
  const ratios = samples.map(s => s.realTokens / estimate(s.text).tokens);
  return +(ratios.reduce((a, b) => a + b, 0) / ratios.length).toFixed(3);
}

// 测试
const sample = `说明：实现分页。
\`\`\`ts
const usePagination = (page: number) => { /* 50 chars */ };
\`\`\``;
console.log(estimate(sample));
// breakdown 区分 prose 中文/英文与 code
const k = calibrateFrom([
  { text: '中英文 mixed text 例子', realTokens: 12 },
  { text: '纯中文样本一二三四五六七八九十', realTokens: 14 },
]);
console.log(estimate(sample, { calibrate: k }));
```

**评分点**：
1. 中英混合分段计数（含中文标点全角归类），一刀切 4 字符/token 对中文误差 2 倍以上；
2. 代码块单独计价（符号密度高），忽略这点会低估代码任务上下文；
3. 校准系数机制：估算器必须有「向真实 tokenizer 收敛」的通路；
4. breakdown 便于定位哪类内容吃掉预算（优化有方向）；
5. 追问：精确计数应接入真实 tokenizer（tiktoken 类），估算器用于预算前置检查与无 tokenizer 场景。
