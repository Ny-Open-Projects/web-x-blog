---
title: [RBL-796] 笔试：手写 sourcemap 上传时序守卫（上传先行 + 绑定校验 + 阻断发布）
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-796：笔试：手写 sourcemap 上传时序守卫（绑定校验 + 阻断）

**需求**：实现 `ensureMapsUploaded(manifest, uploader, { timeoutMs })`。manifest: `{ buildId, files: Array<{ name, map?: string }> }`（map 字段为 sourcemap 内容）。规则：1) 收集全部带 map 的文件上传（release = buildId）；2) 校验每个已上传文件的「绑定成功」响应（uploader.upload 返回 { file, accepted, reason? }）；3) 任一未 accepted → 抛错列出失败清单（阻断发布）；4) 超时未完成（timeoutMs）→ 抛 'upload-timeout'；5) 返回 `{ uploaded: string[], buildId }`。边界：无 map 文件（直接通过）；部分成功。

```javascript
async function ensureMapsUploaded(manifest, uploader, { timeoutMs = 30000 } = {}) {
  const maps = manifest.files.filter(f => f.map);
  if (!maps.length) return { uploaded: [], buildId: manifest.buildId };

  const results = await Promise.race([
    Promise.all(maps.map(f =>
      uploader.upload({ release: manifest.buildId, file: f.name, content: f.map })
        .then(r => ({ ...r, file: f.name })))),
    new Promise((_, rej) => setTimeout(() => rej(new Error('upload-timeout')), timeoutMs)),
  ]);

  const failed = results.filter(r => !r.accepted);
  if (failed.length)
    throw new Error(`sourcemap 绑定失败，中止发布: ${failed.map(f => `${f.file}(${f.reason ?? 'rejected'})`).join(', ')}`);
  return { uploaded: results.map(r => r.file), buildId: manifest.buildId };
}

// 自测
// 1) 全部成功
const manifest = {
  buildId: 'b-777',
  files: [
    { name: 'main.js', map: '{"m":1}' },
    { name: 'chunk.js', map: '{"m":2}' },
    { name: 'logo.png' },
  ],
};
let r = await ensureMapsUploaded(manifest, {
  upload: async ({ file }) => ({ accepted: true }),
});
console.log(r.uploaded.sort().join(','));                // chunk.js,main.js
console.log(r.buildId === 'b-777');

// 2) 部分失败 -> 抛错
let e; try {
  await ensureMapsUploaded(manifest, {
    upload: async ({ file }) => file === 'chunk.js' ? { accepted: false, reason: 'size-limit' } : { accepted: true },
  });
} catch (x) { e = x; }
console.log(/中止发布/.test(e.message) && e.message.includes('chunk.js') && e.message.includes('size-limit'));

// 3) 超时
e = null; try {
  await ensureMapsUploaded(manifest, {
    upload: () => new Promise(() => {}),                 // 永挂
  }, { timeoutMs: 50 });
} catch (x) { e = x; }
console.log(e.message === 'upload-timeout');

// 4) 无 map
r = await ensureMapsUploaded({ buildId: 'b-1', files: [{ name: 'x.png' }] }, { upload: async () => ({ accepted: true }) });
console.log(r.uploaded.length === 0);
```

**评分点**：
- 上传与 release=buildId 绑定正确；部分失败聚合报错且阻断（列出失败清单与原因）
- 超时竞速实现（Promise.race）；无 map 文件直接通过
- 能说清「上传先于发布的顺序契约——断链窗口内的错误反解全部失败」属于加分
