---
title: [AIC-594] AI 跨文件变更的一致性
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-594：AI 跨文件变更一致性

**答**:
- AI 跨文件变更的一致性问题：1) **重命名不同步**（AI 重命名 A 文件中的 `getUser` → `fetchUser`，但 B 文件的 import 仍引用旧名——编译错误（或更糟：如果 B 文件也有 getUser——引用到了错误实现）；2) **类型不同步**（A 文件的接口改了字段名 → B 文件使用旧字段名——运行时 undefined；3) **模式不同步**（A 文件改用 zod → B 文件仍用手动校验——验证方式不一致；4) **API 契约不同步**（A 的函数签名变了 → B 的调用参数不匹配——编译或运行时错误。
- 一致性检测：1) **编译检测**（TypeScript 的 cross-file 类型检查——编译期捕获重命名/类型不同步；2) **import 追踪**（A 文件的 export 变了 → 所有 import A 的文件需要更新——依赖闭包追踪 RBL-778）；3) **AI 的跨文件感知**：Agent 模式的优势（Agent 知道所有文件——多文件变更时保持一致——单文件 Inline 模式无法跨文件 RBL-518）。
- 追问钩子：为什么「Agent 模式的跨文件一致性」优于「Inline 模式的逐文件修改」？——Inline 模式 = 逐文件修改（每次只看一个文件——不知道其他文件的变更——A 改了 B 没跟——不一致）；Agent 模式 = 全局视角（一次看到所有文件——跨文件变更保持一致——A 改了 B 同步改）；「跨文件一致性 = Agent 的核心优势」：Inline 模式 = 单文件编辑器；Agent = 全仓库编辑器——多文件变更的场景（重命名/接口变更/模式迁移）只有 Agent 能保证一致性。

```typescript
// AI 跨文件变更的一致性检测
function detectCrossFileInconsistency(changes: Record<string, string>, imports: Map<string, string[]>) {
  const issues: { from: string; to: string; issue: string }[] = [];
  // 检测：重命名的 export 是否在所有 import 文件中同步更新
  for (const [file, code] of Object.entries(changes)) {
    const renamedExports = [...code.matchAll(/export\s+(?:async\s+)?(?:function|const)\s+(\w+)/g)]
      .map(m => m[1]);
    // 检查引用此文件的文件是否使用了新名
    const importers = imports.get(file) ?? [];
    for (const importer of importers) {
      const importerCode = changes[importer];            // 如果 importer 也被修改
      if (!importerCode) continue;                       // importer 未修改——可能需要更新
      // 检查 importer 是否引用了被删除的旧名
      // （简化：此处仅标记需要人工确认）
      issues.push({ from: file, to: importer,
        issue: `export 变更——确认 ${importer} 的 import 已同步` });
    }
  }
  return issues;
}
```
