---
title: [TST-756] 笔试：实现送模数据的 PII 网关检测器（正则 + 熵值 + 白名单）
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-756：笔试：实现送模数据的 PII 网关检测器（正则 + 熵值 + 白名单）

**题目**：输入文本 text 与白名单数组 whitelist。检测三类 PII：手机号（1 开头 11 位数字）、邮箱、高熵 token（连续 20+ 位字母数字且香农熵 > 3.5）。命中任一类返回 { blocked:true, types:[...] }，否则 { blocked:false, types:[] }。白名单中的完整字符串出现时跳过该次检测（整段匹配则直接放行）。

**答**：
- 三类规则独立检测，命中收集类型。
- 香农熵计算字符集分布，token 提取后判定。
- 白名单整段匹配直接放行。

```javascript
function shannon(s) {
  const freq = {};
  for (const c of s) freq[c] = (freq[c] || 0) + 1;
  return -Object.values(freq).reduce((h, n) => {
    const p = n / s.length; return h + p * Math.log2(p);
  }, 0);
}
function detectPII(text, whitelist) {
  if (whitelist.some(w => text === w)) return { blocked: false, types: [] };
  const types = [];
  if (/1\d{10}/.test(text)) types.push('PHONE');
  if (/[\w.+-]+@[\w-]+\.[\w.]+/.test(text)) types.push('EMAIL');
  const tokens = text.match(/[A-Za-z0-9]{20,}/g) || [];
  if (tokens.some(shannon > 3.5)) types.push('TOKEN');
  return { blocked: types.length > 0, types };
}
console.log(detectPII('联系 13800138000', [])); // PHONE
```

**评分点**：
- 三类 PII 规则检测正确
- 香农熵计算正确
- 白名单放行逻辑
- 返回结构与类型收集
