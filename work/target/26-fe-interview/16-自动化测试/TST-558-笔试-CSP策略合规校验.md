---
title: [TST-558] 笔试：笔试：CSP 策略合规性校验器
date: 2026-11-23
categories: [自动化测试]
tags: [前端面试, 笔试题, TST]
type: 笔试题
---

## TST-558：笔试：笔试：CSP 策略合规性校验器

**题目**：实现 validateCsp(cspHeader, config)。cspHeader 是 Content-Security-Policy 头字符串（如 "default-src 'self'; script-src 'self' 'unsafe-inline'; img-src *"）。config={ forbid: ['unsafe-inline', '*'], require: ['default-src', 'object-src'], maxWildcardSrc: 0 }。要求：① 解析成 {directive: [sources]} 映射；② forbid 中的 source 出现在任何指令则记为违规；③ require 中的指令必须存在；④ wildcard '*' 出现次数（作为 source）超过 maxWildcardSrc 记违规；⑤ 输出 {valid, violations:[string]}。边界：空 header、多余空格、大小写不敏感。

**答**：
- 结论：解析指令为映射 → 逐条检查 forbid/require/通配符 → 聚合违规。
- 实现要点：用 split(';') 再 split(/\s+/)；source 匹配忽略大小写和引号；require 缺失单独记；统计 '*' 作为 source 的出现次数。
- 追问钩子：CSP 太严影响业务（如内联脚本）怎么办？——用 nonce/hash 替代 'unsafe-inline'，逐步收紧并配合 report-only 模式观测违规再切换 enforcing。

```javascript
function validateCsp(header = '', config) {
  const parsed = {};
  for (const part of header.split(';')) {
    const [dir, ...srcs] = part.trim().split(/\s+/);
    if (dir) parsed[dir.toLowerCase()] = srcs.map(s => s.toLowerCase());
  }
  const violations = [];
  for (const [dir, srcs] of Object.entries(parsed))
    for (const s of srcs)
      if (config.forbid.some(f => s === f.toLowerCase())) violations.push(`${dir} 含禁用源 ${s}`);
  for (const d of config.require)
    if (!parsed[d]) violations.push(`缺少必需指令 ${d}`);
  const wildcards = Object.values(parsed).flat().filter(s => s === '*').length;
  if (wildcards > config.maxWildcardSrc) violations.push(`通配符源过多: ${wildcards}`);
  return { valid: violations.length === 0, violations };
}
```

**评分点**：
- 正确解析 CSP 头为指令→源列表映射，大小写不敏感。
- forbid 源与 require 指令检查正确。
- 通配符 '*' 计数与 maxWildcardSrc 判定正确。
- 空 header / 多余空格等边界不报错，违规信息可读。
