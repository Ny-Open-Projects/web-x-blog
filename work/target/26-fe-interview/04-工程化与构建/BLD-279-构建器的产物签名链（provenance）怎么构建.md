---
title: [BLD-279] 产物签名链（provenance）怎么构建？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## BLD-279：provenance 怎么构建？
**答**：
- provenance 内容：「这个产物由哪次构建产生」的可验证陈述——commit/构建环境/输入清单（lockfile hash/配置 hash）/构建器版本——SLSA 供应链框架的构建级保障。
- 实现链：构建时生成 provenance JSON（输入清单+输出 hash）→ CI 用密钥签名（Sigstore/attestation）→ 发布时附带 → 消费端验证（npm provenance，SCN-ENG-233）。
- 验证链闭环：产物 hash ↔ provenance ↔ 源 commit——三层可互相验证（SCN-OPS-220 合规留痕的技术底座）。
- 追问钩子：为什么 provenance 要「输入清单」而不只是 commit——只有 commit 无法证明构建时用了什么依赖（lockfile 可能被改/缓存污染）；输入清单（依赖 hash+配置 hash）让「构建的完整输入集」可验证——这是「可复现构建」（SCN-ENG-222）与供应链审计的桥梁：可复现 = 同输入必同输出，provenance = 输入的公证。

```javascript
// 构建时生成 provenance
const provenance = {
  builder: { id: 'https://github.com/actions/runner', version },
  source: { commit: GIT_SHA },
  inputs: { lockfile: sha256(lockfile), config: sha256(config), env: declaredEnvs },
  outputs: manifest.allHashes(),
};
await sigstoreSign(provenance);                        // CI 密钥签名
// 消费端验证
verify(provenance) && verifyHash(artifact, provenance.outputs);
```
