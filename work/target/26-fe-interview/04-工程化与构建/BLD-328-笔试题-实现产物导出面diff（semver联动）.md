---
title: [BLD-328] 笔试题——实现产物导出面 diff（semver 联动）？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 笔试题, 工程化]
type: 笔试题
---

## BLD-328：手写导出面 diff

**需求与边界**：
- 需求：库产物导出面 diff（SCN-ENG-308 延伸）——① 产物级导出提取（从 d.ts/产物 AST——不是源码级）；② diff 分类（新增/删除/签名变化）；③ semver bump 建议（major = 删除/签名不兼容——SCN-ENG-308 联动）；④ 隐式导出变化（桶文件 re-export 链变化导致的导出消失）。
- 边界：① d.ts 与产物一致性（产物里实际导出的 vs d.ts 声明的——不一致告警）；② 类型级 diff（参数类型变化也是不兼容）；③ 输出带消费方影响（谁 import 了被删导出）。

**答**：
```javascript
function exportSurfaceDiff(oldDist, newDist, consumers) {
  const oldExports = extractExports(oldDist);          // 从 d.ts/产物 AST
  const newExports = extractExports(newDist);
  const dtsConsistent = sameExports(extractExports(newDist.dts), newExports.runtime);
  const diff = {
    added: [...newExports.keys()].filter(k => !oldExports.has(k)),
    removed: [...oldExports.keys()].filter(k => !newExports.has(k)),
    signatureChanged: [...oldExports.keys()].filter(k => newExports.has(k)
      && !sameSignature(oldExports.get(k), newExports.get(k))),
  };
  const bump = diff.removed.length || diff.signatureChanged.length ? 'major'
    : diff.added.length ? 'minor' : 'patch';
  const impacted = consumers.filter(c =>
    c.imports.some(i => diff.removed.includes(i.name)));   // 谁受影响
  return { diff, bump: { suggested: bump, reason: diff.removed.length ? '导出删除' : '签名变化' },
    dtsConsistent: dtsConsistent ? null : { warn: 'd.ts 与产物导出不一致' },
    impacted: impacted.map(c => ({ file: c.file, broken: c.imports.filter(i => diff.removed.includes(i.name)) })),
  };
}
```

**评分点**:
- 产物级导出提取（d.ts/AST——SCN-ENG-308 联动）。
- 三分类 + semver bump 建议（major/minor/patch 规则）。
- d.ts 与产物一致性校验（声明与实现不漂移）。
- 消费方影响分析（谁 import 了被删导出——影响面）。
