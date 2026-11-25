---
title: [AIC-574] AI 辅助 API 版本升级自动化
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-574：AI 辅助 API 升级自动化

**答**:
- AI 辅助 API 升级（v1→v2）：1) **影响面分析**（API 变更 → 受影响的调用点（AI 扫描代码库——找出所有调用旧 API 的位置 RBL-946 推理链）；2) **自动迁移**：AI 生成迁移代码（旧 API → 新 API 的适配代码——RBL-666 配置翻译的代码版）；3) **迁移验证**：迁移前后行为一致（RBL-667 双栈对拍——旧 API 输出 = 新 API 输出）；4) **渐进迁移**：共存期（v1 + v2 同时可用——逐文件迁移——RBL-541 Pages→App 的 API 版）。
- AI 迁移的准确性：1) **映射表驱动**（API 映射表（旧方法名 → 新方法名 + 参数变化）——AI 按映射表迁移（确定性高）；2) **AI 补充**：映射表未覆盖的变更 → AI 推断（置信度标注——低置信进人工清单 RBL-666 哲学）；3) **迁移测试**：迁移后的代码跑同测试集（RBL-685 双包一致性）。
- 追问钩子：为什么「API 升级的 AI 迁移」需要「映射表优先 + AI 兜底」？——映射表 = 确定性迁移（旧方法名 → 新方法名的精确映射——AI 不会搞错）；AI 兜底 = 非确定性的迁移（映射表没覆盖的复杂变更——AI 推断但有幻觉风险）；「映射表优先的哲学」= 确定性优先（RBL-932 codemod 的哲学）：确定性规则能做的不让 AI 猜——AI 只处理规则无法表达的复杂变更。

```typescript
// API 升级的迁移管线
const API_MAPPING = {
  'oldApi.getUser': { newApi: 'newApi.fetchUser', paramChange: 'id → userId' },
  'oldApi.list': { newApi: 'newApi.paginate', paramChange: 'page/limit → cursor' },
  'oldApi.delete': { newApi: 'newApi.remove', paramChange: null },
};
function migrateAPICalls(code: string, mapping: typeof API_MAPPING) {
  const unmigrated: string[] = [];
  let migrated = 0;
  let result = code;
  for (const [old, spec] of Object.entries(mapping)) {
    const regex = new RegExp(`${old.replace(/\./g, '\\.')}`, 'g');
    if (regex.test(result)) {
      result = result.replace(regex, spec.newApi);
      migrated++;
    }
  }
  // AI 兜底：映射表未覆盖的 oldApi 引用
  const remaining = [...result.matchAll(/oldApi\.(\w+)/g)].map(m => m[1]);
  if (remaining.length) unmigrated.push(...remaining);
  return { code: result, migrated, unmigrated };
}
```
