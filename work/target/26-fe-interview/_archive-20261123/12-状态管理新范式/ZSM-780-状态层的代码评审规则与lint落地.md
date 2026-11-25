---
title: [ZSM-780] 状态层的代码评审规则：可 lint 的状态纪律清单
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-780：状态层的代码评审规则：可 lint 的状态纪律清单

**答**：
- 评审规则要「可自动化」才有生命力——状态纪律的 lint 清单（eslint 自定义规则 + code review 人工项分列）：
- **可 lint**：1) selector 返回对象必须包 useShallow（AST 检测 selector 内有对象字面量 return）；2) subscribe 必须在 effect cleanup 退订（useEffect 内调用 subscribe 且返回值未返回即报错）；3) persist 必须带 partialize；4) setState 的 updater 内禁止 await（immer/纯函数纪律）；5) store 文件必须有 ADR 注释头。
- **人工评审**：形状四问（ZSM-618）、跨层依赖合理性、新 store 是否必要（能不能用派生替代）。
- 自定义 eslint 规则的收益：review 从「抓低级错误」升级为「讨论设计」，机器管纪律、人管架构——这是评审规则分级的核心目的。
- 规则的灰度落地：先 warn（不阻断）观察两周误报率，调优后转 error 进 CI 门禁；每个规则附 `--fix` 建议（如 useShallow 自动包裹）。
- 追问钩子：lint 抓不住的「状态设计问题」（如该派生的存了值）靠周度架构巡检——ZSM-765 巡检器跑一遍「写时算派生字段是否存在多写路径」「atomFamily 是否有淘汰」。

```javascript
// eslint 自定义规则示例：selector 对象必须 useShallow
// rules/require-use-shallow.js
module.exports = {
  meta: { fixable: 'code' },
  create(context) {
    return {
      CallExpression(node) {
        if (node.callee.name !== 'useStore' && node.callee.name !== 'useXxxStore') return
        const selector = node.arguments[0]
        if (selector?.type !== 'ArrowFunctionExpression') return
        // selector 返回对象字面量且未包 useShallow
        if (selector.body.type === 'ObjectExpression') {
          context.report({
            node,
            message: 'selector 返回对象必须用 useShallow 包裹（防引用抖动）',
            fix: (fixer) => fixer.replaceText(selector, `useShallow(${context.getSourceCode().getText(selector)})`),
          })
        }
      },
    }
  },
}

// 规则清单（分可 lint / 人工）
const LINT_RULES = [
  { rule: 'require-use-shallow', autofix: true },
  { rule: 'subscribe-cleanup-in-effect', autofix: false },
  { rule: 'persist-needs-partialize', autofix: true },
  { rule: 'no-await-in-state-updater', autofix: false },
  { rule: 'store-needs-adr-header', autofix: false },
]
const MANUAL_REVIEW = [
  '形状四问（谁读谁写多频多大）',
  '新 store 必要性（可否派生）',
  '跨层依赖方向',
  '写时算派生的写路径唯一性',
]
// 落地：先 warn 两周 → 误报率 < 5% 转 error 进 CI
```
