---
title: [WCN-940] 手写多端 token 编译器：一份 JSON 输出 CSS 变量 / iOS / Android / 小程序四端
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-940：手写多端 token 编译器：一份 JSON 输出 CSS 变量 / iOS / Android / 小程序四端

**题目**：实现 `compileTokens(tokens, target)`，tokens 为扁平对象（值含 `{ref}` 引用），target 取 'css' | 'ios' | 'android' | 'mini'。要求：① 先解析所有引用为字面量（支持链式，检测循环与未定义引用）；② css 输出 `:root{--key:value;}`；③ ios 输出 Swift 字典（key: value 每行，值加引号）；④ android 输出 XML 的 color 标签（key 中点转下划线）；⑤ mini 输出 wxss `page{--key:value;}`；⑥ 未知 target 抛错。请自足实现并给出四端输出的可运行示例。

**答**：

```javascript
function compileTokens(tokens, target) {
  const cache = {};
  const resolve = (k, stack = []) => {
    if (k in cache) return cache[k];
    if (stack.includes(k)) throw new Error('循环引用: ' + [...stack, k].join('->'));
    if (!(k in tokens)) throw new Error('未定义: ' + k);
    const raw = tokens[k];
    const val = (typeof raw === 'string' && /^\{[^}]+\}$/.test(raw))
      ? resolve(raw.slice(1, -1), [...stack, k]) : raw;
    cache[k] = val; return val;
  };
  const flat = Object.fromEntries(Object.keys(tokens).map(k => [k, resolve(k)]));
  const entries = Object.entries(flat);
  switch (target) {
    case 'css':    return ':root{' + entries.map(([k, v]) => `--${k}:${v};`).join('') + '}';
    case 'mini':   return 'page{' + entries.map(([k, v]) => `--${k}:${v};`).join('') + '}';
    case 'ios':    return entries.map(([k, v]) => `"${k}": "${v}",`).join('\n');
    case 'android':return entries.map(([k, v]) =>
      `    <color name="${k.replace(/\./g, '_')}">${v}</color>`).join('\n');
    default: throw new Error('未知 target: ' + target);
  }
}
const t = { blue: '#1677ff', link: '{blue}' };
['css', 'ios', 'android', 'mini'].forEach(x =>
  console.log('---' + x + '---\n' + compileTokens(t, x)));
try { compileTokens(t, 'flutter'); } catch (e) { console.log(e.message); }
```

**评分点**：
- 引用解析正确（链式 + 循环/未定义检测），四项前置处理到位。
- 四种 target 输出格式均符合约定（css/mini/ios/android）。
- android 的 key 中点正确转下划线。
- 未知 target 抛错，非法输入健壮。
- 四端示例输出正确可运行。
