---
title: [DP-320] 笔试题：手写 i18n 热切换 Provider？
date: 2026-11-19
categories: [设计模式]
tags: [前端面试, 笔试题, 21]
type: 笔试题
---

## DP-320：笔试题：手写 i18n 热切换 Provider？
**题目**：实现 React I18nProvider：1) Context + useSyncExternalStore 驱动语言切换；2) 切换语言预加载新语言包完成才切换（防闪烁）；3) t(key) 响应式；4) 切换后持久化 + URL 同步。
**评分点**：
- store 模式正确（version 计数 + subscribe）。
- 预加载后原子切换（loading 期间保持旧语言）。
- useSyncExternalStore getSnapshot 稳定（返回 version）。
- URL/Cookie 同步。
```tsx
const store = { lang: 'zh-CN', version: 0, listeners: new Set() };
function setLang(lang) { store.lang = lang; store.version++;
  store.listeners.forEach(l => l());
  document.cookie = `lang=${lang}`;
  history.replaceState(null, '', `?lang=${lang}`); }      // 4)
async function switchLang(lang) {
  await loadLocale(lang);                                  // 2) 预加载完成才切
  setLang(lang);
}
const I18nContext = createContext(null);
export function I18nProvider({ children }) {
  const version = useSyncExternalStore(
    (l) => { store.listeners.add(l); return () => store.listeners.delete(l); },
    () => store.version, () => 0);                         // 3) 稳定 snapshot
  const i18n = useMemo(() => ({
    t: (key, params) => format(store.dicts[store.lang]?.[key] ?? key, params),
    lang: store.lang, version,
  }), [version]);                                          // version 变化重建 t
  return <I18nContext.Provider value={i18n}>{children}</I18nContext.Provider>;
}
export function useT() { return useContext(I18nContext); }
```
