---
title: [MFW-642] Flight 流与 HTML 壳的一致性 CI
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-642：Flight 与 HTML 一致性 CI

**答**:
- 双流一致性的 CI 断言（RBL-700 的流式版）：1) **边界 ID 对齐**（HTML 的 `<!--$?-->` 模板 id = Flight 的 chunk id——错配 = 注入错位置 RBL-507）；2) **内容语义一致**（HTML 壳的内容 ⊆ Flight 树的内容——壳是树的子集）；3) **fallback 一致**（Suspense fallback 的 HTML = Flight 的 fallback 分支）。
- CI 的实现：双请求对比（一次拿 HTML 流、一次拿 RSC payload（Accept: text/x-component）——「HTML 壳的内容」与「Flight 树的对应部分」语义指纹 diff（RBL-794 双渲染的流式版）。
- 抖动的容忍：动态内容（时间戳）——指纹的规范化（RBL-794 语义指纹：忽略时间/随机）；抽样路由 × 状态（RBL-794 分层抽样）。
- 追问钩子：为什么「HTML 壳与 Flight 的边界对齐」错配是「最难排查的静默错」？——错配的表现 = 异步内容注入到错误的占位（A 边界的内容进了 B 的位置——UI 错乱但无报错）；根因在「构建期的 ID 生成」（编译器给边界编号——重构后编号漂移）；「双流协议的 ID 契约」只有 CI 对比才能验证（单看 HTML 或单看 payload 都看不出——错配是「两者之间」的关系）；一致性 CI 是双流架构的验收底线（RBL-656 闭合校验的流式版）。

```javascript
// CI：双流一致性检查
async function verifyStreamConsistency(url, { fetchFn = fetch } = {}) {
  // 1) HTML 流（含边界占位）
  const html = await fetchFn(url, { headers: { accept: 'text/html' } }).then(r => r.text());
  // 2) Flight payload
  const flight = await fetchFn(url, { headers: { accept: 'text/x-component' } }).then(r => r.text());
  // 3) 边界 ID 对齐
  const htmlBoundaries = [...html.matchAll(/template id="B:([A-Z0-9]+)"/g)].map(m => m[1]);
  const flightBoundaries = [...flight.matchAll(/S(\d+):/g)].map(m => m[1]);
  const missing = htmlBoundaries.filter(id => !flightBoundaries.includes(id));
  if (missing.length)
    throw new Error(`边界错配: HTML ${htmlBoundaries.length} vs Flight ${flightBoundaries.length}, missing=${missing}`);
  // 4) 语义指纹（shell 内容 ⊆ Flight 树）
  const shellFp = semanticFingerprint(stripScripts(html));
  const flightFp = semanticFingerprint(flight);
  if (!flightFp.includes(shellFp.slice(0, 100)))       // 粗对齐：shell 是子集
    warn('shell 内容与 Flight 树语义不一致——检查双渲染数据源');
  return { boundaries: htmlBoundaries.length, ok: true };
}
```
