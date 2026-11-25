---
title: [MFW-897] 怎么在 CI 做产物复现门禁：两次独立构建哈希一致性比对
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-897：怎么在 CI 做产物复现门禁：两次独立构建哈希一致性比对

**答**：
- 结论：在干净环境用相同输入独立构建两次，比对产物内容哈希（或 merkle 根）；不一致即判定构建非确定性，阻断发布。
- 落地：CI 并行跑两个隔离 job，归一化时间戳后算哈希；差异用 merkle 树定位到具体文件。
- 追问钩子：为什么要「独立环境」？——同一环境可能残留缓存，掩盖非确定性；隔离环境才能暴露真实漂移。

```javascript
async function reproducibilityGate(buildFn) {
  const [a, b] = await Promise.all([
    runInCleanEnv(buildFn),           // 独立环境 A
    runInCleanEnv(buildFn)            // 独立环境 B
  ]);
  const ha = merkleRoot(normalize(a)); // 归一化时间戳/路径
  const hb = merkleRoot(normalize(b));
  if (ha !== hb) {
    const diff = diffMerkle(a, b);     // 定位到具体文件
    throw new Error('构建不可复现，差异文件: ' + diff.join(', '));
  }
  return ha;
}
// 门禁失败 → 阻断发布，要求修复非确定性来源
```
