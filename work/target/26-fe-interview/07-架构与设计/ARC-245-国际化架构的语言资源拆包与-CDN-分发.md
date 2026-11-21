---
title: [ARC-245] 国际化架构的语言资源拆包与 CDN 分发？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-245：国际化架构的语言资源拆包与 CDN 分发？
**答**：
- 拆包维度：语言 × 命名空间（common/order/payment），首屏只带当前语言的 common+首屏 ns；切换语言才拉对应包（ARC-085 lazy 基础上做分发架构）。
- 分发形态二选一：**随应用构建**（语言包进 chunk，hash 稳定但与代码耦合）vs **独立语言包服务**（文案平台直接产出 JSON 到 CDN，文案更新不用重新构建代码——推荐，解耦发布节奏）。
- CDN 策略：语言包 URL 带版本+语言 hash，immutable 长缓存；文案平台发布新版本 = 生成新 URL，客户端通过"语言包清单"发现更新（清单短缓存）。
- 体积治理：语言包去重（公共 key 提取）、gzip/br、按需裁剪未用 key（构建时扫描引用做 tree-shaking，可减 30%~60%）。

```javascript
// 独立语言包清单 + 按需加载
async function loadLocale(lang, ns) {
  const manifest = await fetch('/i18n/manifest.json').then(r => r.json());   // 短缓存清单
  const url = manifest[lang][ns];                                            // 形如 /i18n/zh-CN/order.8f3a2.json
  const dict = await fetch(url, { cache: 'force-cache' }).then(r => r.json()); // immutable 长缓存
  mergeDict(lang, ns, dict);
}
// 构建期裁剪：扫描源码 t('order.*') 引用 → 只产出被引用的 key 子集 → diff 体积报告进 CI
```
