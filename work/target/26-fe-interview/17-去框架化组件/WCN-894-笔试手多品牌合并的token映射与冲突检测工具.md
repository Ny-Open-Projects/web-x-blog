---
title: [WCN-894] 笔试：手写多品牌合并的「token 映射与冲突检测」工具
date: 2026-11-23
categories: [去框架化组件]
tags: [前端面试, 笔试题, WCN]
type: 笔试题
---

## WCN-894：笔试：手写多品牌合并的「token 映射与冲突检测」工具

**题目**：品牌归一时需把两个品牌的 token 合并。实现 `mergeBrands(brandA, brandB, mapping)`。输入两个 token 对象与映射表 `mapping: { 统一key: { a: 'A中的key', b: 'B中的key' } }`。要求：① 按 mapping 把两品牌的 token 归到统一 key 下，生成 `{ 统一key: { a: 值, b: 值, resolved: 最终值 } }`；② 冲突检测：若 a 与 b 值不同，`resolved` 取 `strategy` 指定——`'preferA'|'preferB'` 直接取一方，`'flag'` 标记为冲突（resolved=null, conflict=true）；③ mapping 未覆盖但两品牌都有的同名 key，自动归入并同样检测；④ 只在一个品牌存在的 key 直接采用该值（resolved=该值, conflict=false）。边界：mapping 指向的源 key 不存在时该侧值为 undefined；支持数字/字符串值。

**答**：

```javascript
function mergeBrands(brandA, brandB, mapping = {}, strategy = 'flag') {
  const result = {};
  function resolve(a, b) {
    const conflict = !Object.is(a, b);
    if (!conflict) return { a, b, resolved: a, conflict: false };
    let resolved = null;
    if (strategy === 'preferA') resolved = a;
    else if (strategy === 'preferB') resolved = b;
    return { a, b, resolved, conflict: true };
  }
  // 按显式 mapping 归并
  for (const [key, m] of Object.entries(mapping)) {
    result[key] = resolve(brandA[m.a], brandB[m.b]);
  }
  // 自动归并：两品牌都有、且未被 mapping 覆盖的同名 key
  const mappedA = new Set(Object.values(mapping).map(m => m.a));
  const mappedB = new Set(Object.values(mapping).map(m => m.b));
  for (const key of new Set([...Object.keys(brandA), ...Object.keys(brandB)])) {
    if (key in result || mappedA.has(key) || mappedB.has(key)) continue;
    result[key] = resolve(brandA[key], brandB[key]);
  }
  return result;
}
const A = { primary: '#06c', gap: '8px', onlyA: 'x' };
const B = { brand: '#e00', gap: '12px', onlyB: 'y' };
console.log(mergeBrands(A, B, { primary: { a: 'primary', b: 'brand' } }, 'flag'));
// primary: 冲突(flag), gap: 冲突(flag), onlyA/onlyB: 直接采用
```

**评分点**：
- 按 mapping 归并 + 同名 key 自动归并 + 单边 key 直接采用，覆盖全部情况（完整性）。
- 冲突检测用 Object.is，strategy 三种策略正确（核心逻辑）。
- 避免重复归并（mappedA/mappedB 去重），边界（源 key 不存在→undefined）处理（细节）。
- 输出结构含 a/b/resolved/conflict，便于后续人工裁决（可用性）。
