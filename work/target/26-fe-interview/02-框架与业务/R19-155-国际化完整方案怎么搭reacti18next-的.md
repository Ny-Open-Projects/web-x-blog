---
title: [R19-155] 国际化完整方案怎么搭？react-i18next 的懒加载、命名空间与回退如何设计？
date: 2026-11-17
categories: [React19]
tags: [前端面试, 面试题, 07]
type: 面试题
---

## R19-155：国际化完整方案怎么搭？react-i18next 的懒加载、命名空间与回退如何设计？
**答**：
- 分包：按 namespace 拆语言包（common/订单/用户），`loadPath` 按需加载，只打默认语言的公共包，其余 chunk 懒加载。
- 回退链：语言回退 `zh-CN -> zh -> en`，key 缺失回 fallbackLng，并在开发期显示 key 本身便于排查。
- 插值/复数/日期本地化：i18next 插值 `{{count}}` + 复数后缀 `_one/_other`，日期金额交给 Intl.DateTimeFormat/NumberFormat。
- 切换语言 = `i18n.changeLanguage(lng)`，配合后端接口语言头与 URL（如 /en/...）保证 SSR 与 SEO 一致。

```tsx
// i18n.ts —— react-i18next 完整配置
import i18n from 'i18next';
import { initReactI18next } from 'react-i18next';
import HttpBackend from 'i18next-http-backend';
import LanguageDetector from 'i18next-browser-languagedetector';

i18n
  .use(LanguageDetector)          // 检测顺序：localStorage -> navigator -> html lang
  .use(HttpBackend)               // 语言包按 namespace 懒加载
  .use(initReactI18next)
  .init({
    fallbackLng: 'en',            // 终极回退
    supportedLngs: ['zh-CN', 'zh', 'en'],
    nonExplicitSupportedLngs: true, // zh-TW/zh-HK 自动归到 zh
    load: 'languageOnly',
    ns: ['common'],               // 只预载公共包
    defaultNS: 'common',
    backend: {
      // 懒加载：/locales/{lng}/{ns}.json，切到订单页才拉 orders.json
      loadPath: '/locales/{{lng}}/{{ns}}.json',
    },
    interpolation: { escapeValue: false }, // React 已防 XSS
    returnEmptyString: false,
    saveMissing: true,            // 开发期上报缺失 key
    missingKeyHandler: (lngs, ns, key) => {
      if (import.meta.env.DEV) console.warn(`missing: ${ns}:${key} in ${lngs}`);
    },
  });

export default i18n;

// OrderPage.tsx —— 使用侧：懒加载命名空间 + 插值 + 复数
import { useTranslation } from 'react-i18next';

export function OrderPage() {
  const { t, i18n } = useTranslation(['orders', 'common']); // 组件声明用到的 ns，触发按需加载
  return (
    <div>
      <h1>{t('orders:title')}</h1>
      {/* 插值 */}
      <p>{t('orders:total', { count: 3 })}</p>
      {/* 复数：en 里 orders:items_one / orders:items_other */}
      <p>{t('orders:items', { count: 3 })}</p>
      {/* 金额与日期交给 Intl，语言跟随 i18n */}
      <p>{new Intl.NumberFormat(i18n.language, { style: 'currency', currency: 'USD' }).format(99.5)}</p>
      <button onClick={() => i18n.changeLanguage(i18n.language === 'zh' ? 'en' : 'zh')}>
        {t('common:switchLang')}
      </button>
    </div>
  );
}
```
