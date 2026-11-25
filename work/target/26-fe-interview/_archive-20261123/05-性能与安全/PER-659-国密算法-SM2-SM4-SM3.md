---
title: [PER-659] 国密算法（SM2/SM4/SM3）在前端的接入场景、库选择与 HTTPS 双栈共存方案
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 面试题, 09]
type: 面试题
---

## PER-659：国密算法（SM2/SM4/SM3）在前端的接入场景、库选择与 HTTPS 双栈共存方案

**答**：
- 三件套分工：SM2（非对称，对应 RSA/ECDH，签名+密钥交换）、SM4（对称分组，对应 AES，需自己管 IV/填充）、SM3（哈希，对应 SHA-256）——等保/关基场景政策要求国密时接入。
- 前端实现选择：WebCrypto 标准不支持国密，用纯 JS 库（sm-crypto）性能一般，或 WASM 编译的 C 实现（性能好 10 倍+）；签名验签在交互频繁场景建议移到 Worker。
- 双栈共存：服务端网关按客户端能力协商（TLS 国密双证书 + 应用层国密可选 header），前端按 UA/配置决定走国密或标准算法；灰度期两套并存，指标（错误率/耗时）分桶对比。
- 实务坑：SM4 默认 ECB 模式不安全（要用 CBC/GCM 语义的自实现）；SM2 签名的DER/裸格式转换（r||s 拼接 vs ASN.1）与服务端对齐——这是联调最高频的坑。

```javascript

import { sm2, sm4, sm3 } from 'sm-crypto';
// 双栈协商 + 国密封装示例
const ALGOS = { gm: { enc: sm4Encrypt, sign: sm2Sign }, std: { enc: aesEncrypt, sign: hmacSign } };
function pickAlgo() {
  if (window.__COMPLIANCE_MODE === 'gm' && wasmSmReady()) return 'gm';  // 政策要求
  return 'std';                                                 // 默认标准
}
async function gmSeal(plaintext, sm4KeyHex, serverPubKey) {
  const iv = randomHex(16);                                     // SM4-CBC 自管 IV
  const ct = sm4.encryptHexWithCBC(plaintext, sm4KeyHex, iv);
  const wrappedKey = sm2.doEncrypt(sm4KeyHex, serverPubKey, 1); // SM2 包裹会话钥
  const sig = sm2.doSignature(ct + iv, clientPrivKey, { hash: true });  // 完整性签名
  return { mode: 'gm', k: wrappedKey, iv, c: ct, sig };         // r||s 裸格式与服务端对齐
}
// 联调对齐清单：SM4 模式(CBC/GCM自实现) / SM2 签名格式(DER vs r||s) / 密钥 hex 编码大小写
```
