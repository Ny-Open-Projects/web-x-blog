---
title: [AIC-504] AI 代码审查的信任分级策略
date: 2026-11-22
categories: [AI结对开发工程化]
tags: [前端面试, 面试题, AIC]
type: 面试题
---

## AIC-504：AI 代码审查的信任分级

**答**:
- AI 代码的审查粒度分级（RBL-501 的深化）：1) **T0 - 全量审查**（安全关键：auth/payment/加密——逐行审（不信任 AI 的安全实现）；2) **T1 - 测试驱动审查**（业务逻辑：AI 写 + 测试验证——人审测试覆盖而非实现细节；3) **T2 - 批量审查**（boilerplate/样式/配置——抽样审（10% 抽查——通过率 > 95% 则信任）；4) **T3 - 免审**（AI 生成的注释/文档/命名——不影响运行时行为）；信任分级 = 「风险 × 变更影响」的函数。
- 信任分级的自动化：AST 标注（AI 生成的代码标记 provenance RBL-942——provenance → 自动选择审查级别）；「T0 的白名单」：路径模式（**/auth/**、**/payment/** → 强制 T0）。
- 追问钩子：为什么「AI 写的测试」不能作为「AI 写的实现」的唯一审查依据？——AI 可能同时写错实现和测试（测试匹配了实现的 bug——"AI 验证 AI"的循环）；解决：1) 人写测试、AI 写实现（测试是人的意图声明——AI 实现通过人的测试 = 可信）；2) AI 写实现 + AI 写测试 → 人审测试（测试是人审的代理——测试的正确性比实现的正确性更容易人审）；「测试驱动审查」的信任传递链：人审测试 → 测试验证实现 → 实现可信。

```typescript
// 信任分级策略
type TrustLevel = 0 | 1 | 2 | 3;
function assignTrustLevel(filePath: string, linesChanged: number, provenance: 'ai'|'human'): TrustLevel {
  if (!provenance || provenance === 'human') return 3;   // 人写：免审
  const CRITICAL_PATHS = [/auth\//, /payment\//, /crypto\//, /security\//];
  if (CRITICAL_PATHS.some(p => p.test(filePath))) return 0;   // 安全关键：全审
  if (linesChanged > 200) return 0;                      // 大变更：全审
  if (filePath.includes('test/') || filePath.includes('.test.'))
    return 1;                                            // 测试文件：测试驱动审
  if (filePath.match(/\.(css|scss|json|md)$/)) return 3; // 样式/配置：免审
  return 1;                                              // 默认：测试驱动
}
// CI 的审查路由
// T0 → 人工逐行 + 安全面扫描
// T1 → CI 测试通过即可合并（人抽审测试）
// T2 → 抽样审 + lint
// T3 → 自动合并
```
