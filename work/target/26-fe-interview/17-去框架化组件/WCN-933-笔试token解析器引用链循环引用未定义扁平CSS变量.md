---
title: [WCN-933] 手写 token 解析器：解析引用链、检测循环引用与未定义引用，输出扁平 CSS 变量
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-933：手写 token 解析器：解析引用链、检测循环引用与未定义引用，输出扁平 CSS 变量

**题目**：实现 `resolveTokens(tokens)`，tokens 是扁平对象，值可能是字面量或 `{path.to.token}` 形式的引用。要求：① 解析所有引用为最终字面量（支持链式引用 A→B→C）；② 检测循环引用（A→B→A）时抛出含完整链的错误；③ 引用了未定义的 token 时抛出明确错误；④ 返回扁平化对象（key 保持原路径，值为字面量）；⑤ 不修改输入对象。请自足实现并给出可运行示例（含正常链、循环、未定义三种情况）。

**答**：

```javascript
function resolveTokens(tokens) {
  const out = {};
  const get = (key, stack) => {
    if (key in out) return out[key];
    if (stack.includes(key)) throw new Error('循环引用: ' + [...stack, key].join(' -> '));
    if (!(key in tokens)) throw new Error('未定义引用: ' + key);
    const raw = tokens[key];
    let val = raw;
    if (typeof raw === 'string' && /^\{[^}]+\}$/.test(raw)) {
      val = get(raw.slice(1, -1), [...stack, key]); // 递归解析引用
    }
    out[key] = val;
    return val;
  };
  Object.keys(tokens).forEach(k => get(k, []));
  return out;
}
const t = {
  blue500: '#1677ff',
  link: '{blue500}',
  buttonBg: '{link}',
};
console.log(resolveTokens(t)); // { blue500:'#1677ff', link:'#1677ff', buttonBg:'#1677ff' }
try { resolveTokens({ a: '{b}', b: '{a}' }); }
catch (e) { console.log(e.message); } // 循环引用: a -> b -> a
try { resolveTokens({ x: '{missing}' }); }
catch (e) { console.log(e.message); } // 未定义引用: missing
console.log(t.link); // {blue500}（输入未被修改）
```

**评分点**：
- 链式引用解析正确（A→B→C 展开为最终字面量）。
- 循环引用检测并抛出含完整链的错误信息（a -> b -> a）。
- 未定义引用抛出明确错误。
- 不修改输入对象（out 为新对象）。
- 三种情况示例均可运行、输出正确。
