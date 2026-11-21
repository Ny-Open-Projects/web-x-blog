---
title: [RBL-101] 笔试：手写模块指纹生成器（内容 + 环境 + 配置联合 hash）
date: 2026-11-18
categories: [Rust系构建工具]
tags: [前端面试, 笔试题, RBL]
type: 笔试题
---

## RBL-101：笔试：手写模块指纹生成器（内容 + 环境 + 配置联合 hash）
**题目**：实现 fingerprint(file, ctx)：1) 指纹 = sha256(内容 + 环境指纹 + 相关配置切片)；2) 环境指纹取 { node 版本, env 关键变量, 平台 } 的稳定序列化；3) 相关配置切片：按文件类型取该类文件生效的配置（如 ts 文件取 transformer 配置），无关配置变更不失效；4) 同内容同环境同配置 → 指纹相同（幂等）；5) 任意一项变更 → 指纹变化（缓存正确失效的根基）。

```javascript
const crypto = require('crypto'), fs = require('fs');

function fingerprint(file, ctx = {}) {
  const content = fs.readFileSync(file);
  const { env = {}, config = {}, nodeVersion = process.version, platform = process.platform } = ctx;

  // 1) 环境指纹：键排序后稳定序列化（保证幂等）
  const envKey = JSON.stringify(env, Object.keys(env).sort());

  // 2) 配置切片：按文件类型取相关配置
  const ext = path.extname(file);
  const slice = configByExt(ext, config);
  const configKey = JSON.stringify(slice, sortKeysReplacer);

  // 3) 联合 hash
  return crypto.createHash('sha256')
    .update(content)
    .update(envKey)
    .update(configKey)
    .update(nodeVersion)
    .update(platform)
    .digest('hex');
}

function configByExt(ext, config) {
  if (/\.tsx?$/.test(ext)) return { transformer: config.transformer };
  if (/\.css$/.test(ext)) return { postcss: config.postcss };
  return { javascript: config.javascript };
}
const sortKeysReplacer = (k, v) =>
  v && typeof v === 'object' && !Array.isArray(v)
    ? Object.fromEntries(Object.entries(v).sort(([a], [b]) => a.localeCompare(b)))
    : v;
module.exports = { fingerprint };
```
**评分点**：
- 联合 hash 覆盖内容+环境+配置三要素（缓存正确性根基）。
- 键排序序列化保证幂等（同输入必同指纹）。
- 配置按文件类型切片（无关配置变更不误伤缓存——精细失效）。
- nodeVersion/platform 纳入（跨机缓存正确性）。
- 能讲出漏掉隐式输入（如 env）会产出脏缓存的实例。
