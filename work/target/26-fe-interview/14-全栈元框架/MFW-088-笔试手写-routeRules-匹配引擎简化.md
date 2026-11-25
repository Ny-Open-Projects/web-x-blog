---
title: [MFW-088] 笔试：手写一个简化版 routeRules 匹配引擎
date: 2026-11-18
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-088：笔试：手写一个简化版 routeRules 匹配引擎
**答**：Nuxt 的 routeRules 支持精确路径与通配符（`/products/**`、`/docs/*`）。实现 `matchRules(rules, path)`：① 返回**所有**命中的规则按声明顺序；② `**` 匹配多级路径，`*` 只匹配单段；③ 精确匹配优先级最高；④ 支持后续规则覆盖前面规则的键（合并视图）。

```ts
type Rule = { swr?: number; ssr?: boolean; headers?: Record<string, string> };

function toRegExp(pattern: string): RegExp {
  // 转义正则特殊字符，再还原通配符
  const escaped = pattern
    .replace(/[.+?^${}()|[\]\\]/g, '\\$&')
    .replace(/\*\*/g, '\u0000')   // 占位防被下一步误替换
    .replace(/\*/g, '[^/]+')       // * : 单段
    .replace(/\u0000/g, '.*');     // ** : 多级
  return new RegExp(`^${escaped}$`);
}

function matchRules(rules: Record<string, Rule>, path: string): Array<{ pattern: string; rule: Rule }> {
  const exact = rules[path] ? [{ pattern: path, rule: rules[path] }] : [];
  const wild = Object.entries(rules)
    .filter(([pattern]) => pattern.includes('*'))
    .filter(([pattern]) => toRegExp(pattern).test(path))
    .map(([pattern, rule]) => ({ pattern, rule }));
  // 精确命中直接返回（优先级最高），否则按声明顺序返回全部通配命中
  return exact.length ? exact : wild;
}

function mergeMatched(rules: Record<string, Rule>, path: string): Rule {
  const hits = matchRules(rules, path);
  return hits.reduce<Rule>((acc, { rule }) => {
    return {
      ...acc,
      ...rule,                                  // 后者覆盖前者
      headers: { ...acc.headers, ...rule.headers }, // headers 深合并
    };
  }, {});
}

// —— 断言用例 ——
const rules = {
  '/': { prerender: true } as Rule,
  '/products/**': { swr: 600 },
  '/products/featured': { ssr: false },
  '/api/*': { headers: { 'cache-control': 'no-store' } },
};
console.assert(matchRules(rules, '/products/featured').length === 1); // 精确优先
console.assert(matchRules(rules, '/products/a/b/c').length === 1);    // ** 多级
console.assert(toRegExp('/api/*').test('/api/v1') === true);
console.assert(toRegExp('/api/*').test('/api/v1/x') === false);       // * 不跨段
console.log(mergeMatched(rules, '/products/featured')); // { ssr: false }
```

**评分点**：
1. 通配符转换正确：`*` 为 `[^/]+`（不跨段），`**` 为 `.*`，且先转义特殊字符防止注入路径崩溃正则。
2. 精确匹配优先级高于通配（或明确说明合并策略）。
3. `**` 占位符技巧避免被 `*` 的替换污染，或者用等价实现也能得分。
4. 合并时 headers 做了二级合并而不是整个对象覆盖。
5. 返回所有命中规则而非第一个——能说清 Nuxt/Nitro 实际语义是多规则叠加。
