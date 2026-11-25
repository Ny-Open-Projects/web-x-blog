---
title: [RBL-693] 构建器与 CDN 的失效协同：预推清单、失效粒度与刷新风暴防护
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-693：构建器与 CDN 的失效协同：预推清单、失效粒度与刷新风暴防护

**答**:
- 发布链路中构建器的 CDN 责任：输出「预推清单」（全部产物 URL + 角色分级：必须预推的 entry/chunk、可惰性的低频资产）与「失效清单」（需刷新的 mutable 文件：index.html/manifest）。hash 产物永不失效（新 URL 直推），mutable 文件才走失效 API——失效配额昂贵（CDN 按次计费），粒度控制是成本工程。
- 预推 vs 用户首访回源：预推保证首访命中（尤其大促场景 RBL-686）；预推清单按重要性排序分批（P0 先推），避免「全量预推」打爆 CDN 入口配额。
- 刷新风暴防护：index.html 失效后所有用户回源拿新 html → 回源风暴；防护是「html 边缘缓存短 TTL（30s）+ stale-while-revalidate」替代主动失效——让 CDN 自己控制新鲜度，失效 API 只用于紧急纠正。
- 发布顺序契约：先推 hash 产物（CDN 全量就绪）→ 再失效/更新 html——顺序颠倒会出现「新 html 引旧 chunk 404」；构建器 manifest 里记录依赖顺序，发布工具按序执行。
- 追问钩子：为什么「失效是最后手段」？——失效是强一致的，但代价高且有延迟（全球边缘节点传播分钟级）；hash 命名 + immutable 语义让「发布」变成「纯新增」，失效天然免了——正确的产物设计让失效几乎不存在。

```javascript
// 发布编排（构建器 manifest 驱动）
async function publish(manifest, cdn) {
  // 1) P0 产物预推（entry/chunk）
  const p0 = manifest.files.filter(f => f.role === 'chunk' || f.role === 'entry-js');
  await cdn.pushBatch(p0, { priority: 1 });
  // 2) 惰性资产
  await cdn.pushBatch(manifest.files.filter(f => f.role === 'asset'), { priority: 5 });
  // 3) hash 产物无需失效；仅 mutable 文件走失效
  const mutable = manifest.files.filter(f => !f.hash);
  for (const f of mutable) await cdn.invalidate(f.name);   // html/manifest/robots
  // 4) 验证：抽查 P0 URL 的边缘状态
  const checks = await Promise.all(p0.slice(0, 5).map(f => cdn.probe(f.name)));
  if (checks.some(c => c.status !== 'fresh')) throw new Error('CDN 预推未生效，中止 html 切换');
  await cdn.commitHtml(manifest.indexHtml);                // 最后切 html
}
```
