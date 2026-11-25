---
title: [NODE-971] 笔试题——实现沟通模板管理（模板版本化 + 变量注入）？
date: 2026-11-21
categories: [Node.js与BFF]
tags: [前端面试, 笔试题, Node.js与BFF]
type: 笔试题
---

## NODE-971：手写模板管理

**需求与边界**：
- 需求：模板管理（SCN-联想-757/971）——① 模板版本化（模板变更审计——SCN-联想-757）；② 变量注入（数据填充——SCN-联想-757）；③ 模板的 i18n（SCN-联想-831）；④ 模板的 CI 校验（变量完整性——SCN-ENG-248）。
- 边界：① 变量的缺失防御（缺失变量警告——SCN-ENG-332）；② 模板的灰度（SCN-OPS-228）；③ 模板的渲染测试（SCN-联想-848 IME 测试同构——模板渲染快照）。

**答**：
```javascript
const TEMPLATES = { 'release.summary': { ver: 3, vars: ['app', 'version', 'verdicts'],
  i18n: { en: '...', zh: '...' } } };                  // 版本化 + i18n（SCN-联想-757/831）
function renderTemplate(key, data) {
  const t = TEMPLATES[key];
  const missing = t.vars.filter(v => data[v] === undefined);
  if (missing.length) warn(`模板 ${key} 缺变量 ${missing}（SCN-ENG-332）`);   // 缺失防御
  return interpolate(t.i18n[locale()], data);          // 变量注入
}
```

**评分点**:
- 模板版本化 + i18n（SCN-联想-757/831）。
- 缺失变量警告（SCN-ENG-332）。
- 渲染快照测试（SCN-联想-848 同构）。
