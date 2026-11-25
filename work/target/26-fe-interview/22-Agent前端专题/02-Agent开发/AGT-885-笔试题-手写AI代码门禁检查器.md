---
title: [AGT-885] 手写 aiGate：幻觉API检测（类型对照）、幻觉包检测、测试缺口、AI标记统计？
date: 2026-11-21
categories: [AI与Agent]
tags: [前端面试, 笔试题, Agent]
type: 笔试题
---

## AGT-885：手写 aiGate：幻觉API检测（类型对照）、幻觉包检测、测试缺口、AI标记统计

**需求与边界**：
- 实现 aiGate(pr, registry)。
- 边界要求：① 幻觉 API：AI 文件中调用的成员不在导出类型里即报（对照 registry 导出表）；② 幻觉包：imports 中包名不在 registry（npm 存在性）即报；③ 测试缺口：AI 文件无对应测试文件（__tests__ 同名）报缺口；④ 输出 { errors[], warnings[], aiRatio }；⑤ 非AI文件跳过检查。

**答**：
```javascript
function aiGate(pr, registry) {
  const aiFiles = pr.files.filter(f => f.aiGenerated);
  const errors = [], warnings = [];
  for (const f of aiFiles) {
    for (const imp of f.imports) {
      if (!registry.hasPackage(imp.pkg))
        errors.push({ file: f.path, kind: 'ghost-package', pkg: imp.pkg });
      for (const member of imp.usedMembers) {
        if (registry.hasPackage(imp.pkg)
          && !registry.exports(imp.pkg).includes(member))
          errors.push({ file: f.path, kind: 'ghost-api',
            pkg: imp.pkg, member });               // 幻觉API
      }
    }
    const testPath = f.path.replace(/\.tsx?$/,
      m => `__tests__/${f.name.replace(m, '')}.test${m}`);
    if (!registry.hasFile(testPath))
      warnings.push({ file: f.path, kind: 'test-gap' });
  }
  return { errors, warnings,
    aiRatio: aiFiles.length / Math.max(pr.files.length, 1) };
}
```

**评分点**:
- 幻觉包与幻觉 API 分开检测（包级先验证，成员级再验证，不误报）。
- 测试缺口按同名约定映射；非 AI 文件跳过（不对人类代码重复收费）。
- aiRatio 归因统计（长期质量追踪的基础）。

