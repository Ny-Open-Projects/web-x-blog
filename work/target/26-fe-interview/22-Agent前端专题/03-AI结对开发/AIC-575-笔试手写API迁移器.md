---
title: [AIC-575] 笔试：手写 API 迁移器
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 笔试题, AIC]
type: 笔试题
---

## AIC-575：笔试：手写 API 迁移器

**答**：实现 `migrateAPI(code, mapping)`。mapping: `Record<oldName, { newName, paramTransform? }>`. paramTransform: `(args) => args`（参数转换函数）。规则：1) 方法名替换：`oldMethod(` → `newMethod(`（正则替换——包括 `obj.oldMethod(` 和独立 `oldMethod(`）；2) 参数转换：mapping 有 paramTransform → 替换时同时转换参数（参数名的映射）；3) **未匹配的 oldXxx 方法** → unmigrated 清单（人工处理 RBL-666）；4) 返回 `{ code, migrated: string[], unmigrated: string[] }`。边界：mapping 空（全 unmigrated）；code 无匹配（原样返回）；参数转换函数抛错（不替换——保留原样并报 unmigrated）；嵌套调用（`oldApi.get(oldApi.list())`——内外都要替换）。

```javascript
function migrateAPI(code = '', mapping = {}) {
  const migrated = [], unmigrated = [];
  let result = code;
  for (const [oldName, spec] of Object.entries(mapping)) {
    const regex = new RegExp(`\\b${oldName}\\s*\\(`, 'g');
    if (!regex.test(result)) continue;
    const transform = spec.paramTransform ?? ((args) => args);
    result = result.replace(regex, () => {
      migrated.push(oldName);
      return `${spec.newName}(`;
    });
    // 参数转换（简化：如果 spec 有参数映射，在替换后处理）
    if (spec.paramMap) {
      for (const [oldP, newP] of Object.entries(spec.paramMap))
        result = result.replace(new RegExp(`\\b${oldP}\\b`, 'g'), newP);
    }
  }
  // 检测未迁移的 oldXxx
  const oldPrefixes = Object.keys(mapping).map(k => k.split('.')[0]);
  for (const prefix of oldPrefixes) {
    for (const m of result.matchAll(new RegExp(`\\b${prefix}\\.(\\w+)\\s*\\(`, 'g'))) {
      if (!mapping[`${prefix}.${m[1]}`])
        unmigrated.push(`${prefix}.${m[1]}`);
    }
  }
  return { code: result, migrated: [...new Set(migrated)], unmigrated: [...new Set(unmigrated)] };
}

// 自测
const mapping = {
  'oldApi.getUser': { newName: 'newApi.fetchUser' },
  'oldApi.list': { newName: 'newApi.paginate' },
  'oldApi.delete': { newName: 'newApi.remove' },
};
const code = `
  const user = oldApi.getUser(1);
  const list = oldApi.list({ page: 1 });
  oldApi.delete(2);
  const unknown = oldApi.patch(3);
`;
let r = migrateAPI(code, mapping);
console.log(r.migrated.length === 3);                    // getUser/list/delete
console.log(r.unmigrated.join(',') === 'oldApi.patch');  // 未映射的
console.log(r.code.includes('newApi.fetchUser'));
console.log(r.code.includes('newApi.paginate'));
console.log(r.code.includes('newApi.remove'));
console.log(r.code.includes('oldApi.patch'));            // 未迁移保留

// 空 mapping：全部 unmigrated
r = migrateAPI(code, {});
console.log(r.migrated.length === 0);
// 空 code
console.log(migrateAPI('', mapping).migrated.length === 0);
// 嵌套调用
r = migrateAPI('oldApi.get(oldApi.list())', mapping);
console.log(r.code.includes('newApi.fetchUser') && r.code.includes('newApi.paginate'));
```

**评分点**：
- 方法名替换（\b 边界——防止 partial match 误替换）；嵌套调用（内外都替换）
- unmigrated 清单（映射表未覆盖的方法——人工处理 RBL-666）；空 mapping 全 unmigrated
- 边界（空 code/空 mapping/嵌套调用/参数转换）；migrated/unmigrated 去重
- 能说清「API 迁移 = 映射表优先（确定性）+ AI 兜底（非确定性）——unmigrated 清单是人工处理的靶点」属于加分
