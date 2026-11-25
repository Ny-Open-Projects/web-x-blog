---
title: [BLD-322] 笔试题——实现 provenance 生成与验证（签名链）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-322：手写 provenance

**需求与边界**：
- 需求：产物 provenance 的生成与验证（SCN-BLD-279）——① 生成（输入清单：commit/lockfile hash/配置 hash/env 声明 + 输出 hash 集）；② 签名（CI 密钥——Sigstore/本地密钥对）；③ 验证（签名验真 + 输入重算比对 + 输出 hash 重算）；④ 验证失败分类（签名伪造/输入漂移/产物篡改）。
- 边界：① 输入清单完整性（漏项 = 可被注入未声明输入）；② 验证的独立环境（验证器不信任生成环境）；③ 失败分类可审计（哪层断了——SCN-OPS-246 链路）。

**答**：
```javascript
async function generateProvenance(buildCtx, signKey) {
  const p = {
    builder: { id: BUILD_SYSTEM_ID, version: BUILD_TOOL_VERSION },
    source: { commit: buildCtx.commit },
    inputs: { lockfile: sha256(buildCtx.lockfile), config: sha256(buildCtx.config),
      env: buildCtx.declaredEnvs },                    // 输入清单完整性（漏项=注入面）
    outputs: Object.fromEntries(buildCtx.manifest.allFiles()
      .map(f => [f.path, f.hash])),
  };
  return { ...p, signature: sign(signKey, sha256(JSON.stringify(p))) };
}
async function verifyProvenance(p, pubKey, actualInputs, actualOutputs) {
  if (!verifySig(pubKey, p.signature, sha256(JSON.stringify(stripSig(p)))))
    return { verdict: 'FORGED' };                      // 签名伪造
  for (const [k, h] of Object.entries(p.inputs))
    if (sha256(actualInputs[k]) !== h) return { verdict: 'INPUT_DRIFT', input: k };   // 输入漂移
  for (const [f, h] of Object.entries(p.outputs))
    if (actualOutputs[f] !== h) return { verdict: 'ARTIFACT_TAMPERED', file: f };     // 产物篡改
  return { verdict: 'VALID' };                         // 三层链闭环（SCN-OPS-220）
}
```

**评分点**:
- 输入清单完整性（漏项即注入面——SCN-BLD-279 核心）。
- 三层验证（签名/输入重算/输出重算）与失败三分类（FORGED/INPUT_DRIFT/ARTIFACT_TAMPERED）。
- 验证器独立环境（不信任生成环境）。
- 与合规留痕闭环（SCN-OPS-246/220）。
