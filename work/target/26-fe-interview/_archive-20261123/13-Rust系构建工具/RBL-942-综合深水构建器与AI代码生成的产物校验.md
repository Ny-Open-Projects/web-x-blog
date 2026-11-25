---
title: [RBL-942] 综合深水：构建器对 AI 生成代码的产物校验——生成代码的「同等人肉标准」
date: 2026-11-22
categories: [Rust系构建工具]
tags: [前端面试, 面试题, RBL]
type: 面试题
---

## RBL-942：综合深水：构建器对 AI 生成代码的产物校验——生成代码的同等标准

**答**:
- AI 生成代码进入构建的治理原则：**与人写的代码同一标准**（lint/类型/测试/审计全过）——「AI 代码降标准」是安全债（生成代码的幻觉依赖/注入漏洞/许可证污染概率更高）；构建器的增量治理点：1) **幻觉依赖检测**（import 的包不在 lockfile——AI 幻觉出「看起来合理但不存在」的包名——typosquatting 攻击也借此向量）；2) 生成代码的来源标记（provenance：AI 生成的模块标注——审计时可区分）；3) 生成代码的 diff 审查增强（AI 代码的 PR 自动附加「安全扫描强化」——敏感模式扫描 RBL-762 全开）。
- 构建期的幻觉依赖检测：import 解析失败本来就会构建失败（RBL-1001）——但「拼错的真实包名」会成功（typosquatting 风险）——防线是「新依赖引入告警」（lockfile diff RBL-772：AI 代码引入的依赖必须有显式 package.json 声明 PR）。
- 生成代码的许可证污染：AI 可能复现训练数据的受限代码（GPL 片段/GPL 证书检测——启发式：特征函数签名/注释）——与许可审计（RBL-807）衔接。
- 治理的度量：AI 代码的「缺陷密度 vs 人写」对比数据（用于调策略——AI 代码更差则强化门禁，更好则可放宽）——数据驱动而非立场驱动。
- 追问钩子：为什么「幻觉依赖」是 AI 时代供应链攻击的新向量？——攻击者注册 AI 常幻觉出的包名（slopsquatting）：AI 生成 `import lodash-utils-deep` → 包不存在 → 开发者 `npm i`（想「AI 应该知道」）→ 恶意包进依赖树；防线「幻觉依赖 = 构建失败 + 新依赖显式 PR」把「自然安装」变成「审计点」——AI 供应链治理的本质仍是「把隐式信任变显式」（RBL-910 的延伸）。

```javascript
// 幻觉依赖防线
async function guardAIDeps(code, lockfile, { isAIProvenance }) {
  const imports = [...code.matchAll(/(?:from|require)\(\s*['"]([^.'"][^'"]*)['"]/g)]
    .map(m => topLevel(m[1]));
  const problems = [];
  for (const pkg of new Set(imports)) {
    if (!lockfile[pkg]) {
      problems.push({ pkg, detail: 'import 的包不在 lockfile——疑似幻觉依赖，禁止安装前人工核实' });
      continue;
    }
    if (isAIProvenance && !declaredInPkgJson(pkg))
      problems.push({ pkg, detail: 'AI 代码引入依赖但无显式声明 PR——补声明并过审' });
  }
  return problems;                                       // 非空 = 构建失败（审计点前置）
}
// provenance 标记（构建器注入）
// 源文件头：/* provenance: ai-assisted generator=copilot date=2026-11 */
const provenanceOf = (code) => /provenance:\s*ai-assisted/.test(code.split('\n')[0] ?? '');
```
