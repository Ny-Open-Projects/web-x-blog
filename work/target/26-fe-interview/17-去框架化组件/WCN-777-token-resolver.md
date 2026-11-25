---
title: [WCN-777] 笔试：手写主题 token 的正交组合解析器
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-777：笔试：手写主题 token 的正交组合解析器

**答**：
- 需求：实现 `resolveTokens(layers)`，layers 是按优先级从低到高的对象数组（如 `[base, modeLayer, brandLayer]`），每项为 `{ '--token': value }`。后面的层覆盖前面的；支持值中引用其他 token（形如 `var(--x)`），需在同一层+之前层解析引用（简单替换，循环引用忽略）。返回最终 token 对象。
- 要点：合并层级（Object.assign 顺序）；解析 var() 引用用已合并结果替换，最多迭代 N 次防循环；边界：引用不存在的 token 保留原样。

```javascript
function resolveTokens(layers) {
  let merged = {};
  for (const layer of layers || []) merged = { ...merged, ...layer };
  // 解析 var() 引用（最多 10 轮防循环）
  for (let round = 0; round < 10; round++) {
    let changed = false;
    for (const [k, v] of Object.entries(merged)) {
      if (typeof v !== 'string') continue;
      const next = v.replace(/var\((--[\w-]+)\)/g, (m, ref) =>
        ref in merged ? merged[ref] : m);
      if (next !== v) { merged[k] = next; changed = true; }
    }
    if (!changed) break;
  }
  return merged;
}
console.log(resolveTokens([
  { '--brand': '#06f', '--primary': 'var(--brand)' },
  { '--bg': '#fff', '--text': '#000' },
]));
```

**评分点**：
- 按层优先级正确覆盖（后面的层胜出）。
- var() 引用解析正确，且限制迭代轮次防循环引用。
- 引用不存在的 token 保留原样，不丢信息。
- 返回扁平可消费的 token 对象。
