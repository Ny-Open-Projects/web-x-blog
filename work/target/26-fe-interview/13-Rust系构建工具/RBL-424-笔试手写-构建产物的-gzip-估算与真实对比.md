---
title: [RBL-424] 笔试：手写 gzip/brotli 体积估算与校准
date: 2026-11-20
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-424：手写 gzip/brotli 体积估算与校准
**需求**：实现 `createSizeEstimator()`：1) `real(content)`：真实 gzip(level 6) 与 brotli(q5) 压缩（node zlib）；2) `estimate(content)`：无压缩库场景的启发式估算（按字符分布：重复度高的 JSON/文本压缩率好——基于 token 频率熵的近似）；3) `calibrate(samples)`：用真实压缩结果校准估算系数（估算/真实比率回归）；4) `compare(a, b)`：两产物压缩后 diff（体积门禁用真实值）；5) 预算口径：预算以真实 gzip 为准，估算仅用于「写代码时快速心算」。

```javascript
import zlib from 'node:zlib'

export function createSizeEstimator() {
  function real(content) {
    const buf = Buffer.isBuffer(content) ? content : Buffer.from(content)
    return {
      raw: buf.length,
      gzip: zlib.gzipSync(buf, { level: 6 }).length,
      brotli: zlib.brotliCompressSync(buf, { params: { [zlib.constants.BROTLI_PARAM_QUALITY]: 5 } }).length,
    }
  }

  function estimate(content) {                        // 启发式：字符重复度熵
    const s = typeof content === 'string' ? content : String(content)
    const freq = new Map()
    for (const ch of s) freq.set(ch, (freq.get(ch) ?? 0) + 1)
    let entropy = 0
    for (const count of freq.values()) {
      const p = count / s.length
      entropy -= p * Math.log2(p)
    }
    // 经验：JS 源码熵约 4.5-5.5 → 压缩率约 3-4x；低熵（重复 JSON）更高
    const ratio = Math.max(2, Math.min(6, 8.2 / Math.max(entropy, 1)))
    return { raw: s.length, gzip: Math.round(s.length / ratio) }
  }

  function calibrate(samples) {                       // [{ raw, estGzip, realGzip }]
    const ratios = samples.map((s) => s.realGzip / s.estGzip)
    const mean = ratios.reduce((a, b) => a + b, 0) / ratios.length
    return { calibrationFactor: +mean.toFixed(3), samples: samples.length }   // est × factor ≈ real
  }

  return { real, estimate, calibrate }
}
```
**评分点**：
- 真实压缩双算法（gzip level6 / brotli q5——预算口径必须真实）
- 熵启发式估算（字符熵→压缩率映射，经验系数声明）
- calibrate 校准闭环（估算系数由真实样本回归——估算不是拍脑袋）
- 口径纪律：门禁用真实值，估算仅心算——口径声明是关键
