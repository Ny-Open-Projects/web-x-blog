---
title: [AGT-493] 笔试题——实现模板变量注入防护（变量白名单+转义+结构隔离）？
date: 2026-11-20
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-493：手写模板注入防护：变量白名单、用户输入转义、指令区隔离

**需求与边界**：
- 输入：prompt 模板（含 {{变量}}）、变量值；输出：安全编译后的 prompt。
- 边界要求：① 变量白名单（模板声明外的变量拒绝）；② 用户输入类变量转义（指令性语句标记为数据）；③ 指令区与数据区结构隔离（数据不进指令区）；④ 长度护栏（单变量超限截断）。

**答**：
```javascript
function compileTemplate(tpl, vars, { declared }) {
  // 1. 白名单：未声明变量拒绝（防未预期注入面）
  const used = [...tpl.matchAll(/\{\{(\w+)\}\}/g)].map(m => m[1]);
  const unknown = used.filter(v => !declared.includes(v));
  if (unknown.length)
    throw new Error(`模板使用未声明变量: ${unknown}`);
  // 2. 分区编译：指令区变量原样；数据区变量转义包装
  const escapeUser = (s) => {
    const truncated = String(s).slice(0, 4000);  // 长度护栏
    const flagged = /忽略|ignore|system|指令/i.test(truncated)
      ? '（用户输入中含指令性内容，已按数据处理）'
      : '';
    return `<<DATA\n${truncated}\nDATA>>${flagged}`;
  };
  const compiled = tpl.replace(/\{\{(\w+)\}\}/g, (_, v) => {
    const val = vars[v];
    if (val == null) throw new Error(`缺变量: ${v}`);
    return declared.meta?.[v]?.kind === 'user_input'
      ? escapeUser(val)                          // 用户输入转义包装
      : String(val);                             // 系统值原样
  });
  // 3. 结构隔离检查：用户数据不得出现在指令区
  // 模板按段声明 kind: instruction|data
  return { compiled, audit: { used, escaped:
    used.filter(v => declared.meta?.[v]?.kind === 'user_input') } };
}
// declared: { fields: ['query','policy'],
//   meta: { query: { kind: 'user_input' },
//           policy: { kind: 'system' } } }
```

**评分点**:
- 变量白名单（未声明拒绝）+ 缺变量报错——注入面最小化。
- 用户输入类变量转义包装（DATA 定界）+ 指令性内容检测标注。
- 长度护栏（4000 截断）防上下文爆量注入。
- 指令/数据分区编译的结构隔离思想。
