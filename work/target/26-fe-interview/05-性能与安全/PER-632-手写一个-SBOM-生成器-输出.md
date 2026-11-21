---
title: [PER-632] 手写一个 SBOM 生成器：输出 CycloneDX 格式的前端依赖清单用于安全审计与应急排查
date: 2026-11-20
categories: [性能与安全]
tags: [前端面试, 笔试题, 09]
type: 笔试题
---

## PER-632：手写一个 SBOM 生成器：输出 CycloneDX 格式的前端依赖清单用于安全审计与应急排查

**答**：
- SBOM（软件物料清单）回答我们到底用了哪些组件、什么版本：CVE 爆出时用它秒查影响面；格式用 CycloneDX JSON（bomFormat/components）。
- 实现要点：读 lockfile（package-lock v3 的 packages 字段含 resolved 版本）；组件条目含 name/version/purl（pkg:npm/xxx@1.2.3）；区分应用自身与依赖；dev 与 prod 依赖分层（runtime 暴露面不同）。
- 边界：嵌套依赖按锁文件全量输出（不只 direct）；生成要进 CI 并归档，作为发版产物的一部分。
- 评分点：purl 格式与 dev/prod 分层。

```javascript

const fs = require('fs');
function genSBOM(pkgJson, lockFile) {
  const lock = JSON.parse(fs.readFileSync(lockFile, 'utf8'));
  const comps = Object.entries(lock.packages ?? {})
    .filter(([k]) => k.startsWith('node_modules/'))
    .map(([k, v]) => {
      const name = k.replace(/^node_modules\//, '').replace(/.*node_modules\//, ''); // 去嵌套前缀
      return {
        type: 'library', name, version: v.version,
        purl: `pkg:npm/${name}@${v.version}`,
        scope: v.dev ? 'excluded' : 'required',           // dev 依赖暴露面分层
      };
    });
  const bom = {
    bomFormat: 'CycloneDX', specVersion: '1.4',
    metadata: { component: { type: 'application', name: pkgJson.name, version: pkgJson.version } },
    components: comps,
  };
  fs.writeFileSync('sbom.json', JSON.stringify(bom, null, 2));
  return comps.length;
}
// 应急用法：CVE 公告 -> jq 查 sbom.json 是否含受影响版本 -> 秒级定位影响面
```
