---
title: [RBL-145] SWC/Oxc 迁移落地的典型踩坑清单有哪些
date: 2026-11-19
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-145：SWC/Oxc 迁移落地的典型踩坑清单有哪些

**答**：
- 语法语义差异：装饰器两套语义（legacy vs 2022-03）选错导致依赖注入框架（NestJS/Nest 类）运行时 metadata 丢失；legacy class field 初始化顺序不同引发老代码 bug。
- output 差异：loose 模式、helper 注入方式（inline vs externalHelpers）、ESM/CJS interop 细节与 Babel 不一致，要用同一批回归用例做产物 diff。
- binding/平台问题：见 RBL-144——optional deps、musl/glibc、跨平台 CI 缓存。
- sourcemap：压缩后映射偏差，尤其 async/await 与压缩重排处；灰度期对异常上报栈做映射抽查。
- 工具链版本耦合：宿主（Next/Rspack）内置的 SWC 版本不可控，升级宿主可能改变转换行为；锁定宿主版本并建立快照测试。
- 追问钩子：迁移策略永远是"影子构建 + 产物对比 + 灰度"三步，不直接全量切换。

```javascript
// scripts/compare-output.mjs —— 影子构建产物对比核心逻辑
import { execSync } from 'node:child_process';
import { createHash } from 'node:crypto';
import { readdirSync, readFileSync } from 'node:fs';

function hashDist(dir) {
  const map = {};
  for (const f of readdirSync(dir, { recursive: true })) {
    if (!/\.(js|css|map)$/.test(f)) continue;
    const raw = readFileSync(`${dir}/${f}`);
    map[f.replace(/\.[a-f0-9]{8,}\./, '.HASH.')] = createHash('sha256').update(raw).digest('hex');
  }
  return map;
}
const a = hashDist('dist-babel');
const b = hashDist('dist-swc');
for (const k of new Set([...Object.keys(a), ...Object.keys(b)])) {
  if (a[k] !== b[k]) console.log('DIFF:', k); // 差异 chunk 进入人工审查清单
}
```
