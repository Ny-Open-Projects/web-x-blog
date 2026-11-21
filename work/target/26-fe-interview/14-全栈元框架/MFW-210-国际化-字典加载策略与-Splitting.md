---
title: [MFW-210] 国际化字典加载策略与按需 Splitting
date: 2026-11-20
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-210：i18n 字典加载策略

**答**:
- 服务端组件读字典：直接 import（构建期打包，SSR 渲染零延迟）——但全语言打包体积大；改进：按 [lang] 动态 import（每语言独立 chunk）
- 客户端组件读字典：字典经 props 从 RSC 传（只传用到的 key 子集——序列化瘦身）或独立请求（语言包接口）
- 命名空间拆分：公共词库（header/footer）+ 页面级词库——页面切换只拉页面词库（增量）
- 语言切换体验：切换即加载新语言包（预加载目标语言——用户可能切换）+ 文案回退链（zh-TW→zh→en）

```javascript
// RSC：按语言动态加载
const dicts = { en: () => import('./dictionaries/en.json'), zh: () => import('./dictionaries/zh.json') }
export async function getDict(lang) { return (await dicts[lang]()).default }
// 传客户端：只传需要的子集（序列化瘦身）
<Counter labels={{ add: t('cart.add'), remove: t('cart.remove') }} />
```
