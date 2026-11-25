---
title: [AIC-930] 笔试：实现「AI 产出溯源签名器」（内容哈希 + 元数据封装，随代码入库）
date: 2026-11-23
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-930：笔试：实现「AI 产出溯源签名器」（内容哈希 + 元数据封装，随代码入库）
**答**：
- 核心需求：实现 `signArtifact(code, meta)` 与 `verifyArtifact(envelope)`。`meta: { session, round, model, promptVersion, actor }`。返回信封 `{ payload, meta, hash, sig }`。
- hash = 对 `payload + 排序后的 meta` 计算稳定哈希（JSON 序列化时键要排序保证确定性）；sig 用简单 HMAC 风格（seed 密钥 + hash）模拟，验证时重算比对。
- verifyArtifact 要校验：① hash 与 payload/meta 是否匹配（防内容篡改）；② sig 是否正确（防元数据伪造）；返回 `{ valid, reasons }`。
- 边界：code 非字符串转 String；meta 缺失字段用 "unknown" 填充；键排序用 Object.keys().sort()；空 code 合法。
- 语义：这是「完整性签名」而非加密——保证产出与元数据未被改动，但不保证代码正确；密钥管理属于平台职责。
- 追问钩子：能指出「签名保证完整性不保证正确性，且密钥泄露会让签名失效」的候选人理解安全的边界。

```typescript
function stableStringify(o) {
  if (o === null || typeof o !== 'object') return JSON.stringify(o);
  if (Array.isArray(o)) return '[' + o.map(stableStringify).join(',') + ']';
  return '{' + Object.keys(o).sort().map(k => JSON.stringify(k)+':'+stableStringify(o[k])).join(',') + '}';
}
const KEY = 0x5eed;
function hash(s){ let h=0; for(const c of s) h=(Math.imul(h,31)+c.charCodeAt(0))>>>0; return h; }
function signArtifact(code, meta = {}) {
  const payload = String(code ?? '');
  const m = { session:'unknown', round:0, model:'unknown', promptVersion:'unknown', actor:'unknown', ...meta };
  const hashV = hash(stableStringify({ payload, meta:m }));
  const sig = hash(KEY + ':' + hashV);
  return { payload, meta:m, hash:hashV, sig };
}
function verifyArtifact(env) {
  const reasons = [];
  if (hash(stableStringify({ payload:env.payload, meta:env.meta })) !== env.hash) reasons.push('内容被篡改');
  if (hash(KEY + ':' + env.hash) !== env.sig) reasons.push('签名无效');
  return { valid: reasons.length === 0, reasons };
}
console.log(verifyArtifact(signArtifact('const x=1', {session:'s1'}))); // valid=true
```
**评分点**：
- stableStringify 对键排序，哈希确定可复现。
- signArtifact 用 meta 默认值填充，hash 与 sig 计算正确。
- verifyArtifact 分别校验内容篡改与签名伪造，reasons 清晰。
- 非字符串 code、空 code、缺失 meta 等边界处理完整。
- 能说明签名只保完整性不保正确性、密钥管理属平台职责（加分项）。
