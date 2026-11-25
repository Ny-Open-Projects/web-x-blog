---
title: [MFW-833] PPR 静态壳与动态洞数据版本不匹配会怎样，怎么校验
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-833：PPR 静态壳与动态洞数据版本不匹配会怎样，怎么校验

**答**：
- 结论：壳在构建期生成、洞在请求期填充；若洞的当前数据版本与壳生成时不一致，会出现「壳说有货、洞说售罄」的矛盾 UI。
- 解法：壳生成时把依赖的数据版本写入壳指纹，洞填充前校验；不匹配就让整页失效走 SSR 兜底，而不是拼接矛盾内容。
- 追问钩子：校验开销在哪？——洞数量少且可枚举才可行，否则退化为定期 revalidate 壳。

```javascript
// 构建期：壳记录依赖数据的版本指纹
const shell = {
  html: '<div>商品信息<!--hole--></div>',
  deps: { stock: 7, price: 7 }
};

// 请求期：洞填充前校验版本
async function fillHoles(shell) {
  const current = await db.versions(['stock', 'price']);
  for (const [k, v] of Object.entries(shell.deps)) {
    if (current[k] !== v) {
      return renderFullSSR();                       // 版本漂移 → 整页兜底
    }
  }
  const stock = await db.stock.get();               // 与壳同一版本
  return shell.html.replace('<!--hole-->', stock);
}
// 若 stock 从 7 变 8 → shell.deps.stock !== current.stock → SSR
```
