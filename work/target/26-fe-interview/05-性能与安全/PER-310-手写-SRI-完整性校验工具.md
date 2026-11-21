---
title: [PER-310] 笔试题：手写 SRI 生成与校验工具（构建期算哈希 + 运行时校验 fallback + manifest 对账）
date: 2026-11-19
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-310：笔试题：手写 SRI 生成与校验工具（构建期算哈希 + 运行时校验 fallback + manifest 对账）

**题目**：实现一个工具模块：① Node 侧 `genIntegrity(filePath, alg='sha384')` 读文件字节生成 integrity 字符串（base64）；② `generateManifest(distDir)` 扫描 js/css 产物生成 `{ file: integrity }` 清单；③ 浏览器侧 `loadWithFallback(src, integrity, onError)`：注入带 integrity 的 script，失败（SRI 校验失败/404）时上报事件并按策略重试一次；④ manifest 对账函数 `verifyManifest(manifest, cdnFetch)`：并发校验 CDN 字节哈希与清单一致，返回失败清单。

**答**：考点是 crypto 用法、字节级一致意识（哈希对象是线上响应字节）与失败路径。

```javascript
// ---------- Node 侧 ----------
const { createHash } = require('crypto');
const fs = require('fs'); const path = require('path');

function genIntegrity(filePath, alg = 'sha384') {
  const h = createHash(alg);
  h.update(fs.readFileSync(filePath));               // 原始字节，不做任何转换
  return `${alg}-${h.digest('base64')}`;
}
function generateManifest(distDir, exts = ['.js', '.css']) {
  const manifest = {};
  const walk = (dir) => {
    for (const f of fs.readdirSync(dir, { withFileTypes: true })) {
      const p = path.join(dir, f.name);
      if (f.isDirectory()) walk(p);
      else if (exts.includes(path.extname(f.name))) manifest[f.name] = genIntegrity(p);
    }
  };
  walk(distDir);
  return manifest;
}

// ---------- 浏览器侧 ----------
function loadWithFallback(src, integrity, onError) {
  return new Promise((resolve, reject) => {
    const s = document.createElement('script');
    s.src = src; s.integrity = integrity; s.crossOrigin = 'anonymous'; s.async = true;
    let retried = false;
    s.onerror = (e) => {
      onError?.({ src, phase: retried ? 'final' : 'first', type: e.type });
      if (!retried) { retried = true; s.remove();    // 重试一次（弱网/CDN 抖动）
        setTimeout(() => { const s2 = s.cloneNode(); s2.onload = resolve; s2.onerror = reject; document.head.append(s2); }, 300);
      } else reject(new Error(`SRI/load failed: ${src}`));
    };
    s.onload = () => resolve(src);
    document.head.append(s);
  });
}
async function verifyManifest(manifest, cdnFetch) {
  const failures = [];
  await Promise.all(Object.entries(manifest).map(async ([file, expected]) => {
    const bytes = await cdnFetch(file).arrayBuffer();
    for (const alg of ['sha384']) {
      const h = createHash(alg); h.update(Buffer.from(bytes));
      if (`${alg}-${h.digest('base64')}` !== expected) failures.push(file);
    }
  }));
  return failures;    // 非空 => 发布中止（CDN 字节被篡改或管线错配）
}
```

**评分点**：
- 哈希对象是"原始字节"，digest base64 与 `alg-` 前缀格式正确。
- manifest 扫描递归目录、只收 js/css。
- loadWithFallback 重试有限次并上报阶段（first/final），crossOrigin=anonymous 同配。
- verifyManifest 并发校验且失败清单可直接阻断发布。
