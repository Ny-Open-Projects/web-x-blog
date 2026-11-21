---
title: [ARC-085] 国际化 SDK 如何设计（lazy 加载/复数/插值）？
date: 2026-11-17
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-085：国际化 SDK 如何设计（lazy 加载/复数/插值）？
**答**：
- 资源 lazy：按语言 + 按命名空间拆包，首屏只加载当前语言的核心 namespace，切换语言时动态 import。
- 能力：插值、复数规则（ICU MessageFormat，复数规则按语言不同：俄语 3 种/阿语 6 种）、日期数字本地化（Intl API 优先）。
- 架构配套：语言持久化与协商顺序（URL → localStorage → navigator → 默认）、RTL 布局、缺失 key 降级链（zh-CN → zh → en）。

```typescript
// i18n 核心：lazy 加载 + 复数 + 插值
const loaders: Record<string, () => Promise<Record<string, string>>> = {
  'zh-CN': () => import('./locales/zh-CN.json').then(m => m.default),
  'en':    () => import('./locales/en.json').then(m => m.default),
};

class I18n {
  private dict: Record<string, string> = {};
  async load(lang: string) {
    const fallbackChain = [lang, lang.split('-')[0], 'en'].filter(uniq); // 降级链 zh-CN → zh → en
    for (const l of fallbackChain) {
      if (loaders[l]) Object.assign(this.dict, await loaders[l]());
      if (this.dict[0]) break;
    }
    document.documentElement.lang = lang;
    document.documentElement.dir = lang === 'ar' ? 'rtl' : 'ltr';       // RTL
  }
  t(key: string, params?: Record<string, unknown>, plural?: number): string {
    const template = this.dict[key] ?? key;                             // 缺失 key 原样返回并上报
    const chosen = plural != null ? this.dict[`${key}_${pluralRule(plural, this.lang)}`] ?? template : template;
    return chosen.replace(/\{(\w+)\}/g, (_, k) => String(params?.[k] ?? `{${k}}`)); // 插值
  }
}
// 语言资源：order.title、order.count_one / order.count_other（ICU 复数类别）
// i18n.t('order.count', { n: 3 }, 3) → "3 orders"
```
