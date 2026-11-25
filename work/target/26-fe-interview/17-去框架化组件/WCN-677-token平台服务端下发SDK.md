---
title: [WCN-677] 笔试：实现 token 平台的服务端下发 SDK（按主题/品牌/版本生成 CSS 变量并按环境缓存）
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-677：笔试：实现 token 平台的服务端下发 SDK（按主题/品牌/版本生成 CSS 变量并按环境缓存）

**答**：
- 需求：实现 getTokens({brand, theme, version})：从本地 token 注册表按 brand→theme→version 合并（覆盖优先）；生成 CSS 变量字符串；用 Map 缓存相同参数结果。
- 思路：分层 deepMerge（后层覆盖前层）；生成 --ds-* 变量；缓存 key 用参数序列化；返回 { css, vars }。
- 边界：缺失层级回退到默认品牌/浅色主题；循环引用检测；缓存上限防无限增长。

```javascript
const REGISTRY = {
  base: { color: { primary: '#165DFF' }, radius: { md: '8px' } },
  dark: { color: { primary: '#4E8CF7' } },
  brandB: { color: { primary: '#F53F3F' } },
};
const cache = new Map();
function deepMerge(a, b) {
  const out = { ...a };
  for (const [k, v] of Object.entries(b || {})) {
    out[k] = v && typeof v === 'object' ? deepMerge(out[k] || {}, v) : v;
  }
  return out;
}
function toCssVars(obj, prefix = '--ds') {
  return Object.entries(obj).flatMap(([k, v]) =>
    v && typeof v === 'object'
      ? toCssVars(v, `${prefix}-${k}`)
      : [`${prefix}-${k}:${v};`]).join('\n');
}
export function getTokens({ brand = 'base', theme = 'base', version = 'latest' } = {}) {
  const key = [brand, theme, version].join(':');
  if (cache.has(key)) return cache.get(key);
  const merged = deepMerge(REGISTRY.base,
    deepMerge(REGISTRY[brand] || {}, REGISTRY[theme] || {}));
  const result = { css: toCssVars(merged), vars: merged };
  if (cache.size < 200) cache.set(key, result);
  return result;
}
console.log(getTokens({ theme: 'dark' }).css);
```

**评分点**：
- 分层 deepMerge 覆盖顺序正确（brand/theme 覆盖 base）。
- 生成 CSS 变量递归处理嵌套对象，前缀正确。
- 缓存 key 由全部参数构成，且设上限防无限增长。
- 缺失层级回退默认，不抛异常。
