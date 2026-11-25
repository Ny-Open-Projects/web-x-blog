---
title: [ENG-288] 笔试题——实现 catalog（统一版本表）校验器？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## ENG-288：手写 catalog 校验器

**需求与边界**：
- 需求：校验全仓 package.json —— ① 引用 catalog: 的包必须在 catalog 表中；② 直接写版本号的依赖若存在于 catalog 表则违规（应统一走 catalog）；③ semver 区间与 catalog 实际版本兼容性检查。
- 边界：① 输出全部违规（按文件聚合）；② dev/peer 依赖同样校验；③ semver 兼容：catalog ^1.2.0 时依赖写 ^1.0.0 属于区间不匹配警告。

**答**：
```javascript
const semver = require('semver');
function validateCatalog(catalog, workspace) {
  const errors = [], warnings = [];
  for (const pkg of workspace) {
    for (const section of ['dependencies', 'devDependencies', 'peerDependencies']) {
      for (const [name, spec] of Object.entries(pkg[section] || {})) {
        if (spec === 'catalog:') {
          if (!(name in catalog))
            errors.push({ file: pkg.path, dep: name, code: 'CATALOG_MISSING' });  // 引用不存在
        } else if (name in catalog) {
          errors.push({ file: pkg.path, dep: name, spec, code: 'NOT_USING_CATALOG' });  // 应统一
        }
        if (spec.startsWith('^') || spec.startsWith('~')) {   // 区间兼容性
          const catVer = catalog[name];
          if (catVer && !semver.satisfies(catVer, spec))
            warnings.push({ file: pkg.path, dep: name, code: 'RANGE_MISMATCH',
                            catalog: catVer, spec });
        }
      }
    }
  }
  return { errors, warnings, ok: errors.length === 0 };
}
```

**评分点**:
- 双向校验（catalog: 缺表 + 有表不用）。
- 三类依赖段全覆盖（dev/peer 不漏）。
- semver 区间与 catalog 版本兼容警告。
- 输出按文件聚合（批量修复可导航）。
