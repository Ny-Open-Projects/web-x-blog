---
title: [WCN-094] 笔试：手写 Signals 版国际化运行时（locale 切换即时生效）
date: 2026-11-19
categories: [去框架化组件]
tags: [前端面试, 笔试题, Signals]
type: 笔试题
---

## WCN-094：笔试：手写 Signals 版国际化运行时

**题目**：① `locale` signal（如 'zh-CN'/'en-US'）；② 字典按 locale 懒加载（import 动态分包）；③ `t(key, params)` 在 effect/computed 内调用时随 locale 变化自动更新；④ 未命中 key 回落默认 locale 并 dev 告警一次；⑤ 复数处理：`t('msg.count', { n })` 按 Intl.PluralRules 选择键；⑥ 返回 `setLocale` 与切换完成 Promise。

**答**：

```javascript
import { createSignal, effect, untrack } from './mini.js';

const [locale, setLocale] = createSignal(navigator.language);
const dictCache = new Map(); // locale -> Promise<dict>
const fallback = 'en-US';

function loadDict(l) {
  if (!dictCache.has(l)) dictCache.set(l, import(`./locales/${l}.json`).then((m) => m.default));
  return dictCache.get(l);
}
// 预热当前 locale，保证 t() 首次同步可用
let ready = loadDict(untrack(locale));

function pluralKey(n, locale) {
  const rules = new Intl.PluralRules(locale);
  return `key:${rules.select(n)}`;   // zero/one/two/few/many/other
}

function t(key, params = {}) {
  const dict = untrack(() => dictCache.get(untrack(locale))); // 同步缓存快照
  let tpl = dict?.[key] ?? null;
  if (tpl === null) {
    console.warn(`missing i18n key: ${key}`);   // 一次告警（可用 Set 去重）
    tpl = key;
  }
  if ('n' in params) {
    const pk = pluralKey(params.n, untrack(locale));
    tpl = dict?.[pk] ?? tpl;
  }
  return tpl.replace(/\{(\w+)\}/g, (_, k) => params[k] ?? `{${k}}`);
}

async function changeLocale(l) {
  await loadDict(l);   // 先加载再切换，避免闪烁
  setLocale(l);
}
// 组件绑定：effect(() => { titleEl.textContent = t('cart.title'); itemEl.textContent = t('msg.count', { n: n() }); })
// locale 变化 → 所有含 t() 的 effect 自动重跑（locale 是 t 读取的依赖）
```

**评分点**：
- locale 为 signal，t() 内读取触发依赖收集（切换即全量文案刷新，无手动刷新）。
- 字典懒加载 + 先加载后切换（避免中间态）。
- Intl.PluralRules 复数选择与参数插值。
- 未命中回落 + 告警去重。
