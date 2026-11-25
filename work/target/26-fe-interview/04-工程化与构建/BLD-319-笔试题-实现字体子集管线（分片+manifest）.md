---
title: [BLD-319] 笔试题——实现字体子集管线（分片 + manifest）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-319：手写字体子集管线

**需求与边界**：
- 需求：字体子集化管线（SCN-BLD-228/ENG-310）——① 字符集收集（源码扫描 + 动态字典输入）；② 分片生成（unicode-range 按段切——pyftsubset 调用）；③ manifest 产出（range → hash 文件映射）；④ CSS 生成（@font-face unicode-range 逐段声明）。
- 边界：① 码点级扫描（surrogate pair——SCN-ENG-310）；② 动态字典纳入（服务端文案——覆盖盲区）；③ 分片数与单片大小的平衡（太多片 = 请求碎片化）。

**答**：
```javascript
import { execSync } from 'child_process';
function fontSubset(ttf, charSources, dynamicDicts, { maxSlices = 60 } = {}) {
  // 1. 码点级收集
  const cps = new Set();
  for (const src of [...charSources, ...dynamicDicts])
    for (const ch of src) cps.add(ch.codePointAt(0));
  // 2. 分段（unicode-range 标准段——CJK 统一表意分段）
  const ranges = planRanges(cps, { maxSlices });       // 平衡分片数与单片大小
  // 3. 子集生成
  const manifest = ranges.map(([lo, hi]) => {
    const out = `noto-${lo.toString(16)}.woff2`;
    execSync(`pyftsubset ${ttf} --unicodes=U+${lo.toString(16)}-${hi.toString(16)} ` +
      `--flavor=woff2 --output-file=${out}`);
    return { range: `U+${lo.toString(16)}-${hi.toString(16)}`, file: out,
      hash: sha256(fs.readFileSync(out)).slice(0, 8) };
  });
  // 4. CSS 生成
  const css = manifest.map(m => `@font-face { font-family: 'Noto';
  src: url('${m.file}') format('woff2'); unicode-range: ${m.range}; font-display: swap; }`).join('\n');
  return { manifest, css };                            // 覆盖校验（SCN-ENG-310）
}
```

**评分点**:
- 码点级收集 + 动态字典输入（覆盖盲区——SCN-ENG-310）。
- 分片平衡（maxSlices——请求碎片化防御）。
- manifest 产出（range→hash——SCN-BLD-240 契约）。
- CSS 逐段 @font-face（unicode-range 按需下载——SCN-BLD-228）。
