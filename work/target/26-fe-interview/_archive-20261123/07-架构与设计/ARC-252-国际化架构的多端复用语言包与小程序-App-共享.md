---
title: [ARC-252] 国际化架构的多端复用：语言包与小程序/App 共享？
date: 2026-11-19
categories: [前端架构]
tags: [前端面试, 面试题, 17]
type: 面试题
---

## ARC-252：国际化架构的多端复用：语言包与小程序/App 共享？
**答**：
- 目标：一份文案源，多端（Web/小程序/App）消费。核心是**语言包产物标准化**：文案平台产出统一 JSON（key+ICU 消息），各端运行时各自实现 t() 消费同一份产物。
- 端差异隔离：格式化能力（日期/货币/复数）Web 用 Intl，小程序无完整 Intl 则内置 ICU 子集库；RTL 只 Web/部分端有，App 端额外要接原生字符串目录（iOS .strings/Android strings.xml 由同一源生成）。
- key 规范统一：全平台同一 key 体系，端独有文案加端前缀（`mp.*`/`app.*`），CI 校验各端引用的 key 都存在于统一源。
- 版本同步：文案平台按"版本+端"发布，App 端走内嵌基线 + 差量热更（类似语言包清单机制）。

```javascript
// 文案平台产物（统一源）
// zh-CN.json: { "order.count_one": "{n} 单", "order.count_other": "{n} 单", "mp.share.tip": "..." }
// 各端生成：
//   Web:  /i18n/zh-CN/common.json（HTTP）
//   iOS:  Localizable.strings 由脚本从同一 JSON 生成
//   小程序: 内置打包或 wx.request 拉取清单（结构同 Web）
function t(key, params, platform) {
  const msg = dict[platform]?.[key] ?? dict.web[key] ?? key;  // 端缺文案回退 Web 源
  return icuFormat(msg, params);                              // 各端一致的 ICU 子集实现
}
// CI：扫 Web/小程序/App 三仓库的 t() 引用 → key 必须在统一源 → 缺失报错
```
