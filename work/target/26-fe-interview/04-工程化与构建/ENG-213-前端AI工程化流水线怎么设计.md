---
title: [ENG-213] 前端 AI 工程化流水线（AI 生成代码进仓库）怎么设计？
date: 2026-11-21
categories: [工程化]
tags: [前端面试, 面试题, 工程化]
type: 面试题
---

## ENG-213：AI 工程化流水线怎么设计？
**答**：
- AI 产物入仓标准：AI 生成代码与人工代码同标准过 CI（lint/type/测试/评审）——不设双标是治理底线；额外加「AI 产物特征检查」（幻觉 API/过期用法）。
- 流水线环节：AI 生成 → 静态校验（AI 幻觉检测：import 不存在的导出即拦）→ 测试生成校验（断言强度，非快照糊弄）→ 评审标注（AI 参与度声明，便于审阅者重点关注）。
- 上下文工程：AI 的输入上下文标准化——组件规范文档/示例代码库/design tokens 结构化进 prompt 模板，让 AI 输出贴合团队约定。
- 效果度量：AI 代码采纳率/返工率/缺陷率 vs 人工基线——没有基线对比就无法判断工具价值。
- 追问钩子：为什么「AI 产物特征检查」单独做——AI 幻觉模式集中且可检测（调不存在的方法/用旧版本 API/编造配置项）；通用 lint 抓不住这些模式，专项检查是漏斗的最后一层。

```javascript
// scripts/ai-verify.js —— AI 产物专项校验
const { exportsOf } = require('./module-graph');
function verifyAiCode(file, ast) {
  const issues = [];
  for (const imp of ast.imports)
    if (!exportsOf(imp.source).has(imp.named))           // 幻觉导入
      issues.push({ type: 'PHANTOM_IMPORT', ...imp });
  if (usesDeprecatedApi(ast, DEPRECATED_MAP))            // 过期 API
    issues.push({ type: 'STALE_API' });
  return issues;   // CI 非零退出拦截
}
```
