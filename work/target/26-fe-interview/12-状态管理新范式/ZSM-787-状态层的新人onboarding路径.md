---
title: [ZSM-787] 状态层的新人 onboarding：一天理解状态架构的路径设计
date: 2026-11-21
categories: [状态管理新范式]
tags: [前端面试, 面试题, ZSM]
type: 面试题
---

## ZSM-787：状态层的新人 onboarding：一天理解状态架构的路径设计

**答**：
- 新人理解状态架构的「一天路径」（四小时读 + 四小时练）：
- **1h 读总图**：ZSM-716 自动生成的状态图 + registry 清单（ZSM-776）——知道有哪些 store、在哪些层。
- **1h 读决策**：ADR 列表（ZSM-712）——知道「为什么是这样」（每个 store 的选型理由与否决方案）。
- **1h 读纪律**：lint 规则清单（ZSM-780）+ 审计八问（ZSM-766）——知道「什么是禁止的」。
- **1h 读工具**：调试工具地图（ZSM-717）——知道「出问题用什么查」（探针/巡检/告警）。
- **练**：完成三个任务——① 用 DevTools 面板复现一个录制的 bug（工具实操）；② 给一个简单 feature 写 store（过 lint + ADR 流程）；③ 修一个标记 good-first-issue 的状态债（技术债表 ZSM-786）。
- onboarding 的产出检验：新人能画出「本次负责 feature 的状态流图」并能答「这个状态为什么放这个层」——通过即上岗，不通过补读对应块。
- 追问钩子：onboarding 材料的「保鲜」机制——全部材料从代码生成（状态图 CI 生成、registry lint 校验、ADR 在代码旁），手写文档会腐烂，生成式文档不会（ZSM-715 的核心论点）。

```javascript
// onboarding 路径清单（可执行）
const ONBOARDING = {
  hour1_总图: {
    read: ['docs/state-graph.mmd（CI 生成，ZSM-716）', 'stores/registry.ts（ZSM-776）'],
    check: '能列出 core/domain/feature/ui 各层有哪些 store',
  },
  hour2_决策: {
    read: ['docs/adr/*.md（ZSM-712）'],
    check: '能说出 cart 拆分与 checkout 服务端权威的理由',
  },
  hour3_纪律: {
    read: ['.eslintrc 状态规则（ZSM-780）', '审计八问（ZSM-766）'],
    check: '能解释为什么 selector 返回对象必须 useShallow',
  },
  hour4_工具: {
    read: ['工具地图（ZSM-717）', '告警 runbook（ZSM-768）'],
    check: '能复现一个录制 bug + 会用重放器',
  },
  practice: [
    '任务①：DevTools 复现录制 bug（replayRecorder）',
    '任务②：写一个 feature store（过 lint + 提交 ADR）',
    '任务③：修一个 TD 债（技术债表 good-first-issue）',
  ],
  graduation: '画出自己 feature 的状态流图 + 答对「为什么放这层」',
}
```
