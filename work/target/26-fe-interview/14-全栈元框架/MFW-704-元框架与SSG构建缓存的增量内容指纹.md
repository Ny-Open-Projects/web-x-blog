---
title: [MFW-704] SSG 构建缓存的内容指纹
date: 2026-11-22
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-704：SSG 构建缓存的内容指纹

**答**:
- SSG 内容指纹的设计（RBL-595 增量的键）：1) **源内容 hash**（Markdown 文件 content hash——内容变更检测）；2) **模板 hash**（组件/layout 的文件 hash——模板变更影响所有引用页 RBL-635 依赖闭包）；3) **数据 hash**（CMS API 数据的 hash——外部数据变更）；4) 组合指纹（source ⊕ template ⊕ data = 页面渲染指纹——任一变化 → 重渲染 RBL-582 最小完备键）。
- 指纹的存储：上次构建 manifest（.next/build-manifest 的 SSG 扩展：path → fingerprint）；「指纹的比对粒度」：页面级（每页一个指纹——细粒度增量）。
- 指纹的可靠性：hash 函数的碰撞（SHA256 碰撞概率可忽略）；「指纹的稳定性」：同内容同指纹（构建可复现 RBL-543——hash 输入不含时间戳/路径）。
- 追问钩子：为什么「SSG 指纹要包含模板 hash」而不只是内容 hash？——内容不变但模板变（改组件样式）→ 渲染结果变 → 页面需重渲染；只比对内容 = 模板变更漏检（静默旧渲染 RBL-956）；「指纹的最小完备性」（RBL-582）：影响渲染输出的所有输入都要参与指纹——源内容 + 模板 + 数据（漏一环 = 旧渲染漏检）——与构建缓存键（RBL-587）的完备性原则一致。

```typescript
// SSG 内容指纹
import { createHash } from 'crypto';
async function pageFingerprint(page: {
  content: string, component: string, data: unknown
}, { templateHash, dataHash } = {}) {
  const h = createHash('sha256');
  h.update(page.content);                                // 源内容
  h.update(templateHash ?? await hashFile(page.component));  // 模板
  h.update(dataHash ?? JSON.stringify(page.data));       // 外部数据
  return h.digest('hex').slice(0, 16);
}
// 增量构建 diff（RBL-595）
async function incrementalBuild(pages, lastManifest) {
  for (const p of pages) {
    const fp = await pageFingerprint(p);
    const prev = lastManifest[p.path];
    if (prev?.fingerprint === fp) continue;              // 未变更：跳过
    await render(p.path);                                // 变更：重渲染
    lastManifest[p.path] = { fingerprint: fp };
  }
}
// 指纹的稳定性：同内容同指纹
// hash 输入不含时间戳/构建路径——RBL-543 确定性
```
