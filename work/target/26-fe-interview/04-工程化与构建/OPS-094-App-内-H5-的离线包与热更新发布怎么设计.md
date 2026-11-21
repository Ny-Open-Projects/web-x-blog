---
title: [OPS-094] App 内 H5 的离线包与热更新发布怎么设计？
date: 2026-11-17
categories: [运维与上线]
tags: [前端面试, 面试题, 16]
type: 面试题
---

## OPS-094：App 内 H5 的离线包与热更新发布怎么设计？
**答**：
- 离线包：把 H5 的静态资源打成 zip 包，App 启动/空闲时预下载缓存，H5 请求命中本地拦截（自定义 scheme/拦截器），实现秒开与弱网可用。
- 版本机制：App 内置兜底版本 + 服务端增量下发新版本；manifest 记录文件清单与 hash，下载后校验完整性再原子切换。
- 热更新应急：线上 H5 出问题，可下发"紧急回滚到指定离线包版本"指令，比 App 发版快得多。
- 注意与常规发布的协同：离线包发布也走 CI，包体积有上限（App 预留空间），灰度按 App 版本+用户维度。

```javascript
// offline-package-manifest.js：离线包 manifest 生成与端上更新逻辑（Node 侧生成 + H5 侧约定）
import { createHash } from 'node:crypto';
import { createWriteStream } from 'node:fs';
import { readdir, stat, readFile, writeFile } from 'node:fs/promises';
import { join } from 'node:path';

async function* walk(dir) {
  for (const f of await readdir(dir, { withFileTypes: true })) {
    const p = join(dir, f.name);
    if (f.isDirectory()) yield* walk(p); else yield p;
  }
}

// 1. 构建 CI 中生成 manifest：文件清单 + sha256，供端上校验
export async function genManifest(distDir, version) {
  const files = {};
  for await (const p of walk(distDir)) {
    const buf = await readFile(p);
    files[p.replace(distDir + '/', '')] = {
      hash: createHash('sha256').update(buf).digest('hex'),
      size: buf.length,
    };
  }
  const manifest = {
    version,                       // 语义化：2.3.1
    minAppVersion: '8.2.0',        // 兼容的最低 App 版本
    fallbackVersion: '2.2.9',      // 异常时端上可回退的版本
    totalSize: Object.values(files).reduce((s, f) => s + f.size, 0),
    files,
    emergencyRollback: false,      // 应急置 true 时端上回退到 fallbackVersion
  };
  await writeFile(join(distDir, 'manifest.json'), JSON.stringify(manifest, null, 2));
  console.log('manifest generated:', manifest.version, manifest.totalSize, 'bytes');
}

// 2. 端上 H5 侧约定（App WebView 拦截 /offline/ 前缀请求走本地缓存）：
//    请求 /offline/2.3.1/assets/app.js -> App 校验 hash -> 返回本地文件
//    未命中或校验失败 -> 透传线上 CDN，保证永远有兜底
```
