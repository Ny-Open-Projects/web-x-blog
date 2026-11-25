---
title: [1010] 笔试手写：实现输出侧敏感信息扫描与脱敏
date: 2026-11-17
categories: [AI与Agent]
tags: [前端面试, 笔试题, 安全, DLP]
type: 笔试题
---

## 1010：笔试手写：实现输出侧敏感信息扫描与脱敏

**答**：实现 scan(text)：检测四类敏感信息——API Key（形如 sk-开头 20+ 位）、手机号（1 开头 11 位）、身份证（18 位含校验尾码简单版：长度+字符集）、内部域名（*.corp.internal）。返回 { findings: [{type, count}], safe: 脱敏后文本 }，脱敏保留前 4 后 2（身份证保留前 6 后 2），手机号中间 4 位打码。

```js
const RULES = [
  { type: 'api_key', re: /\bsk-[A-Za-z0-9]{20,}\b/g, mask: s => s.slice(0, 5) + '***' + s.slice(-2) },
  { type: 'phone', re: /\b1[3-9]\d{9}\b/g, mask: s => s.slice(0, 3) + '****' + s.slice(7) },
  { type: 'id_card', re: /\b\d{17}[\dXx]\b/g, mask: s => s.slice(0, 6) + '********' + s.slice(-2) },
  { type: 'internal_host', re: /[\w-]+\.corp\.internal\b/g, mask: () => '[internal]' },
];
function scan(text) {
  const findings = {};
  let safe = text;
  for (const r of RULES) {
    const found = [...text.matchAll(r.re)];
    if (found.length) {
      findings[r.type] = found.length;
      safe = safe.replace(r.re, r.mask);       // 全量脱敏
    }
  }
  return { findings, safe, ok: Object.keys(findings).length === 0 };
}
console.log(scan('联系 13812345678 或用 sk-abcdef1234567890abcdef12').findings);
// { phone: 1, api_key: 1 }
```

**评分点**：
- 四类正则边界正确（单词边界防误伤、手机号第二位 3-9、身份证尾码 X 兼容）
- 脱敏保留位数按类型区分，可恢复性/可用性权衡有说明
- findings 按类型计数（可聚合告警），safe 文本可直接下发
- 能讨论：正则 DLP 只是第一层，语义级泄露（改写后的敏感事实）需叠 NER/LLM 审查

