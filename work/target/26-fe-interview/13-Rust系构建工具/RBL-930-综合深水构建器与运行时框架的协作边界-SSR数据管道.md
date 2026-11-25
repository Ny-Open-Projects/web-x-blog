---
title: [RBL-930] 综合深水：构建器与运行时框架的协作边界——SSR 数据管道的产物约定
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-930：综合深水：构建器与运行时框架的协作边界——SSR 数据管道约定

**答**:
- 构建器与框架（Next/Nuxt 类）的职责切面：1) **框架管数据管道语义**（loader/action 的执行时机/去重/序列化）；2) **构建器管产物形态**（server bundle 的 external/ client 的 Flight 序列化边界/manifest 对齐 RBL-700）；3) 协作点在「约定」：路由 → 模块映射（构建器 glob 展开 RBL-627）、数据注入协议（html 里的序列化数据块——escape 安全 `</script` 转义）。
- 数据注入的安全细节：HTML 内嵌 JSON 的 XSS 向量（`</script><script>alert(1)` 闭合注入）——序列化必须转义（`<` → `\u003c`）——「内嵌数据的转义」是构建器/框架共同的契约点，漏转义 = 存储型 XSS。
- 协作的演进摩擦：框架每代升级改变约定（Pages Router → App Router）——构建器的「约定适配层」（每代框架一个 adapter，统一内部表示 RBL-826 schema 模式）。
- 数据管道的可观测：SSR 数据获取的 trace（每 loader 一个 span——慢 loader 定位）；「waterfall loader」（串行无依赖的 loader）的构建期 lint（并行化建议）。
- 追问钩子：为什么「内嵌 JSON 转义」是构建器与框架必须共同测试的契约点？——转义在数据流经多层（server 渲染 → 模板 → 序列化 → html）时最容易在某层丢失（框架升级换序列化器/构建器改动模板注入）；契约测试的形态是「恶意数据贯穿用例」（`</script>` payload 从 loader 到 html 全链路验证）——安全契约不能靠单层自觉，要靠贯穿测试锁定。

```javascript
// 数据注入的安全序列化
function serializeForHtml(data) {
  return JSON.stringify(data)
    .replace(/</g, '\\u003c')                            // </script> 闭合注入防护
    .replace(/-->/g, '--\\u003e')
    .replace(/\u2028|\u2029/g, (m) => '\\u202' + (m === '\u2028' ? '8' : '9'));  // 行终止符
}
// html 注入模板
const injection = `<script>window.__DATA__ = ${serializeForHtml(loaderData)}</script>`;
// 恶意数据贯穿测试
it('恶意 payload 全链路安全', async () => {
  const evil = { name: '</script><script>alert(1)</script>' };
  const html = renderWithData(evil);
  expect(html).not.toContain('</script><script>');
  expect(html).toContain('\\u003c/script\\u003e');       // 已转义
});
// waterfall loader lint
function auditLoaderWaterfall(loaders, deps) {
  const independent = loaders.filter(l => !deps[l.id]?.length);
  const serial = independent.filter((l, i) => i > 0);    // 无依赖却串行
  if (serial.length)
    warn(`loader ${serial.map(s => s.id)} 无依赖但串行——建议并行 await Promise.all`);
}
```
