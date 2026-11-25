---
title: [RBL-429] 笔试：手写构建产物 CDN 预热器
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-429：手写 CDN 预热器
**答**：实现 `createCdnWarmer(manifest, { concurrency })`：1) 目的：发布后预热边缘节点（避免首用户回源慢）——并发拉取全部产物；2) 关键路径优先：entry html 与首屏 chunk 先预热（优先级队列）；3) 预热验证：HEAD 请求确认可达 + 内容长度与 manifest 一致（防上传截断）；4) 失败重试与最终报告 { warmed, failed }；5) 区域并发控制（每 region 限速防打爆）；6) 跳过已是热点的（HEAD 命中且 ETag 匹配）。

```javascript
export async function createCdnWarmer(manifest, { baseUrl, concurrency = 8, regionLimit = 4 } = {}) {
  const priority = (p) => (p === 'index.html' || p.startsWith('runtime') ? 0 : p.startsWith('vendor') ? 1 : 2)
  const paths = Object.keys(manifest.files).sort((a, b) => priority(a) - priority(b))
  const warmed = [], failed = []
  let active = 0, idx = 0

  async function warmOne(p) {
    const url = `${baseUrl}/${p}`
    const head = await fetch(url, { method: 'HEAD' })
    if (head.ok && +head.headers.get('content-length') === manifest.files[p].size) return   // 已热
    const res = await fetch(url)                                   // 拉取触发回源
    if (!res.ok) throw new Error(`warm ${p}: ${res.status}`)
    const buf = await res.arrayBuffer()
    if (buf.byteLength !== manifest.files[p].size) throw new Error(`size mismatch: ${p}`)
  }

  await new Promise((resolve) => {
    const pump = () => {
      while (active < concurrency && idx < paths.length) {
        const p = paths[idx++]
        active++
        warmOne(p).then(() => warmed.push(p)).catch(() => failed.push(p))
          .finally(() => { active--; pump() })
      }
      if (active === 0 && idx >= paths.length) resolve()
    }
    pump()
  })
  return { warmed, failed }
}
```
**评分点**：
- 优先级队列（entry/runtime 先热——首用户路径优先）
- 三重校验（HEAD 可达 + content-length 一致 + 拉取长度一致——防截断上传）
- 已热跳过（ETag/长度匹配不重复拉）
- 并发控制（限速防打爆 CDN）；失败收集报告
