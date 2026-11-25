---
title: [BLD-247] 构建产物上传 CDN 的编排怎么做的？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-247：产物上传编排怎么做？
**答**：
- 上传顺序：immutable 资源先传（hash 命名无冲突）→ HTML 最后切（SCN-OPS-209 发布流量顺序）——顺序错 = 用户拉到引用不存在资源的 HTML。
- 幂等与并发：同 hash 资源幂等（重复上传无害）、并发上传分片（大仓产物数万文件——并发池限流）。
- 校验闭环：上传后抽验（CDN 拉回比对 hash）+ manifest 与 CDN 对象集 diff（SCN-OPS-246 验签延伸）。
- 失败处理：部分上传失败的回滚（HTML 未切则无影响——天然原子性依赖「HTML 后切」顺序）。
- 追问钩子：为什么「HTML 最后切」让产物上传天然具备原子性——上传中途失败时，线上 HTML 仍指向旧 hash（旧资源还在 CDN）——用户完全无感；把「切换引用」这个原子动作留在最后一步，前面的资源上传就是可重试的幂等操作——顺序设计替代了分布式事务。

```javascript
async function publishToCdn(manifest) {
  await uploadAssets(manifest.assets, { concurrency: 20, idempotent: true });  // 1. 资源先传
  await verifyRoundtrip(manifest);                     // 2. 抽验 hash
  const missing = diff(manifest, cdnList());           // 3. 对象集 diff
  if (missing.length) throw new Error('上传不完整');
  await switchHtml(manifest);                          // 4. HTML 最后切（原子）
}
```
