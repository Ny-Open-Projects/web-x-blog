---
title: [MFW-878] 构建时长与 CI 成本怎么治理（增量构建 + 远程缓存命中率）
date: 2026-11-23
categories: [全栈元框架]
tags: [前端面试, 面试题, MFW]
type: 面试题
---

## MFW-878：构建时长与 CI 成本怎么治理（增量构建 + 远程缓存命中率）

**答**：
- 结论：构建成本 = 单次时长 × 次数；治理靠三招——远程缓存复用产物、增量构建只重算变更子图、按需选择验证范围，减少无效重跑。
- 落地：用内容哈希做缓存键（相同输入命中缓存）；依赖图驱动选择性构建；监控缓存命中率作为核心指标。
- 追问钩子：命中率是不是越高越好？——命中率 100% 可能是缓存键过粗（漏掉该重算的变更），需配合正确性校验。

```javascript
function cacheKey(pkg, inputs) {
  // inputs：源码哈希 + 依赖版本 + 环境变量（影响产物的都要入键）
  return stableHash({ pkg, inputs });
}
async function build(pkg) {
  const key = cacheKey(pkg, await collectInputs(pkg));
  if (await remoteCache.has(key)) return remoteCache.restore(key); // 命中复用
  const out = await runBuild(pkg);
  await remoteCache.save(key, out);
  return out;
}
// 命中率 = hits / (hits + misses)，配合「缓存键是否覆盖全部产物输入」校验
```
