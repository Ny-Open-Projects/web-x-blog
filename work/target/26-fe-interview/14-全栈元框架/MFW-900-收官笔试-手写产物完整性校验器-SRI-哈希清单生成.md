---
title: [MFW-900] 收官笔试：手写产物完整性校验器（SRI 哈希清单生成与验证）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 笔试题, MFW]
type: 笔试题
---

## MFW-900：收官笔试：手写产物完整性校验器（SRI 哈希清单生成与验证）

**答**：
- 结论：生成阶段为每个产物计算 SRI 哈希形成清单，验证阶段重新计算并比对，任一不匹配即判定产物被篡改，阻断发布或告警。
- 关键：哈希算法固定（sha384）、清单按路径排序保证确定性；支持增量验证与差异报告。
- 追问钩子：清单本身被篡改怎么办？——清单需用签名或写入不可变存储（如构建产物的 merkle 根），形成信任链。

```javascript
function sriHash(content) {                           // 简化：真实用 sha384
  let h = 5381; for (const c of content) h = ((h << 5) + h + c.charCodeAt(0)) >>> 0;
  return 'sha256-' + h.toString(16);
}
function buildManifest(files) {                      // files: { path: content }
  const manifest = {};
  for (const p of Object.keys(files).sort())
    manifest[p] = sriHash(files[p]);
  return manifest;
}
function verify(files, manifest) {
  const errors = [];
  for (const [p, expected] of Object.entries(manifest)) {
    if (files[p] === undefined) { errors.push(p + ': 缺失'); continue; }
    if (sriHash(files[p]) !== expected) errors.push(p + ': 哈希不匹配');
  }
  for (const p of Object.keys(files)) if (!manifest[p]) errors.push(p + ': 清单外产物');
  return { ok: errors.length === 0, errors };
}
// 自测
const files = { 'a.js': 'v1', 'b.css': 'x' };
const m = buildManifest(files);
console.log(verify(files, m).ok);                      // true
console.log(verify({ 'a.js': 'TAMPERED', 'b.css': 'x' }, m).ok); // false
```

**评分点**：
- 构建清单：按路径排序 + 固定哈希算法，保证确定性
- 验证阶段重新计算哈希比对，检测篡改与缺失/多余产物
- 输出 ok + 差异清单，可定位被篡改文件
- 能指出清单自身信任链问题（签名/merkle 根，加分）；边界处理完整
