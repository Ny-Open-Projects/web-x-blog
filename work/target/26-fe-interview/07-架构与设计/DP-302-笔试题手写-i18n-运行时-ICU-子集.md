---
title: [DP-302] 笔试题：手写 i18n 运行时（ICU 子集+回退链）？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-302：笔试题：手写 i18n 运行时（ICU 子集+回退链）？
**题目**：实现 I18n 类：1) 懒加载语言包（动态 import）；2) t(key, params) 插值 {name}；3) 复数 t(key, {n}) 按 Intl.PluralRules 选 one/other；4) 回退链 zh-CN→zh→en；5) 缺 key 上报并返回 key。
**评分点**：
- 懒加载并行去重（同一语言同时多次调用只 import 一次）。
- 回退链构建正确（去重、顺序）。
- PluralRules 正确使用（select(n) → 类别 key）。
- 缺 key 上报埋点。
```javascript
class I18n {
  dicts = {}; loading = new Map();
  constructor(private supported = ['en']) {}
  async load(lang) {
    if (this.dicts[lang]) return;
    this.loading.get(lang) ?? this.loading.set(lang, import(`./locales/${lang}.json`).then(m => (this.dicts[lang] = m.default)));  // 1) 去重
    await this.loading.get(lang);
  }
  async t(key, params = {}) {                          // 4) 回退链
    const chain = [...new Set([lang, lang.split('-')[0], ...this.supported])];
    for (const l of chain) {
      await this.load(l);
      const msg = this.dicts[l]?.[key];
      if (!msg) continue;
      return this.format(msg, params);
    }
    reportMissing(key); return key;                    // 5)
  }
  format(msg, { n, ...params }) {
    let out = msg.replace(/\{(\w+)\}/g, (_, k) => String(params[k] ?? `{${k}}`));   // 插值
    if (n != null) {
      const cat = new Intl.PluralRules(this.lang).select(n);    // 3) 复数
      const pluralMsg = this.dicts[this.lang][`${key}_${cat}`] ?? out;
      out = pluralMsg.replace('#', n);
    }
    return out;
  }
}
```
