---
title: [XP-309] 跨端 UI 一致性：设计 Token 与主题下发
date: 2026-11-22
categories: [垂直方向]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## XP-309：跨端 UI 一致性：设计 Token 与主题下发

**答**：
- Token：颜色/间距/字号/圆角统一 JSON，各端映射（CSS 变量/RN StyleSheet/Flutter ThemeData）。
- 下发：主题走配置中心（可热更），端侧本地缓存兜底。
- 校验：CI 校验 Token 引用完整性（禁止硬编码色值）。

```javascript
// 设计 Token 映射
const TOKENS = { primary: '#1677ff', gap: 12, radius: 8 };
const ADAPTERS = {
  web: t => Object.entries(t).map(([k, v]) => `--${k}: ${v};`).join(''),
  rn: t => ({ primaryColor: t.primary, spacing: t.gap, borderRadius: t.radius }),
  flutter: t => ({ primary: t.primary, spacing: t.gap * 1.0 }),
};
function theme(platform) { return ADAPTERS[platform](TOKENS); }
```
